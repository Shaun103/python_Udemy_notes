import timeit 



menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["spam", "egg", "sausage", "bacon", "spam"],
    ["spam","egg", "sausage", "bacon", "chips"],
    ["spam","egg", "spam", "spam", "bacon", "spam"],
    ["spam","egg", "sausage", "bacon"],
    ["chicken", "chips"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)


def not_spam(meal_list: list):
    return "spam" not in meal_list

def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))
    return spamless_meals


def spamless_comp():
    # meals = [meal for meal in menu if "spam" not in meal]
    meals = [meal for meal in menu if not_spam(meal)]
    return meals


if __name__ == "__main__":
    print(spamless_comp())
    print(spamless_filter())
    print(timeit.timeit(spamless_comp, number=1000))
    print(timeit.timeit(spamless_filter, number=1000))