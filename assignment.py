#! python3
import random

print("Rock // Paper // Scissor")

class game:
  randomchoice = None
  playerchoice = None

  def __init__(self):
    while True:
      self.playerchoice = input("Choice: ").capitalize()
      randomlist = ['Rock', 'Paper', 'Scissors']
      self.randomchoice = random.choice(randomlist).capitalize()
      
      print(f"Player Choice: {self.playerchoice}\nNPC Choice: {self.randomchoice}")
      self.PlayervRando()
    return None

  def gamble(self):
    randomchoice = self.randomchoice
    playerchoice = self.playerchoice
    return 
    

  
  def PlayervRando(self):
    
      randomlist = ['Rock', 'Paper', 'Scissors']
      if self.playerchoice not in randomlist:
        print("invalid resonse")
      else:
        if self.playerchoice == 'Rock' and self.randomchoice == 'Scissors':
          print("you win\n")
        elif self.playerchoice == 'Scissors' and self.randomchoice == 'Rock':
          print("you lose\n")
        elif self.playerchoice == 'Paper' and self.randomchoice == 'Rock':
          print("you win\n")
        elif self.playerchoice == 'Rock' and self.randomchoice == 'Paper':
          print("you lose\n")
        elif self.playerchoice == 'Scissors' and self.randomchoice == 'Paper':
          print("you win\n")
        elif self.playerchoice == 'Paper' and self.randomchoice == 'Scissors':
          print("you lose\n")
        elif self.playerchoice == 'Rock' and self.randomchoice == 'Rock':
          print("tie\n")
        elif self.playerchoice == 'Paper' and self.randomchoice == 'Paper':
          print("tie\n")
        elif self.playerchoice == 'Scissors' and self.randomchoice == 'Scissors':
          print("tie\n")
      
      
      pass

  

# This is the only command allowed that is not in the class template. All code must be done there.
g = game()


