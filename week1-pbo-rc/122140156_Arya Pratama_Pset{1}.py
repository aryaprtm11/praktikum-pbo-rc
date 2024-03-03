class robot:

    player = 0;

    def __init__(self, name, power, health, deff) :
        self.name = name
        self.power = power
        self.health = health
        self.deff = deff
        robot.player += 1

    def attack(self, enemy) :
        lost = self.power//enemy.deff
        enemy.health -= self.power//enemy.deff
        print(f"{self.name} attacked {enemy.name}, with attack power {lost}")
        enemy.info()

    def deffup(self) :
        self.deff += 2
        print(f"{self.name} defance up!\n")

    def healup(self) :
        self.health += 10
        print(f"{self.name} used heal potion and gain 10 health\n")

    def giveup(self) :
        print(f"{self.name} Gived up from battle and runaway\n")
        self.health = 0

    def info(self) :
        print(f"{self.name} health : {self.health}\n")

player1 = robot("Daedalus",70,100,12)
player2 = robot("Atleus",65,100,15)

i = 1
while player1.health > 0 or player2.health > 0:
    print(f"ROUND {i} ----------------------------------------------------------------------")
    print(f"Action :\n1. Attack\t 2. Deff Up\t 3.Heal Up\t 4. Give Up")
    action = input(f"{player1.name} Turn : ")

    match action :
        case "1" :
            player1.attack(player2)
        case "2" :
            player1.deffup()
        case "3" :
            player1.healup()
        case "4" :
            player1.giveup()
            print(f"{player2.name} WIN!")
            break

    if player2.health <= 0 :
        print(f"{player1.name} WIN!")
        break
            
    action2 = input(f"{player2.name} Turn : ")

    match action2 :
        case "1" :
            player2.attack(player1)
        case "2" :
            player2.deffup()
        case "3" :
            player2.healup()
        case "4" :
            player2.giveup()

    if player1.health <= 0 :
        print(f"{player2.name} WIN!")
        break

    i = i + 1