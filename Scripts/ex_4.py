import random

animals = ["dogs", "cats", "bats"]


def main():
    favourite = random.choices(animals, [8, 1, 1], k=1)[0]
    print(f"I love {favourite}")

main()
