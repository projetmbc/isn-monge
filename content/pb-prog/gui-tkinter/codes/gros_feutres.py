# ------------------ #
# -- IMPORTATIONS -- #
# ------------------ #

import random
import tkinter


# ---------------------------------------------- #
# -- ACTIONS FAITES PAR L'INTERFACE GRAPHIQUE -- #
# ---------------------------------------------- #

DELTA = 5

TOUTES_LES_COULEURS = ['black', 'blue', 'magenta', 'red', '#ffff99']

# Les valeur choisies ci-dessous indique que rien n'a été tracé pour le moment
# (ceci est nécessaire pour que le ``global`` de la fonction ``ajoute_disque``
# ci-dessous fonctionne lors du tout premier clic.
DERNIER_DISQUE_ID = -1

COULEUR = -1

X_CENTRE = -1
Y_CENTRE = -1
RAYON    = -1

def ajoute_disque():
    global X_CENTRE, Y_CENTRE, RAYON
    global DERNIER_DISQUE_ID, COULEUR

    DERNIER_DISQUE_ID = canevas.create_oval(
        X_CENTRE - RAYON, Y_CENTRE - RAYON,
        X_CENTRE + RAYON, Y_CENTRE + RAYON,
        fill    = COULEUR,
        outline = COULEUR
    )

def nouveau_disque(evenement):
    global X_CENTRE, Y_CENTRE, RAYON
    global TOUTES_LES_COULEURS, COULEUR

    RAYON = random.randint(5, 25)

    X_CENTRE = evenement.x
    Y_CENTRE = evenement.y

    COULEUR = random.choice(TOUTES_LES_COULEURS)

    ajoute_disque()


# On autorise l'utilisateur à sortir du canevas !

def bouge_gauche(evenement):
    global X_CENTRE

    X_CENTRE -= DELTA

    ajoute_disque()

def bouge_droite(evenement):
    global X_CENTRE

    X_CENTRE += DELTA

    ajoute_disque()

def bouge_bas(evenement):
    global Y_CENTRE

    Y_CENTRE += DELTA

    ajoute_disque()

def bouge_haut(evenement):
    global Y_CENTRE

    Y_CENTRE -= DELTA

    ajoute_disque()


# --------------------------- #
# -- L'INTERFACE GRAPHIQUE -- #
# --------------------------- #

# Fenêtre principale placée au centre de l'écran
racine = tkinter.Tk()
racine.title('Cliquer pour retrouver')

larg_fen = 500
haut_fen = 500

larg_ecran = racine.winfo_screenwidth()
haut_ecran = racine.winfo_screenheight()

xpos_fen = larg_ecran//2 - larg_fen//2
ypos_fen = haut_ecran//2 - haut_fen//2

racine.geometry(
    "{0}x{1}+{2}+{3}".format(
        larg_fen, haut_fen,
        xpos_fen, ypos_fen
    )
)

# Cadre
cadre = tkinter.Frame(master = racine)
cadre.grid(row = 0, column = 0)

# Ajout du canevas où les dessins seront faits.
larg_canevas = larg_fen
haut_canevas = haut_fen

canevas = tkinter.Canvas(
    master     = cadre,
    width      = larg_canevas,
    height     = haut_canevas,
    background = 'grey'
)
canevas.grid(row = 0, column = 0, sticky = "ew")


# Agir quand on fait un clic gauche.
canevas.bind(
    sequence = '<Button-1>',
    func     = nouveau_disque
)


# Associer l'appui des touches à une fonction.
#
# ATTENTION ! Nous devons laisser travailler la fenêtre principale et non
# le cadre.
racine.bind(
    sequence = '<Left>',
    func     = bouge_gauche
)

racine.bind(
    sequence = '<Right>',
    func     = bouge_droite
)

racine.bind(
    sequence = '<Up>',
    func     = bouge_haut
)

racine.bind(
    sequence = '<Down>',
    func     = bouge_bas
)

# -------------------------------- #
# -- LANCEMENT DE L'APPLICATION -- #
# -------------------------------- #

racine.mainloop()
