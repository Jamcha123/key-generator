import os 
import random
import argparse

def main(letters: str, digits: int):
    if letters not in os.listdir():
        return letters + " not found or not a text file"
    ans, f = "", open(letters, "r")
    targets = str(f.read())
    f.close()
    for x in range(int(digits)):
        nums = random.randrange(0, len(targets)-1)
        ans += str(targets[nums])
    return ans
args = argparse.ArgumentParser(
    prog="pykey",
    description="python cli tool for random key generators",
)
args.add_argument("-w", "--wordlist")
args.add_argument("-l", "--length")
parser = args.parse_args()
print(main(parser.wordlist, parser.length))