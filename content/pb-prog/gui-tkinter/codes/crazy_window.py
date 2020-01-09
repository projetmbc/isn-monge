# ------------------ #
# -- Importations -- #
# ------------------ #

import random
import tkinter


# ------------------------------------------------ #
# -- Actions faites par l'application graphique -- #
# ------------------------------------------------ #

def bouton_clique():
    global racine, larg_fen, haut_fen

    xpos_fen = random.randint(100, 400)
    ypos_fen = random.randint(100, 400)

    racine.geometry(
        "{0}x{1}+{2}+{3}".format(
            larg_fen, haut_fen,
            xpos_fen, ypos_fen
        )
    )


# --------------------------- #
# -- L'interface graphique -- #
# --------------------------- #

# Construction de la fenêtre principale
racine = tkinter.Tk()
racine.title("Au hasard...")

larg_fen = 350
haut_fen = 150

xpos_fen = ypos_fen = 300

racine.geometry(
    "{0}x{1}+{2}+{3}".format(
        larg_fen, haut_fen,
        xpos_fen, ypos_fen
    )
)

# Ajout d'un cadre.
cadre = tkinter.Frame(racine)
cadre.grid(row = 0, column = 0)

# Ajout du bouton.
bouton = tkinter.Button(
    cadre,
    text    = "Cliquer ici",
    command = bouton_clique
)

bouton.grid(row = 0, column = 0)


# -------------------------------- #
# -- LANCEMENT DE L'APPLICATION -- #
# -------------------------------- #

racine.mainloop()
