#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = 0
    count = 0
    for count in range(len(sys.argv) - 1):
        number = number + int(sys.argv[count + 1])
    print("{}".format(number))
