class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550
        self.state = "Main_Menu"
        self.is_filling = False

    def turn_off_machine(self):
        self.state = "OFF"

    def display_menu(self):
        if self.state == "Main_Menu":
            print("Write action(buy, fill, take, remaining, exit): ")
        elif self.state == "Buy_Menu":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    def buy_espresso(self):
        if self.water < 250 and self.coffee < 16:
            print("Sorry, not enough coffee and water")
        elif self.water < 250:
            print("Sorry, not enough water")
        elif self.coffee < 16:
            print("Sorry, not enough coffee")
        elif self.water >= 250 and self.coffee >= 16:
            print("I have enough resources, making you coffee")
            self.water -= 250
            self.coffee -= 16
            self.money += 4
            self.cups -= 1

    def buy_latte(self):
        if self.water < 350 and self.milk < 75 and self.coffee < 20:
            print("Sorry, not enough water, milk and coffee!")
        elif self.water < 350:
            print("Sorry, not enough water!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.coffee < 20:
            print("Sorry, not enough coffee!")
        elif self.water >= 350 and self.milk >= 75 and self.coffee >= 20:
            print("I have enough resources, making you coffee!")
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.money += 7
            self.cups -= 1

    def buy_cappuccino(self):
        if self.water < 200 and self.milk < 100 and self.coffee < 12:
            print("Sorry, not enough water, milk and coffee!")
        elif self.water < 200:
            print("Sorry, not enough water!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        elif self.coffee < 12:
            print("Sorry not enough coffee!")
        elif self.water >= 200 and self.milk >= 100 and self.coffee >= 12:
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.money += 6
            self.cups -= 1

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:"))
        self.is_filling = False

    def give_money(self):
        print("i gave you $", self.money)
        self.money = 0

    def remaining(self):
        print(f"""the coffee machine has:"
{self.water},"of water" 
{self.milk}, "of milk"
{self.coffee},"of coffee beans"
{self.cups}, "of disposable cups" 
{self.money}, "of money""")

    def input(self, user_input):
        if self.state == "Main_Menu":
            if user_input == "buy":
                self.state = "Buy_Menu"
            elif user_input == "fill":
                self.is_filling = True
                self.fill()
                self.display_menu()
            elif user_input == "remaining":
                self.remaining()
                self.display_menu()
            elif user_input == "take":
                self.give_money()
                self.display_menu()
            elif user_input == "exit":
                self.turn_off_machine()
        if self.state == "Buy_Menu":
            if user_input == "1":
                self.buy_espresso()
                self.state = "Main_Menu"
            elif user_input == "2":
                self.buy_latte()
                self.state = "Main_Menu"
            elif user_input == "3":
                self.buy_cappuccino()
                self.state = "Main_Menu"
            elif user_input == "back":
                self.state = "Main_Menu"
            self.display_menu()
