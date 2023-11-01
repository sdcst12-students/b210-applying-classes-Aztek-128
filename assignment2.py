#! python3
import random
print("Craps")
class game:
    def __init__(self):
        self.playerbet = int(input("What is your bet\nPass Line Bet:    1\nDon't Pass Bet:   2\nCome Bet:         3\nDon't Come Bet:   4\nOdds Bet:         5\nPlace Bet:        6\nProposition Bet:  7\nFields bet        8\nNo Bet:           9\nWhat is your bet: "))
        #betlist = {'Pass Line Bet': 1,'Dont Pass Bet': 2,'Come Bet': 3,'Dont Come Bet': 4,'Field': 5,'Place Bet': 6,'Proposition Bet': 7}
        self.money = int(input("how much do you want to bet: $"))
        if self.playerbet == 1:
            self.passline()
        elif self.playerbet == 2:
            self.dontpass()
        elif self.playerbet== 3:
            self.comebet()
        elif self.playerbet == 4:
            self.dontcome()
        elif self.playerbet == 5:
            self.odds()
        elif self.playerbet == 6:
            self.Place()
        elif self.playerbet == 7:
            self.Proposition()
        elif self.playerbet == 8:
            self.Field()
        elif self.playerbet == 9:
            self.Nobet()

    def passline(self):
        dicenum = random.randint(2,12)
        print(dicenum)
        turns = 0
        if dicenum in [7,11]:
            print(f"you won {self.money * 2 }")
        elif dicenum in [2, 3, 12]:
            print("you lose")
        else:
            print(f"your point is {dicenum}") 
            turns+=1
            if turns >= 1:
                while True:
                    dicenum2 = random.randint(2,12)
                    print(dicenum2)
                    if dicenum2 == dicenum:
                        print(f"you won {self.money * 2 }")
                        break
                    elif dicenum2 == 7:
                        print("you lose")
                        break
    def dontpass(self):
        dicenum = random.randint(2,12)
        print(dicenum)
        turns = 0
        if dicenum in [2,3,12]:
            print(f"you won {self.money * 2 }")
        elif dicenum in [7,11]:
            print("you lose")
        else:
            print(f"your point is {dicenum}") 
            turns+=1
            if turns >= 1:
                while True:
                    dicenum2 = random.randint(2,12)
                    print(dicenum2)
                    
                    if dicenum2 == dicenum:
                        print("you lose")
                        
                        break
                    elif dicenum2 == 7:
                        print(f"you won {self.money * 2 }")
                        break
    def comebet(self): 
        dicenum = random.randint(2,12)
        print(dicenum)
        turns = 0
        if dicenum in [7,11]:
            print(f"you won ${self.money * 2 }")
        elif dicenum in [2, 3, 12]:
            print("you lose")
        else:
            print(f"your point is {dicenum}") 
            turns+=1
            if turns >= 1:
                while True:
                    dicenum2 = random.randint(2,12)
                    print(dicenum2)
                    if dicenum2 == dicenum:
                        print(f"you won ${self.money * 2 }")
                        break
                    elif dicenum2 == 7:
                        print(dicenum2)
                        print("you lose")
                        break
    def dontcome(self):
            dicenum = random.randint(2,12)
            print(dicenum)
            turns = 0
            if dicenum in [2,3,12]:
                print(f"you won ${self.money * 2 }")
            elif dicenum in [7,11]:
                print("you lose")
            else:
                print(f"your point is {dicenum}") 
                turns+=1
                if turns >= 1:
                    while True:
                        dicenum2 = random.randint(2,12)
                        print(dicenum2)
                        if dicenum2 == dicenum:
                            print("you lose")
                            break
                        elif dicenum2 == 7:
                            print(f"you won ${self.money * 2 }")
                            break
    def odds(self):
        callout = int(input("What Payoff will you callout\nPayoff options are 2 to 1: 4 and 10, 3 to 2: 5 and 9\n 6 to 5: 6 and 8:      "))
        dicenum = random.randint(2,12)
        print(f"the point is {dicenum}")
        while True:
            if dicenum == callout:
                if callout == 4 or callout == 10:
                    print(f"you won ${self.money * 2}")
                    break
                if callout == 5 or callout == 9:
                    print(f"you won ${self.money * (3/2)}")
                    break
                if callout == 6 or callout == 8:
                    print(f"you won ${self.money * (6/5)}")
                    break
            elif dicenum == 7:
                print("you lose")
                break
            else:
                break
           # Once a shooter makes a point, you may make a “place bet” on 
           # numbers 4, 5, 6, 8, 9, and 10. If the shooter rolls any of these numbers 
           # before a 7, you win the following payoffs: 9 to 5 on 4 and 10, 7 to 5 on 5 and 9, and 7 to 6 on 6 and 8.
    def Place(self):
        callout = int(input("What Payoff will you callout\nPayoff options are 9 to 5: 4 and 10, 7 to 5: 5 and 9\n 7 to 6: 6 and 8:      "))
        dicenum = random.randint(2,12)
        print(f"the point is {dicenum}")
        while True:
            if dicenum == callout:
                if callout == 4 or callout == 10:
                    print(f"you won ${self.money * 9/5}")
                    break
                if callout == 5 or callout == 9:
                    print(f"you won ${self.money * (7/5)}")
                    break
                if callout == 6 or callout == 8:
                    print(f"you won ${self.money * (7/6)}")
                    break
            elif dicenum == 7:
                print("you lose")
                break
            
            else:
                break
    def Proposition(self):
        dicenum = random.randint(2,12)
        print(dicenum)
        prop = int(input("what bet are you going for:\nOptions\n1)Any Craps: 8 to 1 on 2 - 3 - 12\n2)Aces Or Twelve: 31 to 1 on 2 - 12\n3)Ace-Duece Or Eleven: 16 to 1 on 3 - 11\n4)Seven: 5 to 1 on 7\nWhat is your choice:   "))
        while True:
            if prop == 1:
                if dicenum in [2,3,12]:
                    print(f"you won{self.money * 8}")
                    break
                else:
                    print(f"you lost {self.money}")
                    break
            elif prop == 2:
                if dicenum == 2 or dicenum == 12:
                    print(f"you won{self.money * 31}")
                    break
                else:
                    print(f"you lost {self.money}")
                    break
            elif prop == 3:
                if dicenum == 3 or dicenum == 11:
                    print(f"you won{self.money * 16}")
                    break
                else:
                    print(f"you lost {self.money}")
                    break
            elif prop == 4:
                if dicenum == 7:
                    print(f"you won{self.money * 31}")
                    break
                else:
                    print(f"you lost {self.money}")
                    break
            
        pass
    def Field(self):
        dicenum = random.randint(2,12)
        while True:
            if dicenum in [3,4,9,10,11]:
                print(f"you win ${self.money}")
                break
            elif dicenum == 2:
                print(f"you win ${self.money * 2}")
                break
            elif dicenum == 12:
                print(f"you win ${self.money * 3}")
                break
            else:
                print(f"you lose ${self.money}")
                break
    def Nobet(self):
        print("If you don't want to bet why the hell are you here")

    
    
g = game()