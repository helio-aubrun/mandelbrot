# mandelbrot

## Les fractales
Les fractales sont des objets mathématiques fascinants qui défient souvent notre intuition.
Leur caractéristique principale est l'auto-similarité, ce qui signifie que lorsqu'on zoome sur une partie d'une fractale, on observe une structure qui ressemble à l'ensemble global.
Cette propriété se répète à différentes échelles, ce qui confère aux fractales une complexité infinie et une beauté remarquable.
Les fractales peuvent être générées à l'aide de processus itératifs simples, comme la répétition d'une transformation sur une forme de base.
Les exemples classiques incluent l'ensemble de Mandelbrot et l'ensemble de Julia, qui sont générés à partir de simples équations algébriques.
En dehors des mathématiques pures, les fractales ont trouvé des applications dans de nombreux domaines. En physique, elles sont utilisées pour modéliser des phénomènes tels que la croissance des cristaux et la turbulence.
En biologie, elles sont observées dans les structures des arbres, des poumons et des réseaux vasculaires. Les fractales sont également utilisées en informatique pour la compression d'images et la génération de paysages virtuels.

## Implémentation
De votre tempérament naturellement curieux et avide de connaissances, votre nouvelle obsession est la figure fractale ! Vous explorez différents types de fractales et vous les implémentez à l'aide de Python.
Les fractales sont souvent générées à l'aide de concepts mathématiques tels que les équations récursives, les nombres complexes et l'itération :
● Équations récursives : Ces équations définissent comment la forme de base évolue au fil de plusieurs itérations, entraînant l'émergence de motifs complexes.
● Nombres complexes : Les nombres complexes se composent d'une partie réelle et d'une partie imaginaire, permettant la représentation à la fois de l'amplitude et de la direction. 
Dans le contexte des fractales, les nombres complexes sont utilisés pour définir des points dans le plan complexe, où chaque point correspond à une itération unique dans le processus de génération fractale.
● Itération : L'itération est un concept fondamental dans la génération de fractales, où une série d'étapes répétitives est appliquée pour créer des motifs complexes. 
Lors de chaque itération, une règle de transformation est appliquée à chaque point de la fractale, déterminant sa position dans l'itération suivante.
À travers des itérations répétées, la structure fractale évolue, révélant des motifs autosimilaires à différentes échelles.

## Triangle de Sierpiński
Le triangle de Sierpiński, ou tamis de Sierpiński, également appelé par Mandelbrot le joint de culasse de Sierpiński1, est une fractale, du nom de Wacław Sierpiński qui l'a décrit en 19152.
Il peut s'obtenir à partir d'un triangle « plein », par une infinité de répétitions consistant à diviser par deux la taille du triangle puis à les accoler en trois exemplaires par leurs sommets pour former un nouveau triangle. 
À chaque répétition le triangle est donc de même taille, mais « de moins en moins plein ».

## Mandelbrot
L'ensemble de Mandelbrot a été découvert par Gaston Julia et Pierre Fatou1 avant la Première Guerre mondiale. Sa définition et son nom actuel sont dus à Adrien Douady, en hommage aux représentations qu'en a réalisées Benoît Mandelbrot dans les années 1980. Cet ensemble permet d'indicer les ensembles de Julia associés à la suite : à chaque point du plan complexe correspond un ensemble de Julia différent. Les points de l'ensemble de Mandelbrot correspondent précisément aux ensembles de Julia connexes, et ceux en dehors correspondent aux ensembles de Julia non connexes. Cet ensemble est donc intimement lié aux ensembles de Julia, ils produisent d'ailleurs des formes similairement complexes.

## Julia
En dynamique holomorphe, l'ensemble de Julia et l'ensemble de Fatou sont deux ensembles complémentaires l'un de l'autre, définis à partir du comportement d'une fonction (ou d'une application) holomorphe par composition itérée avec elle-même.

## Flocon de Koch
Le flocon de Koch est l'une des premières courbes fractales à avoir été décrites, bien avant l'invention du terme « fractal(e) » par Benoît Mandelbrot.
Elle a été inventée en 1904 par le mathématicien suédois Helge von Koch.

## Burning ship
La fractale burning ship (« navire en feu », en anglais), décrite pour la première fois par Michael Michelitsch et Otto E. Rössler en 1992, est générée dans le plan complexe.
La fractale est définie par l'ensemble des points ne divergeant pas à l'infini.
Très similaire à l'ensemble de Mandelbrot, elle en diffère par le fait que l'on considère la valeur absolue des composantes réelles et imaginaires.
