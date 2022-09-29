import clsx from 'clsx'

export function Plot({ children, className }) {
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
      <span className="text-white pl-3">lille</span>
    </div>
  )
}
