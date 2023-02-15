class Pokemon:

  def __init__(self, name, type, level = 5):
    self.name = name
    self.type = type
    self.level = level
    self.health = level * 5
    self.is_dead = False


  def __repr__(self):

    return "This pokemon called {name} is {level}, has {health} hit points and is {type} pokemon.".format(name = self.name, level = self.level, health = self.health, type = self.type)

  def death(self):
    self.is_dead = True

    if self.health != 0:
      self.health = 0
      print("{} has sadly died in battle. ").format(self.name)
      

  def revive(self):
    self.is_dead = False

    if self.health == 0:
      self.health = 1
      print("Your pokemon has been revived and has now {} hit points").format(self.health)
  
  def gain_health(self, amount):
    self.amount = amount
    if self.health == 0:
      self.revive()

      self.health += amount
      print("{name} gained {amount} health!").format(name = self.name, amount = self.amount)

  def lose_health(self, amount):
    self.health -= amount
    if self.health == 0:
      print("{} has died and we have to revive him").format(self.name)
      self.revive()

  def attack(self, other_pokemon):
        
        if self.is_dead:
            print("{name} can't attack because it is knocked out!".format(name = self.name))
            return
        
        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = round(self.level * 0.5)))
            print("It's not very effective")
            other_pokemon.lose_health(round(self.level * 0.5))
        
        if (self.type == other_pokemon.type):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level))
            other_pokemon.lose_health(self.level)
        
        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = other_pokemon.name, damage = self.level * 2))
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)


class Trainer:

  def __init__(self, name, pokemons)
    self.name = name
    self.pokemons = pokemons    

     
