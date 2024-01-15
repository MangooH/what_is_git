from random import randint, choice

get_randint = lambda: [randint(1, 45) for _ in range(6)]
get_choice = lambda: [choice(range(1, 45 + 1)) for _ in range(6)]

foods = [
    "banana",
    "grape",
    "apple",
]

if __name__ == "__main__":
    print(get_randint())
    print(get_choice())
