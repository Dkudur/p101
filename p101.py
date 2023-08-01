import random

choice = "y"

while (choice == "y"):
    num = random.randint(1, 6)
    if (num == 1):
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        choice = input("Do you want to roll a dice, use y as yes and n as no : ")
        num = random.randint(1, 6)

    elif (num == 2):
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
        choice = input("Do you want to roll a dice, use y as yes and n as no : ")
        num = random.randint(1, 6)

    elif (num == 3):
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        choice = input("Do you want to roll a dice, use y as yes and n as no : ")
        num = random.randint(1, 6)

    elif (num == 4):
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        choice = input("Do you want to roll a dice, use y as yes and n as no : ")
        num = random.randint(1, 6)

    elif (num == 5):
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        choice = input("Do you want to roll a dice, use y as yes and n as no : ")
        num = random.randint(1, 6)

    if (num == 6):
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        choice = input("Do you want to roll a dice, use y as yes and n as no : ")
        num = random.randint(1, 6)