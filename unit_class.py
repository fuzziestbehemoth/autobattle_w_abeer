# Created by: Abeer and Ander
# Date: 8/14/19
# Objective: Hold data on units

def class Unit(career):
    # the class determines which text file to read from for starting characteristics and attacks
    self.career = career
    # Determines units target selection preferences
    self.type = ''
    
    # When this reaches zero, unit dies
    self.health = 0
    
    # Added to action point and mana point total (respectively) at the start of each round
    self.speed = 0
    self.mregen = 0
    
    # Defensive characteristics, higher numbers reduce damage from an attack
    self.armor = 0
    self.mresist = 0
    
    # Offensive characteristics, higher numbers increase the damage when delivering an attack
    self.attack = 0
    self.mattack = 0
    
    # Used for charting units advancement progress
    self.exp = 0
    self.level = 0
    
    self.attacks = []
    
    