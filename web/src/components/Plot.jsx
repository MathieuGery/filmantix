import clsx from 'clsx'

function roundNearest100(num) {
  return Math.round(num / 100) * 100;
}

function Plot({ data, guessWord, className }) {
  if (!data) {
    return (<span className='text-teal-500'>Loading</span>)
  }
  return (
    <div className={clsx(className, "flex-row flex flex-wrap border border-zinc-300 rounded-xl p-5")}>
      <div className="mb-4 flex-row flex flex-wrap">
        {data.plot.title_obsucred.map((word, item) => {
          if ([",", "-", ":", "'", ".", "!", "?", ";", "’", "'"].some(item => word.word.includes(item))) {
            return <span key={item} id={word.id} className="select-none text-white mt-2 rounded">{word.word}</span>
          }
          if (word.score == 100) {
            return <span key={item} id={word.id} className="animate-bounce [animation-iteration-count:1.5] select-none text-white mt-2 ml-1 text-2xl">{word.guess}</span>
          } else if (word.score >= 25) {
            return <span key={item} id={word.id} className="select-none text-white bg-red-500 mx-1 mt-2 rounded px-2 text-2xl">{word.guess}</span>
          } else {
            return <span key={item} id={word.id} className="select-none text-2xl text-teal-500 bg-teal-500 mx-1 mt-2 rounded px-2">{word.word}</span>
          }
        }
      )}
      </div>
      <div className="flex-row flex flex-wrap">
        {data.plot.plot_obsucred.map((word, item) => {
          if ([",", "-", ":", "'", ".", "!", "?", ";", "’", "'"].some(item => word.word.includes(item))) {
            return <span key={item} id={word.id} className="select-none text-white mt-2 rounded">{word.word}</span>
          }
          if (word.score == 100) {
            return <span key={item} id={word.id} className="animate-bounce [animation-iteration-count:1.5] select-none text-white mt-2 ml-1 text-l">{word.guess}</span>
          } else if (word.score >= 36 && word.score <= 43) {
            return <span key={item} id={word.id} className="select-none text-white bg-orange-400 mx-1 mt-2 rounded px-2">{word.guess}</span>
          } else if (word.score >= 68) {
            return <span key={item} id={word.id} className="select-none text-white bg-red-700 mx-1 mt-2 rounded px-2">{word.guess}</span>
          } else if (word.score > 53 && word.score < 68) {
            return <span key={item} id={word.id} className="select-none text-white bg-orange-600 mx-1 mt-2 rounded px-2">{word.guess}</span>
          } else if (word.score > 43 && word.score < 53) {
            return <span key={item} id={word.id} className="select-none text-white bg-orange-500 mx-1 mt-2 rounded px-2">{word.guess}</span>
          } else {
            return <span key={item} id={word.id} className="select-none text-teal-500 bg-teal-500 mx-1 mt-2 rounded px-2">{word.word}</span>
          }

        })}
      </div>
    </div>
  )
}

export default Plot;
