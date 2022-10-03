import clsx from 'clsx'


function Plot({ data, className }) {
  if (!data) {
    return (<span className='text-teal-500'>Loading</span>)
  }
  return (
    <div className={clsx(className, "flex-row flex flex-wrap border border-zinc-300 rounded-xl p-5")}>
      {data.plot.plot_obsucred.map((word, item) => {
        if ([",", "-", ":", "'", ".", "!", "?", ";"].some(item => word.word.includes(item))) {
          return <span key={item} id={word.id} className="select-none text-white mt-2 rounded">{word.word}</span>
        }
        else if ([" "].some(item => word.word.includes(item))) {
          return <span key={item} id={word.id} className="select-none text-teal-500 bg-teal-500 mx-1 mt-2 rounded px-2">{word.word}</span>
        }
        else {
          return <span key={item} id={word.id} className="animate-bounce [animation-iteration-count:1.5] select-none text-white mt-2 ml-1 rounded">{word.word}</span>
        }
      })}
    </div>
  )
}

export default Plot;
