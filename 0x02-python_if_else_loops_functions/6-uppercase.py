#!/usr/bin/python3

def uppercase(string):
    for each_letter in string:
        if ord(each_letter) > 96 and ord(each_letter) < 123:
            each_letter = chr(ord(each_letter) - 32)
        else:
            each_letter = chr(ord(each_letter))
        print("{}".format(each_letter), end="")
    print("")


