# ------------------ #
# -- IMPORTATIONS -- #
# ------------------ #

import random
import tkinter


# ---------------------------------------------- #
# -- ACTIONS FAITES PAR L'INTERFACE GRAPHIQUE -- #
# ---------------------------------------------- #

# AVERTISSEMENT 1 : la modélisation du choc est mauvaise. Améliorer ceci est
# un exrcice facile qui vosu est conseillé de faire.
#
# AVERTISSEMENT 2 : à partir de trois billes, la gestion des collisions doit
# se faire plus intelligemment. Venir me voir pour savoir pourquoi.

DX_1 = DY_1 = DX_2 = DY_2 = 0

def debute_animation():
    global bouton_lancer

    global DX_1, DY_1, DX_2, DY_2

    bouton_lancer.destroy()

    while(DX_1 == 0):
        DX_1 = random.randint(-4, 4)

    while(DY_1 == 0):
        DY_1 = random.randint(-4, 4)

    while(DX_2 == 0):
        DX_2 = random.randint(-4, 4)

    while(DY_2 == 0):
        DY_2 = random.randint(-4, 4)

    anime()  # Voir après ``gere_collision``


# La gestion des collisions est incomplète et peu réaliste : penser par exemple
# au cas d'une bille ne bougeant que verticalement, et l'autre ne se déplaçant
# qu'horizontalement. Ceci étant dit, le code suivant montre la voie à suivre.
#
# Nous utilisons une fonction à part pour simplifier le code de ``anime`` mais
# surtout pour pouvoir améliorer notre code facilement dans le futur car toute
# la logique des collisions est gérée par la fonction `gere_collision`.

def gere_collision():
    global rayon
    global x_1, y_1, x_2, y_2
    global DX_1, DY_1, DX_2, DY_2

    dist_2_centres = (x_1 - x_2)**2 + (y_1 - y_2)**2

# Une collision (faire un dessin si besoin) : dans ce cas, on décide de faire
# partir les billes en sens inverse (peu réaliste mais cela reste un bon début).
    if dist_2_centres <= (2*rayon)**2:
        DX_1, DY_1 = -DX_1, -DY_1
        DX_2, DY_2 = -DX_2, -DY_2


def anime():
    global canevas, cercle_1_id, cercle_2_id, rayon

    global x_1, y_1, x_2, y_2
    global x_min, y_min, x_max, y_max
    global DX_1, DY_1, DX_2, DY_2

# Gestion des collisions
    gere_collision()

# Bille 1
    x_1 += DX_1
    y_1 += DY_1

    if x_1 < x_min:
        x_1 = x_min
        DX_1 = -DX_1

    elif x_1 > x_max:
        x_1 = x_max
        DX_1 = -DX_1

    if y_1 < y_min:
        y_1 = y_min
        DY_1 = -DY_1

    elif y_1 > y_max:
        y_1 = y_max
        DY_1 = -DY_1

# Bille 2 (et là on voit qu'utiliser de listes serait bien plus malin)
    x_2 += DX_2
    y_2 += DY_2

    if x_2 < x_min:
        x_2 = x_min
        DX_2 = -DX_2

    elif x_2 > x_max:
        x_2 = x_max
        DX_2 = -DX_2

    if y_2 < y_min:
        y_2 = y_min
        DY_2 = -DY_2

    elif y_2 > y_max:
        y_2 = y_max
        DY_2 = -DY_2

# Mise à jour du dessin
    canevas.coords(
        cercle_1_id,
        x_1 - rayon, y_1 - rayon,
        x_1 + rayon, y_1 + rayon
    )

    canevas.coords(
        cercle_2_id,
        x_2 - rayon, y_2 - rayon,
        x_2 + rayon, y_2 + rayon
    )

# On relance la fonction ce qui va créer une aniation infinie...
    cadre.after(ms = 1, func = anime)


# --------------------------- #
# -- L'INTERFACE GRAPHIQUE -- #
# --------------------------- #

# Fenêtre principale placée au centre de l'écran
racine = tkinter.Tk()
racine.title('La quantique des deux particules')

# Prenons une fenêtre pas trop grande pour favoriser les collisions.
larg_fen = haut_fen = 350

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

racine.resizable(
    width  = False,
    height = False
)

# Cadre
cadre = tkinter.Frame(master = racine)
cadre.grid(row = 0, column = 0)

# Ajout du canevas où les dessins seront faits.
larg_canevas = larg_fen - 6
haut_canevas = haut_fen - 100

canevas = tkinter.Canvas(
    master     = cadre,
    width      = larg_canevas,
    height     = haut_canevas,
    background = 'grey'
)
canevas.grid(row = 0, column = 0, sticky = "ew")

# Ajout d'un bouton pour lancer l'animation.
bouton_lancer = tkinter.Button(
    master  = cadre,
    text    = "Commencer",
    command = debute_animation
)
bouton_lancer.grid(row = 1, column = 0, sticky = "ew")

# Les deux billes.
couleur_1 = "red"
couleur_2 = "blue"

rayon = 10

x_min, x_max = rayon + 1, larg_canevas - rayon
y_min, y_max = rayon + 1, haut_canevas - rayon

x_1 = random.randint(x_min, x_max)
y_1 = random.randint(y_min, y_max)

# On veut deux billes sufisamment éloignées l'une de l'autre initialement (notre
# choix n'est pas le seul possible).
x_2, y_2 = x_1, y_1

while(
    abs(x_2 - x_1) <= 2*rayon
    and
    abs(y_2 - y_1) <= 2*rayon
):
    x_2 = random.randint(x_min, x_max)
    y_2 = random.randint(y_min, y_max)


cercle_1_id = canevas.create_oval(
    x_1 - rayon, y_1 - rayon,
    x_1 + rayon, y_1 + rayon,
    fill = couleur_1
)

cercle_2_id = canevas.create_oval(
    x_2 - rayon, y_2 - rayon,
    x_2 + rayon, y_2 + rayon,
    fill = couleur_2
)


# -------------------------------- #
# -- LANCEMENT DE L'APPLICATION -- #
# -------------------------------- #

racine.mainloop()
