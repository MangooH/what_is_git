from random import choice

get_luckies = lambda: [choice(range(1, 45 + 1)) for _ in range(6)]

if __name__ == "__main__":
    print(get_luckies())
