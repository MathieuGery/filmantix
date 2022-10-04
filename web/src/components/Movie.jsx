import clsx from 'clsx'
import Image from 'next/image';
import { Button } from './Button';
function Movie({ data, className }) {
  return (
    <div>
      <div className={clsx(className, "border border-teal-500 rounded-xl p-5 mt-4")}>
        <div className="grid grid-cols-1">
          <h1 className='text-white text-4xl font-extrabold'>🥳 Félicitation vous avez trouvé le film du jour !</h1>
          <div className="sm:flex">
            <div className="mt-10">
              <Image
                src={data.poster}
                alt=""
                height="200"
                width="140%"
                layout='fixed'
                className="aspect-square rounded-2xl bg-zinc-100 object-cover dark:bg-zinc-800"
              />
            </div>
            <div className="flex-1 space-y-2">
              <p className="text-2xl font-bold tracking-tight text-white mt-4 mb-5 sm:ml-10">
                {data.title}
              </p>
              <p className="text-l font-bold tracking-tight text-white sm:ml-14">
                Pays d'origine: <span className="text-teal-500">{data.origin_country}</span>
              </p>
              <p className="text-l font-bold tracking-tight text-white sm:ml-14">
                Directeur: <span className="text-teal-500">{data.director}</span>
              </p>
              <p className="text-l font-bold tracking-tight text-white sm:ml-14">
                Durée: <span className="text-teal-500">{data.runtime}</span>
              </p>
              <p className="text-l font-bold tracking-tight text-white sm:ml-14">
                Sortie: <span className="text-teal-500">{data.release_date}</span>
              </p>
              <p className="text-l font-bold tracking-tight text-white sm:ml-14">
                bouton
              </p>
            </div>
          </div>
        </div>
      </div >
    </div>
  )
}

export default Movie;
