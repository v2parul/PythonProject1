#!usr/bin/python3
def main(msg):
    print(msg)


def secondary(msg):
    print(msg)
    # two functions to demonstrate changes to main.py
    #updating another funtion in another directory to create conflict.
def tertiary(msg):
    print(msg)

main("hello world")
secondary("another update")

#nothing to modify, will merge later.

tertiary("hello"

