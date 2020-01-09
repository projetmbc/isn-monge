# ------------------ #
# -- Importations -- #
# ------------------ #

import tkinter


# ---------------------------------------------- #
# -- ACTIONS FAITES PAR L'INTERFACE GRAPHIQUE -- #
# ---------------------------------------------- #

def touche_activee(i):
    global saisie_dec, etiquette_bin, etiquette_hex

    if i == 10:
        nelle_val_dec = int(saisie_dec.get())

        nelle_val_bin = bin(nelle_val_dec)
        nelle_val_hex = hex(nelle_val_dec)

# On doit retirer les "0b" et "0x" propres à Python.
        nelle_val_bin = nelle_val_bin[2:]
        nelle_val_hex = nelle_val_hex[2:]

# Mise à jour des affichages.
        etiquette_bin.config(text = nelle_val_bin)
        etiquette_hex.config(text = nelle_val_hex)

    else:
        saisie_dec.insert(tkinter.INSERT, i)


# --------------------------- #
# -- L'interface graphique -- #
# --------------------------- #

# Construction de la fenêtre principale
racine = tkinter.Tk()
racine.title('Conversions basiques')

# Voici comment centre une fenêtre (un petit bonus gratuit).
larg_ecran = racine.winfo_screenwidth()
haut_ecran = racine.winfo_screenheight()

# Utilisation de la loi pifométrique n°24713.
larg_fen = 400
haut_fen = 100

xpos_fen = larg_ecran // 2 - larg_fen // 2
ypos_fen = haut_ecran // 2 - haut_fen // 2

racine.geometry(
    "{0}x{1}+{2}+{3}".format(
        larg_fen, haut_fen,
        xpos_fen, ypos_fen
    )
)

# Les cadres.
cadre_affichage = tkinter.Frame(racine)
cadre_affichage.grid(row = 0, column = 0)

cadre_boutons = tkinter.Frame(racine)
cadre_boutons.grid(row = 0, column = 1)

# Remplissage du cadre pour l'affichage.
etiquette_dec = tkinter.Label(cadre_affichage, text = "Valeur décimale :")
etiquette_dec.grid(row = 0, column = 0, sticky = tkinter.E)

etiquette_hex = tkinter.Label(cadre_affichage, text = "Valeur hexadécimale :")
etiquette_hex.grid(row = 1, column = 0, sticky = tkinter.E)

etiquette_bin = tkinter.Label(cadre_affichage, text = "Valeur binaire :")
etiquette_bin.grid(row = 2, column = 0, sticky = tkinter.E)


valeur_decimale = tkinter.StringVar()

saisie_dec = tkinter.Entry(cadre_affichage, textvariable = valeur_decimale)
saisie_dec.grid(row = 0, column = 1)
saisie_dec.focus_set()

etiquette_hex = tkinter.Label(cadre_affichage)
etiquette_hex.grid(row = 1, column = 1, sticky = tkinter.W)

etiquette_bin = tkinter.Label(cadre_affichage)
etiquette_bin.grid(row = 2, column = 1, sticky = tkinter.W)

# Remplissage du cadre pour les boutons.

for pos, etiquette in enumerate("0123456789="):
    bouton = tkinter.Button(
        cadre_boutons,
        text    = etiquette,
        command = lambda i = pos: touche_activee(i)
    )

    bouton.grid(row = pos // 3, column = pos % 3)


# -------------------------------- #
# -- LANCEMENT DE L'APPLICATION -- #
# -------------------------------- #

racine.mainloop()
