#! /usr/bin/python3

from playsound import playsound
import random
import time
import sys
import os

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = (
            '\33[94m', '\033[91m',
            '\33[97m', '\33[93m',
            '\033[1;35m', '\033[1;32m',
            '\033[0m'
        )
colors = [BLUE, RED, YELLOW, MAGENTA, GREEN]

try:
    def info():
        """
        Coder: Amo James
        Github: amo95
        Twitter: @dummyCod3r_
        """
        print(info.__doc__)


    def quit(name):
        try:
            print("\nDo you want to quit? Yes/No: ", end="")
            for i in range(len("testing")):
                entry = input()
                if entry == "Yes":
                    print("Thank you for playing")
                    time.sleep(1)
                    exit(1)
                elif entry == "No":
                    begin(name)
                else:
                    print("\nEnter either 'Yes' or 'No'>> ", end="")
                    continue
        except KeyboardInterrupt:
            quit(name)


    def begin(name):
        os.system("clear")
        global score

        score = 0
        lists = [
            "New Game", "Quit"]
        while True:
            for i, s in enumerate(lists, start=1):
                print("[{}] {}".format(i, s))
            print("Enter select >> ", end=" ")
            selects = int(input())
            if selects == 1:
                return scores(score)
            elif selects == 2:
                quit(name)
            else:
                print("You entered a wrong entry")
                break
        exit(1)


    def continuous(name):
        global score

        print('\n')
        score = 0
        lists = [
            "New Game", "Continue",
            "Score", "Clear Score",
            "Quit"]
        while True:
            for i, s in enumerate(lists, start=1):
                print("[{}] {}".format(i, s))
            print("Enter select >> ", end=" ")
            selects = int(input())
            if selects == 1:
                return scores(score)
            elif selects == 2:
                resume(name)
            elif selects == 3:
                highscore(name)
            elif selects == 4:
                os.system("rm ./data/*.txt")
                lists = ["new user", "ignore"]

                for i, user in enumerate(lists, start=1):
                    print(f"{i}: {user}")

                entry = input("Select: ")
                if entry == "1":
                    start()
                elif entry == "2":
                    begin("no name")
                else:
                    print("You entered wrong option")
                    continue

            elif selects == 5:
                quit(name)
            else:
                print("You entered a wrong entry")
                break
        exit(1)


    def saves(name, score):
        with open(f"./data/{name}.txt", "w+") as output:
            output.write(f"{name}:{score}")

    def scores(score):
        try:
            for i in range(10):
                lists = random.sample(range(0, 9), 2)
                sums = int(input(f"{lists[0]} + {lists[1]} = "))
                if sums == (lists[0] + lists[1]):
                    score += 10
                    saves(name, score)
                elif type(sums) is not int or sums != (lists[0] + lists[1]):
                    print("Wrong answer!!!\n")
                    score -= 10
                    if score <= 0:
                        os.system("clear")
                        for i in range(4):
                            if i == 3:
                                playsound("./effects/Sound Effect - YouTube.MP3")
                            else:
                                with open("./ascii.txt", "r") as text:
                                    print(random.choice(colors) + text.read() + END)
                                    playsound('./effects/game-over-sound-effect.mp3')

                        time.sleep(3)
                        os.system("clear")
                        continuous(name)
                    # saves(name, score)

                else:
                    pass

        # suppress warning the intepreter throws when strings are entered
        except ValueError:
            print("Enter a number!!")
            time.sleep(0.5)
            scores(score)

        # i just dont know why i added this line code :)
        time.sleep(1)
        os.system("clear")
        continuous(name)


    def read(file):
        try:
            f = open(f"./data/{file}.txt", "r")
            contents = f.read()
            os.system("clear")
            integer = int(contents[-1])
            if integer >= 0 and integer <= 25:
                print(RED + contents + END)
            elif integer > 25 and integer <= 70:
                print(YELLOW + contents + END)
            else:
                print(GREEN + contents + END)

            print("Press enter to continue")
            enter = input()
            if enter == "":
                pass

        # this exception is not necessary tho
        except FileNotFoundError:
            print("User not found!!")
            start()


    def resume(file):
        for i in range(3):
            username = input("Verify username: ")
            if username == file:
                scores(score)
            else:
                print("Wrong Entry!!")
                time.sleep(1)
                continue


    def highscore(name):
        read(name)

        time.sleep(1)
        os.system("clear")
        continuous(name)


    def spin():
        while True:
            for cursor in '|/-\\':
                yield cursor


    def start_spin():
        spinner = spin()
        for _ in range(50):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
        os.system("clear")


    def start():
        try:
            global name
            name = input("Enter username: ")

            os.system("clear")
            print("Wait a moment", end=" ")
            start_spin()

            if name == " " or name == "":
                print("You entered Nothing!! Retry")
                time.sleep(1)
                start()

            if os.path.isfile(f"./data/{name}.txt"):
                continuous(name)
            else:
                begin(name)

        except KeyboardInterrupt:
            print("Exiting session...")
            default = 0
            symbol = "."

            while default < 10 and len(symbol) < 10:
                os.system("clear")


                # terminating session for unauthorized access
                print("Quitting game" + symbol)

                # delay shutdown
                time.sleep(1)
                default += 1
                symbol = symbol + "."

            print("\nThank you for using this script")
            time.sleep(0.5)
            exit(1)

    def permission():
        if os.getuid() == 0000:  # userid is 0000 for users and 1000 for admins
            print(RED + "run this game as root!" + END)
            exit(1)

    if __name__ == '__main__':
        try:
            farg, sarg = sys.argv
            permission()
            info()
            start()

        except ValueError:
            print(RED + "Warning:" + END + YELLOW
                        + "Type python3 <script> start" + END)

except EOFError:
    print(RED + "\n\nYou are exiting....\n" + END)
    time.sleep(2)
    exit(1)
