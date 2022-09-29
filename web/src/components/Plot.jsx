import clsx from 'clsx'
import { useRouter } from 'next/router'
import { useEffect } from 'react'
import { useState } from 'react'

function Plot({ plot, className }) {
  const [data, setData] = useState(null)
  const router = useRouter()
  useEffect(() => {
    console.log("coucou");
    setData("mabite")
    // setData({
    //   "plot": [
    //     {"id": 1, "word": "keep"},
    //     {"id": 2, "word": "tota"},
    //     {"id": 3, "word": "qsdfqsef"},
    //     {"id": 4, "word": "kqsdfep"},
    //     {"id": 5, "word": "qsdfqsefp"},
    //   ]
    // })
  }, [router.pathname])

  return (
    <div className={clsx(className, "flex-row flex flex-wrap border border-zinc-300 rounded-xl p-5")}>
      <span className="text-white pl-3">Bonjour</span>
      <span className="text-white pl-3">Je</span>
      <span className="text-white pl-3">Suis</span>
      <span className="text-white pl-3">Le</span>
      <span className="text-white pl-3">Facteur</span>
      <span className="text-white pl-3">de</span>
      <span className="text-white pl-3">la</span>
      <span className="text-white pl-3">veille</span>
      <span className="text-white pl-3">bourse</span>
      <span className="text-white pl-3">{data}</span>
    </div>
  )
}


export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://dumbstockapi.com/stock?exchanges=NYSE')
  const posts = await res.json()
  console.log("mabite")
  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      plot,
    },
  }
}

export default Plot;