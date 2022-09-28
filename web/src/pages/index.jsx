import { Container } from '@/components/Container'
import { SimpleLayout } from '@/components/SimpleLayout'
import Head from 'next/head'

export default function Home() {
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
          <div className='grid grid-cols-1 sm:grid-cols-2 gap-20 mt-10'>
            <div class="border-2 border-teal-500 rounded-xl px-5 py-5 flex-1 text-center">
              <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100">
                Les carrés <span className="text-teal-500">100</span>
              </p>
              <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100 mt-2">
                Liste des mots
              </p>
            </div>

              <div class="border-2 border-teal-500 rounded-xl px-5 py-5 flex-1 text-center">
                <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100">
                  🗓 Mot Numéro <span className="text-teal-500">100</span>
                </p>
                <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100 mt-2">
                  😎 Trouvé par
                  <span className="text-teal-500"> 900 </span>
                  <span> personnes</span>
                </p>
                <p className="text-l font-bold tracking-tight text-zinc-800 dark:text-zinc-100 mt-2">
                  🎥 Le film d'hier était
                  <span className="text-teal-500"> Matrix </span>
                </p>
            </div>
          </div>
          <div class="mt-10 mx-10">
            <input
              type="mot"
              placeholder="Mot"
              aria-label="Mot"
              required
              className="min-w-0 flex-auto appearance-none rounded-md border ring-white border-zinc-900/10 bg-white ring-2 px-3 py-[calc(theme(spacing.2)-1px)] shadow-md shadow-zinc-800/5 placeholder:text-zinc-400 focus:border-teal-500 focus:outline-none focus:ring-4 focus:ring-teal-500/10 dark:border-zinc-700 dark:bg-zinc-700/[0.15] dark:text-zinc-200 dark:placeholder:text-zinc-500 dark:focus:border-teal-400 dark:focus:ring-teal-400/10 sm:text-l"
            />
          </div>
        </div>
      </Container>
    </>
  )
}
