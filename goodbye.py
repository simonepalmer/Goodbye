import os
import time
import random

def dots():
    for i in range(4):
        os.system("clear")
        display_message(
            f"{'.'*(i+1)}"
        )
        time.sleep(1)

def generate_message():
    key = random.randint(1, 10)
    message = messages[key]
    display_message(
        message
    )
    time.sleep(2)

def display_message(*args):
    os.system("clear")
    for string in args:
        print(string)

def main():
    while True:
        dots()
        generate_message()

messages = {
    1: "Hej då :'(",
    2: "Vi ses snart igen!",
    3: "Hej då :'(",
    4: "Jag kommer att sakna er!",
    5: "Glöm inte att punkta ut!",
    6: "Hej då :'(",
    7: "Vi ses snart igen!",
    8: "Hej då :'(",
    9: "Jag kommer att sakna er!",
    10:"Ni har iallfall fortfarande Linux!"
}

if __name__ == "__main__":
    main()
