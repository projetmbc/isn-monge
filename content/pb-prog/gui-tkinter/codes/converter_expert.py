# Source pour travailler directement avec des ``tkinter.StringVar()`` :
#     * http://effbot.org/tkinterbook/variable.htm


# ------------------ #
# -- Importations -- #
# ------------------ #

import tkinter


# ---------------------------------------------- #
# -- ACTIONS FAITES PAR L'INTERFACE GRAPHIQUE -- #
# ---------------------------------------------- #

def dec_vers_hex_bin(entier):
    val_bin = bin(entier)
    val_hex = hex(entier)

    val_bin = val_bin[2:]
    val_hex = val_hex[2:]

    return val_hex, val_bin


# La variable suivante permet d'éviter des changements non souhaités.
chgt_en_cours = False

def dec_change(*args):
    global chgt_en_cours
    global valeur_dec, valeur_hex, valeur_bin

    if not chgt_en_cours:
        chgt_en_cours = True

        nelle_val_dec = int(valeur_dec.get())

        nelle_val_hex, nelle_val_bin = dec_vers_hex_bin(nelle_val_dec)

        valeur_bin.set(nelle_val_bin)
        valeur_hex.set(nelle_val_hex)

        chgt_en_cours = False


def binaire_change(*args):
    global chgt_en_cours
    global valeur_dec, valeur_hex, valeur_bin

    if not chgt_en_cours:
        chgt_en_cours = True

        nelle_val_dec = int(valeur_bin.get(), 2)

        nelle_val_hex, nelle_val_bin = dec_vers_hex_bin(nelle_val_dec)

        valeur_dec.set(nelle_val_dec)
        valeur_hex.set(nelle_val_hex)

        chgt_en_cours = False


def hex_change(*args):
    global chgt_en_cours
    global valeur_dec, valeur_hex, valeur_bin

    if not chgt_en_cours:
        chgt_en_cours = True

        nelle_val_dec = int(valeur_hex.get(), 16)

        nelle_val_hex, nelle_val_bin = dec_vers_hex_bin(nelle_val_dec)

        valeur_dec.set(nelle_val_dec)
        valeur_bin.set(nelle_val_bin)

        chgt_en_cours = False


def touche_activee(i):
    global saisie_dec

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


valeur_dec = tkinter.StringVar()
valeur_dec.trace(mode = "w", callback = dec_change)

saisie_dec = tkinter.Entry(cadre_affichage, textvariable = valeur_dec)
saisie_dec.grid(row = 0, column = 1)
saisie_dec.focus_set()


valeur_hex = tkinter.StringVar()
valeur_hex.trace(mode = "w", callback = hex_change)

saisie_hex = tkinter.Entry(cadre_affichage, textvariable = valeur_hex)
saisie_hex.grid(row = 1, column = 1, sticky = tkinter.W)


valeur_bin = tkinter.StringVar()
valeur_bin.trace(mode = "w", callback = binaire_change)

saisie_bin = tkinter.Entry(cadre_affichage, textvariable = valeur_bin)
saisie_bin.grid(row = 2, column = 1, sticky = tkinter.W)

# Remplissage du cadre pour les boutons.

for pos, etiquette in enumerate("0123456789"):
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
