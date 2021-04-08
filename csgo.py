import random
import sys


__DEFAULT_GAMER_COUNT = 5
__NO_ARG_MSG = """No arguments. This application needs atleast 1 argument: path to a file with gamer names.
Normal usage: 
csgo.py <PATH_TO_GAMER_FILE> <NUMBER_OF_GAMERS>

If only one argument is provided(path to a file containing gamers), default value of 5 gamers is used.
"""

def main():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print(__NO_ARG_MSG)
        exit(1)
    f = open(sys.argv[1])
    gamers = [line.strip() for line in f]
    if len(sys.argv) == 2:
        print("Too few gamers in file, use everybody.") if  len(gamers) < 5 else print(random.sample(gamers, __DEFAULT_GAMER_COUNT))
    else:
        try:
            gamer_count = int(sys.argv[2])
            print("Too few gamers in file, use everybody.") if gamer_count > len(gamers) else print(random.sample(gamers, gamer_count))
        except Exception:
            print("LOL enter a number you homo xD")
    



if __name__ == "__main__":
    main()