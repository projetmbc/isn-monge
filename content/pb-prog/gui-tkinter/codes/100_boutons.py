# ------------------ #
# -- Importations -- #
# ------------------ #

import tkinter


# ---------------------------------------------- #
# -- ACTIONS FAITES PAR L'INTERFACE GRAPHIQUE -- #
# ---------------------------------------------- #

def bouton_clique(no):
    print("Bouton {0} cliqué.".format(no))


# --------------------------- #
# -- L'INTERFACE GRAPHIQUE -- #
# --------------------------- #

# Construction de la fenêtre principale
racine = tkinter.Tk()
racine.title('Quel bouton ?')

# Le cadre.
cadre = tkinter.Frame(master = racine)
cadre.grid(row = 0, column = 0)

# Remplissage du cadre avec les boutons.
for i in range(100):
    bouton = tkinter.Button(
        master  = cadre,
        text    = "Bouton {0}".format(i + 1),
        command = lambda x = i + 1: bouton_clique(x)
    )

    bouton.grid(row = i//10, column = i%10)


# -------------------------------- #
# -- LANCEMENT DE L'APPLICATION -- #
# -------------------------------- #

racine.mainloop()
