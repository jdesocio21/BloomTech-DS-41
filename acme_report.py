from statistics import mean
from acme import Product
import random


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    global product_list
    product_list = []

    for x in range(num_products):
        rand_prod_name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        rand_price = random.randint(5, 100)
        rand_weight = random.randint(5, 100)
        rand_flam = random.uniform(0.0, 2.5)

        prod = Product(rand_prod_name, rand_price, rand_weight, rand_flam)
        product_list.append(prod)

    return product_list


def inventory_report(product_list):
    unq_names = set(x.name for x in product_list)
    num_unq = len(unq_names)
    avg_price = mean(x.price for x in product_list)
    avg_weight = mean(x.weight for x in product_list)
    tot_flam = sum(x.flammability for x in product_list)
    avg_flam = tot_flam / len(product_list)

    return (num_unq, avg_price, avg_weight, avg_flam)
