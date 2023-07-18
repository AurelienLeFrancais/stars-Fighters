import tkinter as tk

class AireDeJeu:
    """
    Class AireDeJeu initialise l'aire jouable dans l'application.
    Prend le container comme parametre.
    """
    def __init__(self, container):
        self.height = 500
        self.width = 450 
        self.imageBackground = tk.PhotoImage(file='Images/Background.png').subsample(2,2) #Image de fond -> le subsample definit la taille de limage de fond. Attention, plus on laugmente, plus la taille est petite
        
        self.canva = tk.Canvas(container, height=self.height, width=self.width)
        self.canva.create_image(10,10, image=self.imageBackground)
        self.canva.grid(column=1, row=1, padx=20) # pour centrer et donner un padding
        self.canva.config(cursor="none")

class Vaisseau:
    """
    Class Vaiseau permet l'initialisation de l'objet vaisseau, controlable par l'utilisateur
    Parameters: Container, pour pouvoir placer le vaisseau dans l'air de jeu.
    """
    def __init__(self, container):#dans le container
        self.imageVaisseau = tk.PhotoImage(file='Images/Vaisseau.png').subsample(6,6) #creer un vaisseau
        self.x = 0
        self.y = 0

    def setPositions(self,x,y):
        self.x = x
        self.y = y
        

class Ovni:
    '''
    Cette classe s'occupe d'initialiser un objet ovni. Il comprend les cordonees ainsi que l'image de l'ovni.
    '''
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageOvni = tk.PhotoImage(file='Images/ovni.png').subsample(4,4) #Creation de l'image Ovni .subsample -> plus cest petit plus cest gros
        self.instanceOvni = container.canva.create_image(self.x,self.y,anchor=tk.NW,image=self.imageOvni)
        self.direction = "right"

class Asteroide:
    """
    Cette classe permet l'initialisation d'un asteroide dans l'air de jeu,
    Parameters: Les cordonnes (X, Y) ainsi que la direction de l'asteroide.
    """
    def __init__(self,container, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        if self.direction == "bas-droit":
            self.imageAsteroide = tk.PhotoImage(file='Images/asteroide.gif').subsample(4,4)                             #Creation de l'image Asteroide
        else:
            self.imageAsteroide = tk.PhotoImage(file='Images/asteroideFlipped.png').subsample(4,4)                      #Creation de l'image Asteroide
        self.instanceAsteroide = container.canva.create_image(self.x, self.y, anchor=tk.NW,image=self.imageAsteroide)   #Placer l'image dans le container
        

class Missile:
    """
    Class Missile permet d'initialiser un objet missile, prend les coordonnes ainsi que le container tkinter comme paramatre.
    """
    def __init__(self,container, x, y):
        self.x = x
        self.y = y
        self.imageMissile = tk.PhotoImage(file='Images/missile.png').subsample(3,3)#plus on grossi, plus cest petit
        self.instanceMissile = container.canva.create_image(self.x, self.y, image=self.imageMissile) #placer limage dans le container      

    