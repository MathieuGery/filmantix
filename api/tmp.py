from imdb import Cinemagoer, locale
# from colorama import Fore, init
import re

rgx = re.compile('\w+')

# init(autoreset=True)

def get_plot(id: str):
    ia = Cinemagoer()

    #TODO find HOW TO GET FRENCH 
    # print(Fore.CYAN + "requesting movie")
    # movie = ia.get_movie(id)
    # print(Fore.CYAN + "got movie")
    # # print(movie['plot'])
    # return movie['plot'][0]

    text = """
    Dans un hôtel abandonné d'une grande ville, une escouade de police coince Trinity, qui les domine avec ses capacités surhumaines. Elle s'enfuit, poursuivie par la police et un groupe d'agents adaptés capables d'exploits surhumains similaires aux siens. Elle répond à la sonnerie d'un téléphone public et disparaît juste avant que l'agent Smith n'écrase un camion dans sa cabine. Celui-ci apprend néanmoins qu'elle est à la recherche d'un certain « Neo ».

    Le programmeur informatique Thomas Anderson, connu sous son pseudonyme de piratage « Neo », est intrigué par les rencontres répétées en ligne avec l'expression « The Matrix », qui lui demandent de suivre « le lapin blanc ». Acceptant l'invitation d'une jeune femme tatouée d'un lapin blanc, Neo est contacté dans une discothèque par Trinity, qui lui dit qu'un homme nommé Morpheus a les réponses qu'il cherche sur la matrice. Le lendemain, au travail, après que Neo a été réprimandé pour ses retards, il est contacté par Morpheus par téléphone cellulaire au moment où une équipe d'agents et de policiers, dirigée par l'agent Smith, arrive sur son lieu de travail, à sa recherche. Bien que Morpheus tente de le guider par téléphone vers une issue, Neo choisit d'être capturé plutôt que de risquer de s'échapper par un échafaudage accolé au rebord du gratte-ciel. L'agent Smith et ses acolytes tentent alors de contraindre Neo à les aider à localiser Morpheus, qu'ils prétendent être un terroriste à capturer mort ou vif. Neo insiste sur son droit à un appel téléphonique pour contacter un avocat, mais les agents font disparaître sa bouche et un implant robotique en forme d'insecte est inséré dans son nombril. Neo se réveille de ce qu'il croit être un cauchemar, répond au téléphone avant d'être emmené par Trinity et des rebelles pour rencontrer Morpheus. En chemin, ils enlèvent l'insecte espion de l'estomac de Neo, prouvant que le cauchemar qu'il a vécu était réel.

    Lors de leur première rencontre, Morpheus offre à Neo le choix entre deux pilules : rouge pour révéler la vérité sur la matrice et bleue pour le ramener à son ancienne vie. Neo avale la pilule rouge, sa réalité se désintègre, il se réveille nu et le crâne rasé dans une capsule remplie de liquide, parmi d'innombrables autres humains attachés à un système de production électrique élaboré. Détecté par une sentinelle robotique, il est relâché puis récupéré et amené à bord du vaisseau volant de Morpheus, le Nebuchadnezzar.

    Alors que Neo se remet d'une vie d'inactivité physique dans le pod, Morpheus explique la situation : au début du xxie siècle, une guerre a éclaté entre l'humanité et les intelligences artificielles. Après que les humains ont bloqué l'accès des machines à l'énergie solaire en assombrissant le ciel, les machines ont réagi en « cultivant » les humains et en récoltant leur énergie bioélectrique, tout en gardant leur esprit apaisé dans la matrice grâce à une réalité simulée partagée, modelée sur le monde tel qu'il était en 1999. Les machines ont remporté la guerre et la ville souterraine de Sion est le dernier refuge des humains libres. Morpheus et son équipage sont un groupe de rebelles qui piratent la Matrice pour « débrancher » les humains asservis et les recruter. Leur compréhension de la nature simulée de la matrice leur permet de contourner ses lois physiques.

    D'abord réticent au concept, Neo est programmé par Tank à toutes les formes de combat. Les prouesses de Neo lors d'un entraînement virtuel cimentent la conviction de Morpheus que Neo est « l'Élu », un humain possédant des pouvoirs exceptionnels, prophétisé pour libérer l'humanité. Morpheus avertit Neo que la mort dans la matrice tue le corps physique et que les agents sont des programmes informatiques sensibles qui éliminent les menaces pour le système, tandis que des machines appelées Sentinelles éliminent les rebelles dans le monde réel. L'une d'elles est justement à la poursuite du Nebuchadnezzar. L'équipage prépare une arme EMP pour s'en débarrasser.

    Cypher, un membre d'équipage regrettant sa vie d'avant, a trahi son équipage en s'alliant avec l'agent Smith en échange d'une vie prospère dans la matrice. Le groupe entre dans la Matrice pour visiter l'Oracle, la prophète qui a prédit que « l'Élu » émergerait. Entourée d'enfants aux pouvoirs télékinétiques, elle suggère à Neo qu'il n'est pas le seul « élu » et prévient qu'il devra choisir entre la vie de Morpheus et la sienne. Avant qu'il puisse quitter la matrice, les agents et la police tendent une embuscade au groupe, renseignés par Cypher. Les rebelles essayent de se frayer un chemin dans les canalisations du bâtiment assiégé mais Morpheus est capturé en train de combattre Smith pour gagner du temps afin que le reste du groupe puisse s'échapper. Cypher quitte la matrice et assassine plusieurs membres d'équipage alors qu'ils sont sans défense. Avant que le traître ne puisse tuer Neo, Tank, qui n'était qu'inconscient, se réveille et tue Cypher puis s'empresse de retirer Neo et Trinity de la matrice.

    Les agents torturent Morpheus pour tenter de lui soutirer ses codes d'accès à l'ordinateur central de Sion. Tank, pensant la situation perdue, propose de débrancher Morpheus avant qu'il ne parle et abréger ses souffrances. S'opposant à cette décision, Neo décide de retourner dans la Matrice pour le sauver, comme l'Oracle l'a prophétisé. Trinity insiste pour l'accompagner. Armés jusqu'aux dents, ils attaquent à eux seuls le bâtiment où est détenu Morpheus, gardé par l'armée. En sauvant finalement Morpheus, Neo prend confiance en ses capacités, tenant tête aux agents. Morpheus et Trinity sortent de la Matrice, mais Smith leur tend une embuscade et tue Neo d'une balle avant qu'il ne puisse fuir. Alors qu'un groupe de Sentinelles attaque le Nebuchadnezzar, Trinity, pensant Neo mort, lui avoue son amour et révèle que l'Oracle lui a prédit qu'elle tomberait amoureuse de « l'Élu ». Contre toute attente, Neo se réveille avec de nouvelles capacités pour percevoir et contrôler la matrice. Il bat Smith ainsi que les autres agents et quitte la matrice au moment où l'impulsion électromagnétique du vaisseau désactive les Sentinelles.

    De retour dans la Matrice, Neo passe un coup de téléphone, promettant aux machines qu'il montrera à leurs prisonniers « un monde où tout est possible ». Il raccroche et s'envole.
    """
    
    text = rgx.findall(text)
    return (' '.join(text), len(text))