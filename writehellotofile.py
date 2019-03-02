import argparse
from typing import Any

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program is testing docker containers')
    parser.add_argument('-n', help='Jou naam', required=True)
    parser.add_argument('-v', help='Jou van', required=True)
    args = parser.parse_args()

    print("Hello world!")
    print("Jou naam is: {0}".format(args.n))
    print("Jou van is: {0}".format(args.v))
    with open("hello.txt", "w") as f:
        f.write("This is hello world to file\n")
        f.write("Jou naam is: {0}\n".format(args.n))
        f.write("Jou van is: {0}\n".format(args.v))
        f.close()
