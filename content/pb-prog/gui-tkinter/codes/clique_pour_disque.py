# ------------------ #
# -- IMPORTATIONS -- #
# ------------------ #

import tkinter


# ---------------------------------------------- #
# -- ACTIONS FAITES PAR L'INTERFACE GRAPHIQUE -- #
# ---------------------------------------------- #

RAYON = 10

def clic_gauche(evenement):
    global canevas, RAYON

    x_centre = evenement.x
    y_centre = evenement.y

    canevas.create_oval(
        x_centre - RAYON, y_centre - RAYON,
        x_centre + RAYON, y_centre + RAYON,
        width   = 5,
        fill    = '#980e0e',
        outline = 'blue'
    )


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

# Associer le clic gauche à une fonction.
canevas.bind(
    sequence = '<Button-1>',
    func     = clic_gauche
)


# -------------------------------- #
# -- LANCEMENT DE L'APPLICATION -- #
# -------------------------------- #

racine.mainloop()
