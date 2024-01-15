from random import randint

get_luckies = lambda: [randint(1, 45) for _ in range(6)]

if __name__ == "__main__":
    print(get_luckies())
