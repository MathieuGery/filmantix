import { Container } from '@/components/Container'
import Plot from '@/components/Plot'
import Movie from '@/components/Movie'
import Head from 'next/head'
import { useEffect, useState } from 'react'
import { History } from '@/components/History'


function HandleError(props) {
  if (props.error != null) {
    return <a className="animate-pulse [animation-iteration-count:4] ml-4 text-red-500 text-l font-bold">😵‍💫 Mot Inconnu</a>
  }
}

export default function Home() {
  const [plot, setPlot] = useState(null)
  const [guessWord, setGuessWord] = useState("")
  const [word, setWord] = useState("")
  const [error, setError] = useState(null)
  const [movie, setMovie] = useState(null)
  const [history, setHistory] = useState({ "guesses": [] })

  const handleOnSubmit = async (e) => {
    e.preventDefault();
    try {
      const plot_obscured = JSON.parse(localStorage.getItem("plot"))
      const res = await fetch(
        `https://filmantix-api.gery.me/api/testModel/`,
        {
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            "word": word.toLowerCase(),
            "title": plot_obscured.plot.title_obsucred
          }),
          method: "POST"
        }
      );
      const data = await res.json();
      setError(null)
      setGuessWord(word.toLowerCase())
      const guess_history = JSON.parse(localStorage.getItem("guess_history"))
      guess_history.guesses.push(word)
      for (const property in data.score) {
        if (data.score[property].value >= plot_obscured.plot.plot_obsucred[data.score[property].id].score) {
          plot_obscured.plot.plot_obsucred[data.score[property].id].guess = data.score[property].word
          plot_obscured.plot.plot_obsucred[data.score[property].id].score = data.score[property].value
        }
      }
      for (const property in data.title) {
        if (data.title[property].value >= plot_obscured.plot.title_obsucred[data.title[property].id].score) {
          plot_obscured.plot.title_obsucred[data.title[property].id].guess = data.title[property].word
          plot_obscured.plot.title_obsucred[data.title[property].id].score = data.title[property].value
        }
      }
      if (data.movie) {
        setMovie(data.movie)
        plot_obscured.movie = data.movie
      }
      localStorage.setItem("plot", JSON.stringify(plot_obscured))
      localStorage.setItem("guess_history", JSON.stringify(guess_history))
      setHistory(guess_history)
      setPlot(plot_obscured)
    } catch (err) {
      console.log(err);
      setError("Mot Inconnu")
    }
    setWord("")
  };

  const callAPI = async () => {
    try {
      const res = await fetch(
        `https://filmantix-api.gery.me/api/plot/`,
        {
          headers: { 'Content-Type': 'application/json' }
        }
      );
      const data = await res.json();
      setPlot(data)
      if (localStorage.getItem("guess_history")) {
        setHistory(JSON.parse(localStorage.getItem("guess_history")))
      }
      if (localStorage.day != data.plot.day_num) {
        console.log("New day, new plot good luck!")
        localStorage.setItem("plot", JSON.stringify(data))
        localStorage.setItem("day", data.plot.day_num)
        localStorage.setItem("guess_history", JSON.stringify({ "guesses": [] }))
      } else {
        const data_from_lc = JSON.parse(localStorage.getItem("plot"))
        setPlot(JSON.parse(localStorage.getItem("plot")))
        if (data_from_lc.movie) {
          console.log("You have already win for today!")
          setMovie(data_from_lc.movie)
          setHistory(JSON.parse(localStorage.getItem("guess_history")))
        }
      }
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    callAPI()
  }, [])

  if (!plot) {
    return (<span className='text-teal-500'>Loading</span>)
  }
  return (
    <>
      <Head>
        <title>
          Filmantix - Trouver le film du jour !
        </title>
        <meta
          name="description"
          content="Filmantix - Trouver le film du jour à partir de son synopsis!"
        />
      </Head>
      <Container className="mt-16 sm:mt-15">
        <div className="lg:order-first lg:row-span-2">
          <h1 className="text-4xl font-bold tracking-tight text-zinc-800 dark:text-zinc-100 sm:text-5xl">
            Bienvenue sur Filmantix ! 🎬🍿
          </h1>
          <div className='grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-20 mt-10'>
            <div className="order-last sm:order-first border border-teal-500 rounded-xl px-5 py-5 flex-1">
              <h1 className='text-xl font-bold text-white'>Historique</h1>
              {history.guesses.length != 0 && <History history={history} />}
            </div>

            <div className="border border-teal-500 rounded-xl px-5 py-5 flex-1 text-left">
              <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100">
                🗓 Mot Numéro <span className="text-teal-500">{localStorage.day}</span>
              </p>
              <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100 mt-2">
                😎 Trouvé par
                <span className="text-teal-500"> {plot.plot.nb_found} </span>
                <span> personnes</span>
              </p>
              <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100 mt-2">
                🎥 Le film d'hier était
                <span className="text-teal-500"> Matrix </span>
              </p>
            </div>
          </div>
        </div>
        {movie != null &&
          <Movie data={movie} className="animate-bounce [animation-iteration-count:1.5]" />
        }
        <div className="mt-10 mx-2">
          <form onSubmit={handleOnSubmit}>
            <input
              type="mot"
              placeholder="🔎 Mot"
              aria-label="Mot"
              value={word}
              required
              onChange={event => setWord(event.target.value)}
              className="min-w-0 placeholder:p-1 flex-auto appearance-none rounded-md border ring-zinc-800 dark:ring-white border-zinc-900/10 bg-white ring-2 px-2 py-[calc(theme(spacing.2)-1px)] shadow-md shadow-zinc-800/5 placeholder:text-zinc-400 focus:border-teal-500 focus:outline-none focus:ring-4 focus:ring-teal-500/10 dark:border-zinc-700 dark:bg-zinc-700/[0.15] dark:text-zinc-200 dark:placeholder:text-zinc-500 dark:focus:border-teal-400 dark:focus:ring-teal-400/10 sm:text-l"
            />
            <HandleError error={error} />
          </form>
        </div>
        <div>
          <Plot data={plot} guessWord={guessWord} className="mt-10" />
        </div>
      </Container>
    </>
  )
}
