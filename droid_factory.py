"""
Gunnar Bachmann
11/6/2019
droid_factory.py
CSCI-141
Homework 11
"""

from dataclasses import dataclass
from cs_queue import Queue
from cs_queue import make_empty_queue
from cs_queue import enqueue
from cs_queue import dequeue
from cs_queue import front
from cs_queue import back
from cs_queue import is_empty

@dataclass
class Droid:
    __slots__ = 'serial_num', 'head', 'body', 'arms', 'legs'
    serial_num: int
    head: bool
    body: bool
    arms: bool
    legs: bool


def readfile(filename):
    """
    Takes in a filename and opens it. Then creates
    an empty queue as a conveyor belt. Then the function
    goes line by line reading the opened file and adding
    each item to the conveyor belt. Then closes the file,
    and return belt.

    :param filename: name of inputted file
    :return: conveyor belt with items from file
    """
    file = open(filename)
    belt = make_empty_queue()
    for line in file:
        line = line.strip('\n')
        enqueue(belt, line)
    file.close()
    return belt


def build_droid(serial_num, belt):
    """
    This function builds a droid with the items on the conveyor belt, while
    assigning them a serial number.

    :param serial_num: serial number for the droid being created
    :param belt: conveyor belt with parts to build the droid
    :return: assembled droid
    """
    print("Building a new droid with the serial number", serial_num)
    new_droid = Droid(serial_num, False, False, False, False)
    while new_droid.head == False or new_droid.body == False or new_droid.arms == False or new_droid.legs == False:
        if belt.front.value == 'head' and new_droid.head == False:
            new_droid.head = True
            dequeue(belt)
            print("attaching head...")
        elif belt.front.value == 'body' and new_droid.body == False:
            new_droid.body = True
            dequeue(belt)
            print("attaching body...")
        elif belt.front.value == 'arms' and new_droid.arms == False:
            new_droid.arms = True
            dequeue(belt)
            print("attaching arms...")
        elif belt.front.value == 'legs' and new_droid.legs == False:
            new_droid.legs = True
            dequeue(belt)
            print("attaching legs...")
        else:
            droid_part = dequeue(belt)
            enqueue(belt, droid_part)
            print("placing unneeded part back on the belt:", droid_part)
    print("Droid", serial_num, "has been assembled!")


def as_many_droids_possible(belt):
    """
    This function, using the items on the conveyor belt, will
    build as many droids as it can until the conveyor belt is empty.

    :param belt: conveyor belt with droid parts
    :return: assemble droids until there are no more parts on the belt
    """
    serial_num = 1000
    while belt.front is not None:
        build_droid(serial_num, belt)
        serial_num += 1


def test():
    test1 = "droid_parts_1"
    test2 = "droid_parts_3"
    test3 = "droid_parts_5"
    test4 = "droid_parts_20"
    test5 = "droid_parts_1000"

    input("Ready to test droid_parts_1? [Enter] ")
    print("Testing droid_parts_1:")
    as_many_droids_possible(readfile(test1))

    print("")
    input("Ready to test droid_parts_3? [Enter] ")
    print("Testing droid_parts_3")
    as_many_droids_possible(readfile(test2))

    print("")
    input("Ready to test droid_parts_5? [Enter] ")
    print("Testing droid_parts_5")
    as_many_droids_possible(readfile(test3))

    print("")
    input("Ready to test droid_parts_20? [Enter] ")
    print("Testing droid_parts_20")
    as_many_droids_possible(readfile(test4))

    print("")
    input("Ready to test droid_parts_1000? [Enter] ")
    print("Testing droid_parts_1000")
    as_many_droids_possible(readfile(test5))


def main():
    """
    Store a filename from input. Then read that file and store the conveyor belt created
    from that file. Then, we will assemble as many droids as we can with the parts on
    the conveyor belt.

    :return:
    """
    print("Starting a shift at the Droid Factory!")
    filename = input("Input droid parts file: ")
    belt = readfile(filename)
    as_many_droids_possible(belt)
    print("All of the droids have been assembled! Time to clock out and play Sabacc...")


main()
print("Running test function...")
test()