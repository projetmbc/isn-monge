# ------------------ #
# -- IMPORTATIONS -- #
# ------------------ #

import tkinter


# ---------------------------------------------- #
# -- ACTIONS FAITES PAR L'INTERFACE GRAPHIQUE -- #
# ---------------------------------------------- #

# Ci-dessous, on pourrait utiliser plus de constantes globales pour ne pas
# refaire inutilement les calculs de ``x_max``, ``y_max``, ``x_min``, ``y_min``.
#
# À vous de le faire si le coeur vous en dit !

def deplace_disque(evenement):
    global rayon, x_centre, y_centre
    global canevas, disque_id

# On ne bouge le disque que si la souris est suffisamment prête du disque.
    dist_2_souris_centre \
    = (x_centre - evenement.x)**2 + (y_centre - evenement.y)**2

# La valeur 7 a été choisie pour une fois en faisant appel à la fameuse loi
# scientificopifométrique XZ24.
    delta_rayon_2 = (rayon + 7)**2

# On bouge de 7 pixels à l'opposé la souris si c'est possible (on ne s'autorise
# pas à sortir du canevas).
    if dist_2_souris_centre < delta_rayon_2:
        delta = 7

        delta_securite = max(delta, rayon)

        x_max = larg_canevas - delta_securite
        x_min = delta_securite + 1

        y_max = haut_canevas - delta_securite
        y_min = delta_securite + 1

        if x_centre >= evenement.x:
            x_centre = min(x_max, x_centre + delta)

        else:
            x_centre = max(x_min, x_centre - delta)

        if y_centre >= evenement.y:
            y_centre = min(y_max, y_centre + delta)

        else:
            y_centre = max(y_min, y_centre - delta)

        canevas.coords(
            disque_id,
            x_centre - rayon, y_centre - rayon,
            x_centre + rayon, y_centre + rayon
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

# Ajout du cercle initial au centre
rayon = 10

x_centre = larg_canevas // 2
y_centre = haut_canevas // 2

disque_id = canevas.create_oval(
    x_centre - rayon, y_centre - rayon,
    x_centre + rayon, y_centre + rayon,
    fill = '#ffff99'
)


# Agir quand la souris passe au-dessus du canevas.
canevas.bind(
    sequence = '<Motion>',
    func     = deplace_disque
)


# -------------------------------- #
# -- LANCEMENT DE L'APPLICATION -- #
# -------------------------------- #

racine.mainloop()
