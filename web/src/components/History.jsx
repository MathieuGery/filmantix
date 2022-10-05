export function History({history}) {
  return (
    <div>
      {history.guesses.slice(-5).reverse().map((word, index) => {
        return (
          <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100 mt-2"><span className="text-teal-500 mr-3">{history.guesses.length - index}</span>{word}
          </p>)
      })}
    </div>
  )
}
