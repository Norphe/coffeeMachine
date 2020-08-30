from CoffeeMachine import CoffeeMachine

coffee_machine = CoffeeMachine()
while coffee_machine.state != "OFF":
    user_input = input()
    coffee_machine.input(user_input)
