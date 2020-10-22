class Coffee:
    money = 550
    water = 400
    milk = 540
    beans = 120
    cups = 9

    def display(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")
        self.base_choices()


    def espresso(self):
        espresso_water = 250
        espresso_beans = 16
        espresso_cost = 4
        if self.water >= espresso_water and self.beans >= espresso_beans and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.cups -= 1
            self.water -= espresso_water
            self.beans -= espresso_beans
            self.money += espresso_cost
            self.base_choices()
        
        else:
            if self.water < espresso_water:
                print("Sorry, not enough water!")
                self.base_choices()


    def latte(self):
        latte_water = 350
        latte_milk = 75
        latte_beans = 20
        latte_cost = 7
        if self.water >= latte_water and self.milk >= latte_milk and self.beans >= latte_beans and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.cups -= 1
            self.water -= latte_water
            self.milk -= latte_milk
            self.beans -= latte_beans
            self.money += latte_cost
            self.base_choices() 
        else:
            if self.water < latte_water:
                print("Sorry, not enough water!")
                self.base_choices()
                


    def cappuccino(self):
        cappuccino_water = 200
        cappuccino_milk = 100
        cappuccino_beans = 12
        cappuccino_cost = 6
        if self.water >= cappuccino_water and self.milk >= cappuccino_milk and self.beans >= cappuccino_beans and self.cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.cups -= 1
            self.water -= cappuccino_water
            self.milk -= cappuccino_milk
            self.beans -= cappuccino_beans
            self.money += cappuccino_cost
            self.base_choices()
        else:
            if self.water < cappuccino_water:
                print("Sorry, not enough water!")
                self.base_choices()


    def buy_coffee(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if choice == "1":
            self.espresso()
        elif choice == "2":
            self.latte()
        elif choice == "3":
            self.cappuccino()
        elif  choice == "back":
            self.base_choices()


    def fill(self):
        add_water = int(input("Write how many ml of water do you want to add:"))
        add_milk = int(input("Write how many ml of milk do you want to add:"))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.cups += add_cups
        self.base_choices()
    
    def take(self):
        print("I gave you $", self.money)
        self.money = 0
        self.base_choices()

    def base_choices(self):
        choice = input("Write action (buy, fill, take, remaining, exit):")
        if choice == "buy":
            self.buy_coffee()
        elif choice == "fill":
            self.fill()
        elif choice == "take":
            self.take()
        elif choice == "remaining":
            self.display()
        elif choice == "exit":
            exit()
        else:
            pass

user = Coffee()
user.base_choices()
