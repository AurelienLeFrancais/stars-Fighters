import tkinter as tk
from functools import partial
from threading import Timer
import random
from ModeleJeu import Ovni, Asteroide, Missile


class Mouvement(tk.Frame):
     '''
    Classe mouvement, qui s'occupe de tout ce qui a un rapport avec un mouvement des objets du jeu (vaisseau, missile, ovnis, asteroides, etc)
    Prend comme parametre un objet tkinter
    '''

     def __init__(self):
        pass


     def moveVaisseau(self, vaisseau, aireDeJeu, e):#meme si vaisseau est en bleu pale, jen ai besoin!!!!!
        """Methode qui permet le mouvement du vaisseau lorsque la souris se deplace"""
            # Récupérer l'image de Vaisseau et reduire sa taille avec la méthode subsample
        self.imageV = tk.PhotoImage(file='Images/Vaisseau.png').subsample(12,12)
            # Créer une instance de Vaisseau et l'afficher dans l'aire de jeu en lui donnant une position x, y
        aireDeJeu.canva.create_image(e.x,e.y, image=self.imageV)#.x et.y pour recup la position de la sourit
        vaisseau.setPositions(e.x,e.y)#!!!!!TRES IMPORTANT!!!! CEST CA QUI PERMET DAVOIR LA POSITION X ET Y DU VAISSEAU!!!!!


     def moveOvnis(self, timerMoveOvnis, vitesseOvniY,vitesseOvniX, listeOvnis, aireDeJeu):
        """Methode qui permet le mouvement des ovnis"""
        vitesseHorizontalDroite = vitesseOvniX
        vitesseHorizontalGauche = -vitesseOvniX
        vitesseOvniY = 2

        for ovn in listeOvnis: # forEach qui passe dans toute la list listAsteroide
                    
                    ovn.y += vitesseOvniY
                    
                    if(ovn.x >= 400):               # Si x >= 400, ca veut dire que l'ovni est a gauche de l'aire de jeu.
                        ovn.direction = "left"      # On s'en sert en bas pour definir si il faut bouger l'ovni a gauche ou a droite

                    elif(ovn.x <= 5):               # Si x >= 400, ca veut dire que l'ovni est a gauche de l'aire de jeu.
                        ovn.direction = "right"     # On s'en sert en bas pour definir si il faut bouger l'ovni a gauche ou a droite

                    if(ovn.direction == "right"):
                        aireDeJeu.canva.move(ovn.instanceOvni,vitesseHorizontalDroite ,vitesseOvniY)#deplacement de l'ovnis en x = 0, y = 2
                        ovn.x += vitesseHorizontalDroite
                    else:
                        aireDeJeu.canva.move(ovn.instanceOvni,vitesseHorizontalGauche ,vitesseOvniY)#deplacement de l'ovnis en x = 0, y = 2
                        ovn.x += vitesseHorizontalGauche

                    
                    # Si y >= 500, veut dire que l'ovni est en dehors de l'aire de jeu, donc on supprime
                    if ovn.y >= 600:
                        aireDeJeu.canva.delete(ovn.instanceOvni)
                        listeOvnis.remove(ovn)
            
        mouvOvniTimer = Timer(timerMoveOvnis, partial(self.moveOvnis, timerMoveOvnis, vitesseOvniY,vitesseOvniX, listeOvnis, aireDeJeu))
        mouvOvniTimer.start()

     def moveAsteroide(self,timerMoveAsteroide, listAsteroide, aireDeJeu):
        """Methode qui permet le mouvement des asteroides"""
        for aste in listAsteroide: # forEach qui passe dans toute la list listAsteroide
                
                #Change la direction
                if aste.direction == "bas-droit":
                    aireDeJeu.canva.move(aste.instanceAsteroide,5 ,5)
                    aste.y += 5
                    aste.x += 5

                elif aste.direction == "bas-gauche":
                    aireDeJeu.canva.move(aste.instanceAsteroide,-5 ,5)
                    aste.y += 5
                    aste.x -= 5

                if aste.y >= 500:
                    aireDeJeu.canva.delete(aste.instanceAsteroide)
                    listAsteroide.remove(aste)
                
        mouvAsteroideTimer = Timer(timerMoveAsteroide, partial(self.moveAsteroide, timerMoveAsteroide, listAsteroide, aireDeJeu))
        mouvAsteroideTimer.start()


     def mouvMissiles(self, aireDeJeu, listeMissiles, timerMoveMissile):
        """Methode qui permet le mouvement des missiles"""

            #Boucle for each qui va passer dans la liste des missiles qui existent deja
        for missile in listeMissiles:
                aireDeJeu.canva.move(missile.instanceMissile, 0, -10)
                missile.y -=10

                #Si le missile depasse la partie en haut de l'aire de jeu (y <= 0), supprimer le missile, pour eviter de se retrouver avec plein de missiles.
                if missile.y <= 0:
                    aireDeJeu.canva.delete(missile.instanceMissile)
                    listeMissiles.remove(missile)
            
            #Timer threads
        mouvMissileTimer = Timer(timerMoveMissile,partial(self.mouvMissiles,aireDeJeu, listeMissiles, timerMoveMissile))
        mouvMissileTimer.start()


class Spawns(tk.Frame):#Spawns -> reproduire
    '''
    Cette classe s'occupe de la generation des objets dans l'aire de jeu (Generation des ovnis, des asteroides ainsi que des bonus (Power Up))
    '''

    def __init__(self):
        self.listeOvnis = []
        self.listAsteroides = []
        

    def createOvnis(self, timerCreateOvnis, aireDeJeu):
        '''methode pour creer des ovnis avec une postion x aleatoire'''
        
        if random.randint(0,1) == 0:
            # on fait partir l'ovnis a gauche
            x = random.randint(25,200)
            self.listeOvnis.append(Ovni(aireDeJeu,x,-40))
           
        else:
            #on fait partir l'ovnis à droite
            x = random.randint(250,425)
            self.listeOvnis.append(Ovni(aireDeJeu,x,-40))

       
        createOvniTimer = Timer(timerCreateOvnis, partial(self.createOvnis, timerCreateOvnis, aireDeJeu))#cree un ovnis a chaque 3s
        createOvniTimer.start()


    def createAsteroide(self,timerCreateAsteroide, aireDeJeu):
        """Methode qui creer un asteroide et l'ajoute a la listAsteroide"""
        if random.randint(0,1) == 0:
            # on fait partir l'asteroide a gauche
            x = random.randint(25,200)
            self.listAsteroides.append(Asteroide(aireDeJeu,x,-40,"bas-droit"))

        else:
            #on fait partir l'asteroide à droite
            x = random.randint(250,425)
            self.listAsteroides.append(Asteroide(aireDeJeu,x,-40,"bas-gauche"))

        
        createAstroideTimer = Timer(timerCreateAsteroide, partial(self.createAsteroide, timerCreateAsteroide, aireDeJeu))
        createAstroideTimer.start()


class Shoot(tk.Frame):
    '''
    Cette classe s'occupe de tout ce qui a un rapport avec l'action de tirer 
    (Le vaisseau tire un missile/laser(ET cooldown laser), les ovnis tirent une mine, etc)JE NE FERAI PAS LES LASERS
    '''

    def __init__(self):
        pass

        self.listeMissiles = []

    """Methode qui creer un missile et l'ajoute a la listeMissiles"""
    def shootMissile(self, aireDeJeu, vaisseau, event):
        
        #if vaisseau.missileCooldown == False:-> Pour linstant je ne les mets pas et ca tire bien
            #vaisseau.missileCooldown = True
            self.listeMissiles.append(Missile(aireDeJeu, event.x, event.y))
            #aireDeJeu.canva.after(350, partial(vaisseau))-> SI JE MET JUSTE CA CA FONCTIONNE MAIS JAI LERREUR SUIVANTE: the first argument must be callable
            aireDeJeu.canva.after(350, partial(self.resetMissileCooldown, vaisseau))
            

    def resetMissileCooldown(self, vaisseau):#grace a cette fonction, je nai plus lerreur
        vaisseau.missileCooldown = False


class Collision():
    '''
    Cette classe s'occupe des collisions entre les objets
    '''
    def __init__(self):
        pass
    

    def vaisseau_ennemie(self, vaisseau, listeOvnis):#COLLISION VAISSEAU-OVNIS
        '''Collision entre un vaisseau et un ovni'''
        equivalance = 31        # taille du cadre de l'image
         
        VY = vaisseau.y         #position Y milieu du vaisseau
        VX = vaisseau.x         #position X milieu du vaisseau
        VL = vaisseau.x - vaisseau.imageVaisseau.width()/2 + equivalance      #position gauche du vaisseau 
        VR = vaisseau.x + vaisseau.imageVaisseau.width()/2 - equivalance      #position droite du vaisseau
        VT = vaisseau.y - vaisseau.imageVaisseau.height()/2 + equivalance     #position haut du vaisseau
        VB = vaisseau.y + vaisseau.imageVaisseau.height()/2 - equivalance     #position bas du vaisseau
        
        for ovni in listeOvnis: # On passe dans la liste des ovnis
            OL = ovni.x                           #position gauche du pion
            OR = ovni.x + ovni.imageOvni.width()  #position droite du pion
            OT = ovni.y                           #position haut du pion
            OB = ovni.y + ovni.imageOvni.height() #position bas du pion
            

            # la logique des collisions 
            if VT <= OB and VT >= OT or VY <= OB and VY >= OT or VB >= OT and VB <= OB:
                if VR >= OL and VR <= OR or VL <= OR and VL >= OL or VX <= OR and VX >= OL:
                    print("Collision")#si il y a une collision on l'affiche ici
                    listeOvnis.remove(ovni)
                    



    def missiles_ovnis(self, listeMissiles, listeOvnis): 
        '''Collision entre un missile et un ovni'''
        equivalance = 0 # taille du cadre de l'image
        
        for missile in listeMissiles: # On passe a travers la listeMissiles

            MY = missile.y      #position Y milieu du carré rouge 
            MX = missile.x      #position X milieu du carré rouge 
            ML = missile.x - missile.imageMissile.width()/2 + equivalance      #position gauche du carré rouge 
            MR = missile.x + missile.imageMissile.width()/2 - equivalance      #position droite du carré rouge
            MT = missile.y - missile.imageMissile.height()/2 + equivalance     #position haut du carré rouge
            MB = missile.y + missile.imageMissile.height()/2 - equivalance     #position bas du carré rouge

            for ovni in listeOvnis:
            
                OL = ovni.x                           #position gauche du pion
                OR = ovni.x + ovni.imageOvni.width()  #position droite du pion
                OT = ovni.y                           #position haut du pion
                OB = ovni.y + ovni.imageOvni.height() #position bas du pion

                # la logique des collisions avec RB
                if MT <= OB and MT >= OT or MY <= OB and MY >= OT or MB >= OT and MB <= OB:
                    if MR >= OL and MR <= OR or ML <= OR and ML >= OL or MX <= OR and MX >= OL:
                        listeOvnis.remove(ovni)
                        listeMissiles.remove(missile)


    def vaisseau_asteroids(self, vaisseau, listeAsteroids):
        '''Collision entre le vaisseau de l'utilisateur et un asteroide'''
        equivalanceV = 31 # taille du cadre de l'image
        #on recupere la position du vaisseai
        VY = vaisseau.y      #position Y milieu du vaisseau 
        VX = vaisseau.x      #position X milieu du vaisseau 
        VL = vaisseau.x - vaisseau.imageVaisseau.width()/2 + equivalanceV      #position gauche du vaisseau 
        VR = vaisseau.x + vaisseau.imageVaisseau.width()/2 - equivalanceV      #position droite du vaisseau
        VT = vaisseau.y - vaisseau.imageVaisseau.height()/2 + equivalanceV + 10   #position haut du vaisseau
        VB = vaisseau.y + vaisseau.imageVaisseau.height()/2 - equivalanceV 
            #position bas du vaisseau

        for asteroid in listeAsteroids: # On passe a travers de la listeAsteroids

            if asteroid.direction == "bas-droit":
                equivalance = 20 # taille du cadre de l'image 
                AL = asteroid.x + equivalance                           #position gauche asteroide
                AR = asteroid.x + asteroid.imageAsteroide.width()       #position droite asteroide
                AT = asteroid.y + equivalance                           #position haut asteroide
                AB = asteroid.y + asteroid.imageAsteroide.height()      #position bas asteroide
            else:
                AL = asteroid.x                                         #position gauche asteroide
                AR = asteroid.x + asteroid.imageAsteroide.width() - 20  #position droite asteroide
                AT = asteroid.y + 30                                    #position haut asteroide
                AB = asteroid.y + asteroid.imageAsteroide.height()      #position bas asteroide

            # la logique des collisions
            if VT <= AB and VT >= AT or VY <= AB and VY >= AT or VB >= AT and VB <= AB:
                if VR >= AL and VR <= AR or VL <= AR and VL >= AL or VX <= AR and VX >= AL:
                    print("vaisseau touche")
                    listeAsteroids.remove(asteroid)
                    
                        
                        

    def verifierCollision(self,vaisseau, listeOvnis, listeMissiles, listeAsteroids):
        '''
        Fonction qui verifie constamment toutes les collisions chaque 0.03. Appel de toutes les fonctions collisions
        '''
        self.vaisseau_ennemie(vaisseau,listeOvnis)
        self.missiles_ovnis(listeMissiles,listeOvnis)
        self.vaisseau_asteroids(vaisseau,listeAsteroids)
        verifierCollisionTimer = Timer(0.03,partial(self.verifierCollision,vaisseau,listeOvnis,listeMissiles,listeAsteroids)) 
        verifierCollisionTimer.start()







    

    
    

    
    
            
