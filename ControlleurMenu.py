import tkinter as tk
class ControleurMenu(tk.Frame):
    '''
    Cette classe permet de modifier les parametres du jeu (tel que la vitesse des ovnis, le nombre d'ovnis qui apparaissent par secondes, etc.) selon
    la difficulté choisi par l'utilisateur, dans la methode afficherChoixLevel() de la classe Choix.
    '''
    def __init__(self):
        self.timerCreateOvnis = 3 #cree des ovnis toutes les 3s
        self.timerMoveOvnis = 0.03#si jaugmente a 0.1, il y a plus dOvnis qui apparaissent et leur descente est saccade
        self.vitesseOvniY = 0
        self.vitesseOvniX = 0

        #partie asteroide
        self.timerCreateAsteroide = 5# creation des aste toute les 5s
        self.timerMoveAsteroide = 0.03

        #partie missile
        self.timerMoveMissile = 0.03 #toutes les 0.03s fait bouger le missile

    

