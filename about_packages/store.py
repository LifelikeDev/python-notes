def say_something():
    return "Welcome to our store"


def place_order(items):
    order_content = ""
    num = 1

    for item in items:
        order_content += f"""{num}. {item.strip().capitalize()}
"""
        num += 1

    return order_content
