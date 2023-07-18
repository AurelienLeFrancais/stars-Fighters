#LOGIQUE COLLISION: ASTEROIDE QUI TOUCHE VAISSEAU
import tkinter as tk
from ModeleJeu import AireDeJeu, Vaisseau
from ControleurJeu import Mouvement, Spawns, Shoot, Collision
from ControlleurMenu import ControleurMenu
from functools import partial
from threading import Timer

if __name__ == "__main__":

    menu = ControleurMenu()
   

    def commencerJeu():
        couleurTheme = "#41157A"
            
        #creation fenetre root
        root = tk.Tk()
        root.title("Star Fighter")
        root.config(background= couleurTheme)
        root.geometry("510x680")

        # créer un containter et le centrer dans la fenetre tk
        mainContainer = tk.Frame(root, background= couleurTheme)
        mainContainer.pack() # pour centrer et donner un padding


        # créer un titre de jeu et le mettre dans un grid en lui donnant du padding
        titre = tk.Label(mainContainer, text="StarFighter", fg='#FFFC33', background= couleurTheme)
        titre.configure(font=("MV Boli", 25, "bold"))
        titre.grid(column=1, row=0, padx=10, pady=10)

        # créer l'aire de jeu et le mettre dans un grid en lui donnant du padding
        aireDeJeu = AireDeJeu(mainContainer)
        vaisseau = Vaisseau(aireDeJeu)
        mvmt = Mouvement()
        spawns = Spawns()
        shoot = Shoot()
        collision = Collision()

        #----------------------MISE EN PLACE BOUTONS------------------------------------------------------------------
        # créer un container des buttonset le mettre dans un grid en lui donnant du padding
        buttonsContainer = tk.Canvas(mainContainer, background= couleurTheme, highlightthickness=0)
        buttonsContainer.grid(column=1, row=4, padx=10, pady=20) # pour centrer et donner un padding
        couleurButtons = "#E22866"
        buttonEnregistrer = tk.Button(buttonsContainer, text="    Enregistrer    ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))#, command=partial(enregistrer.askUsername, player,jeu))
        buttonEnregistrer.grid(column=1, row=1, padx=15)

        # créer un button qui affiche le menu score un nouveau jeu et le mettre dans un grid en lui donnant du padding
        buttonMenuScores = tk.Button(buttonsContainer, text="    Scores    ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))#, command=partial(enregistrer.AfficherScores))
        buttonMenuScores.grid(column=2, row=1, padx=15)

        # créer un button quitte du programme et le mettre dans un grid en lui donnant du padding
        buttonQuitter = tk.Button(buttonsContainer, text="    Quitter    ", background= couleurButtons, fg='#FFFED6', font=('arial', 9, 'bold'))#, command=root.destroy)
        buttonQuitter.grid(column=3, row=1, padx=15)

        #------------------------------------------------------------------------------------------------------------
         # Le vaisseau se deplace en suivant la position de la souris
        aireDeJeu.canva.bind('<Motion>', partial(mvmt.moveVaisseau, vaisseau, aireDeJeu))

         # # Un missile est tiré lorsqu'on fait un click gauche de la souris
        aireDeJeu.canva.bind('<Button-1>', partial(shoot.shootMissile, aireDeJeu, vaisseau))

         # On bouge le missile vers le haut
        mvmt.mouvMissiles(aireDeJeu, shoot.listeMissiles, menu.timerMoveMissile)

         # creation ovnis
        spawns.createOvnis(menu.timerCreateOvnis, aireDeJeu)

         # creation astroides
        spawns.createAsteroide(menu.timerCreateAsteroide, aireDeJeu)

         # mouvement des ovnis
        mvmt.moveOvnis(menu.timerMoveOvnis, menu.vitesseOvniY, menu.vitesseOvniX, spawns.listeOvnis, aireDeJeu)
         # mouvement des astroides
        mvmt.moveAsteroide(menu.timerMoveAsteroide, spawns.listAsteroides, aireDeJeu)

        collision.verifierCollision(vaisseau, spawns.listeOvnis, shoot.listeMissiles, spawns.listAsteroides)

        root.mainloop()

    
    commencerJeu()