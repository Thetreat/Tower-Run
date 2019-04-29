# import tkinter as tk
from model.Character import Character
import model.Heros as He

class Ennemy (Character):
 
    def __init__ (self, parent, x, y, heros, **kwargs) :
        #Initialisation en tant que Character
        Character.__init__(self,parent,x,y)
        self.heros = heros

        # Insertion dans le tableau
        # Tableau contenant tous les ennemis existants
        parent.ennemies.insert(0,self)

        #Le Monstre se dirige toujours vers l'objectif dès son apparition
        self.path = kwargs.get("path", None)
        if self.path == None:
            self.path = self.parent.defaultPath
        self.goToObjective()

    # Fonction chargée de faire déplacer le monstre
    def goToObjective(self):
        if self.move == None:
            if self.pathIndex != len(self.path) :
                self.moveTo(self.path[self.pathIndex].x,self.path[self.pathIndex].y)
            else : 
                self.loseLife()
                
#---------------------------- Différents ennmis présents dans le jeu --------------

class Skeleton (Ennemy) :
    __slots__ = ("idle", "runRight", "runLeft", "attackRight", "attackLeft", "death")
    hp = 10
    name = "Skeleton"
    attackSpeed = 1
    speed = 20
    damage = 2
    purse = 10

    barOffsetx = -20

    spriteSize = 32
    y_Anim = {"idleRight" : 32,"idleLeft":0, "runRight" : 32, "runLeft" : 0, "attackRight": 32, "attackLeft": 0, "die" : 64}
    damagingSprite = [4,6,7,8]
    num_sprintes = {"idleRight": 1, "idleLeft" : 1, "runRight" : 4, "runLeft" : 4, "attackRight" : 8, "attackLeft": 8, "die": 4}
    spritesheet = "view/src/personnage/ennemis/Skeleton.png"
    zoom = 2

class miniSkeleton (Skeleton) :
    hp = 5
    attackSpeed = 2
    speed = 2
    damage = 1
    zoom = 1

class Totor (Ennemy):
    __slots__ = ("idle", "runRight",
                "runLeft", "attackRight", "attackLeft")

    hp = 200
    name = "Totor"
    attackSpeed = 0.5
    speed = 1
    damage = 10
    
    spritesheet = 'view/src/Totor.png'
    spriteSize = 96
    y_Anim = {"idle" : 0, "runRight" : 96, "runLeft" : 96*12, "attackRight": 96*3, "attackLeft": 96*13, "die" : 96*10}
    damagingSprite = [1,2,3]
    num_sprintes = {"idle" : 5, "runRight" : 8, "runLeft" : 8, "attackRight" : 9, "attackLeft": 9, "die": 6}
    zoom = 2

class Fat_Totor (Totor) :
    hp = 1000
    name = "Fat_Totor"
    damage = 20
    speed = 0.5
    zoom = 3

class Dwarf (Ennemy) :
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft')

    hp = 50
    name = 'Dwarf'
    attackSpeed = 1
    speed = 1
    damage = 5

    spritesheet = 'view/src/Dwarf.png'
    spriteSize = 96 
    num_sprintes = {'idle' : 5, 'runRight' : 8, 'runLeft' : 8, 'attackRight' : 9, 'attackLeft' : 9, 'die' : 6}
    zoom = 1
    