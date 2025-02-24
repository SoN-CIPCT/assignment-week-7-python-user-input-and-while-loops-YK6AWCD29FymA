pizza_orders = ["Mar", "Ita", "Cal"]
finished_pizzas = []
while pizza_orders:
        current_pizza = pizza_orders.pop()
        print(f"Your pizza pie is finished, {current_pizza}!")
        finished_pizzas.append(current_pizza)

print("\n")
for pizza in finished_pizzas:
        print (f"The {pizza} was made")