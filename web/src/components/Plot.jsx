import clsx from 'clsx'


function Plot({ data, className }) {
  if (!data) {
    return (<span className='text-teal-500'>Loading</span>)
  }
  return (
    <div className={clsx(className, "flex-row flex flex-wrap border border-zinc-300 rounded-xl p-5")}>
      {data.plot.plot_obsucred.map(word => {
        if ([",", "-", ":", "'", ".", "!", "?", ";"].some(item => word.word.includes(item))) {
          return <span id={word.id} className="select-none text-white mt-2 rounded">{word.word}</span>
        }
        else {
          return <span id={word.id} className="select-none text-teal-500 bg-teal-500 mx-1 mt-2 rounded px-2">{word.word}</span>
        }
      })}
    </div>
  )
}

export default Plot;
