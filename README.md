# Project_3_OC
Il s'agit du 3ième projet à réaliser sur OpenClassrooms pour le parcours de Développeur d'Applications Web spécialisé en Python.

Il faut créer un jeu de labyrinthe en Python où MacGyver doit trouver la sortie. Un garde l'attend devant la sortie. MacGyver doit ramasser 3 objets afin de fabriquer une seringue et d'endormir le garde. Ces 3 objets sont une aiguille, un tube en plastique et de l'éther. Ils seront disposés aléatoirement dans le labyrinthe.

Si MacGyver parvient à ramasser les 3 objets, à endormir le garde et à sortir du labyrinthe, il a gagné. S'il se présente devant le garde sans les 3 objets, il meurt.

Ce repository contient 11 éléments. Il y a les dossiers images, models et music qui contiennent respectivement les images, le plateau et la musique du jeu.

Le fichier .gitignore contient les éléments à ne pas commiter. Le fichier README explique le projet et le fichier requirements.txt contient toutes les bibliothèques externes à installer. Pour l'instant, il y a juste Pygame.

game.py est le fichier principal. Il faut cliquer dessus pour lancer le jeu. characters.py contient les classes qui créent les personnages du jeu. item.py contient la classe Item qui crée les objets du jeu. labyrinth.py crée et affiche le labyrinthe du jeu. 

Enfin, constants.py contient toutes les constantes du jeu. C'est ce fichier qu'il faut modifier pour changer des images ou des coordonnées de départ.
