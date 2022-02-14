import argparse

SIZES = {
    "s": "Small"
    "m": "Medium"
    "l": "Large"
    "x1": "Extra Large"
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
