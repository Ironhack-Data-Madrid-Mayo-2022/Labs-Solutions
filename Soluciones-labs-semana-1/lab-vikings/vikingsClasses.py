
#Import libraries


import random



######################################################################################################

# Soldier


class Soldier:
    def __init__(self, health, strength): #receive **2 arguments** (1st health & 2nd strength), self doesn't "count"
        self.health = health
        self.strength = strength
    def attack(self):       # receive **0 arguments** (self doesn't count)
        return self.strength #return strength` property

    def receiveDamage(self, damage): #receive **1 argument** (the damage)(self doesn't count)
        self.damage = damage
        self.health = self.health - damage #remove the received damage from the `health` property
        return #returns nothing
        

        
######################################################################################################        
        


# Viking


class Viking(Soldier):   #Viking` inherit from `Soldier`
    def __init__(self, name, health, strength):  #receive **3 arguments** (1st name, 2nd health & 3rd strength)
        super().__init__(health, strength) #specifies the inherited properties
        self.name = name

    #def attack(self):
        # This method should be **inherited** from `Soldier`, no need to reimplement it.
        #return self.strength

    def receiveDamage(self, damage): # This method needs to be **reimplemented** for `Viking` because the `Viking` version needs to have different return values.
        
        self.health = self.health - damage


        if self.health > 0:  #if the `Viking` is still alive**, it should return **"NAME has received DAMAGE points of damage
            return f"{self.name} has received {damage} points of damage"

        else:   # **if the `Viking` dies**, it should return **"NAME has died in act of combat"**
            return f"{self.name} has died in act of combat"

    def battleCry(self): # should receive **0 arguments** (remember self doesn't count)
        return "Odin Owns You All!" #return **"Odin Owns You All!"**. Be careful misspelling the battlecry, it will raise an error.
        

        
######################################################################################################        
        

          
# Saxon


class Saxon(Soldier):         #Saxon inherit from `Soldier`
    def __init__(self, health, strength):  # receive **2 arguments** (1st health & 2nd strength)
        super().__init__(health, strength)

    #def attack(self): #This method should be **inherited** from `Soldier`, no need to reimplement it.
        #return self.strength

    def receiveDamage(self, damage): # receive **1 argument** (the damage)
        self.damage = damage
        self.health = self.health - damage

        if self.health > 0: # if the Saxon is still alive**, it should return _**"A Saxon has received DAMAGE points of damage"**
            return f"A Saxon has received {damage} points of damage"

        else: #if the Saxon dies**, it should return _**"A Saxon has died in combat"**_
            return f"A Saxon has died in combat"
        

        
######################################################################################################        
        

    
# War


class War:
    def __init__(self): #receive **0 arguments**
        self.vikingArmy = [] #assign an empty array to the **`vikingArmy` property** (We'll fill it later)      
        self.saxonArmy = [] #assign an empty array to the **`saxonArmy` property**(We'll fill it later)
    
    def addViking(self, viking): #receive **1 argument** (a `Viking` object)
        self.vikingArmy.append(viking)        

    def addSaxon(self, saxon): #same but with saxon army
        self.saxonArmy.append(saxon)        
    
    def vikingAttack(self):
        v = random.choice(self.vikingArmy)  #select random viking 
        s = random.choice(self.saxonArmy) #select random saxon
    
        # v.attack() => With this I  generate a viking attack with the viking previously created
        # s.receiveDamage () => Saxon gets the damage that.
        
        attack_v = s.receiveDamage(v.attack()) #the Saxon receives Damage equal to the `strength` of a `Viking`

        if s.health <= 0: #If saxon is dead
            self.saxonArmy.remove(s) #remove it from the army list
        return attack_v
   
    def saxonAttack(self): #same but for saxon attacks
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)

        attack_s = v.receiveDamage(s.attack())

        if v.health <= 0:
            self.vikingArmy.remove(v)
        return attack_s
    
    def showStatus(self): #receive **0 arguments**
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0: #if the `Saxon` array is empty**
            return "Vikings have won the war of the century!" #return _**"Vikings have won the war of the century!"**_
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0: #**if the `Viking` array is empty**
            return "Saxons have fought for their lives and survive another day..." # return _**"Saxons have fought for their lives and survive another day..."**_
        else: #**if there are at least 1 `Viking` and 1 `Saxon`**
            return "Vikings and Saxons are still in the thick of battle." #return _**"Vikings and Saxons are still in the thick of battle."**_

  