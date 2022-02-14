import argparse

SIZES = {
    "s": "Small",
    "m": "Medium",
    "l": "Large",
    "x1": "Extra Large",
    "xx1": "Extra extra large"
}

CRUSTS = {"normal": "", "thin": " thin crust", "deep": "deep dish"}

def build_pizza(order):
    pizza = f"{SIZES[order['size']]}{CRUSTS[order['crust']]}"
    if order.get("toppings"):
        pizza += " With " + ", ".join(order["toppings"])
    if order.get("extra-cheese"):
        pizza += " plus extra cheese"
    if order.get("extra-sauce"):
        pizza += " and extra sauce"
    return pizza


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to the pizza builder, let's buil a pizza!!")
   
#Positional Argument
    parser.add_argument("size", type=str, choices=SIZES.keys(), help="Size of your Pizza")
    parser.add_argument("crust", type=str, choices=SIZES.keys(), help="Type of Pizza crust")
# Optional Argument
    parser.add_argument("-c", "--extra-cheese", action="store_true", dest="cheese", help="Add extra Sauce to your Pizza")
    parser.add_argument("-s", "--extra-sauce", action="store_true", dest="sauce", help="Add extra Sauce to your Pizza")
    # Collect into a list
    parser.add_argument("-t", "--toppings", type=str, nargs="+")
    parsed_args = parser.parse_args()
    print(parsed_args)
