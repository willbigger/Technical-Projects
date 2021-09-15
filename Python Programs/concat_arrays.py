from array import *


def concat(*varargs):
    list_order = 0
    new_array = array("i", [])
    for i in range(len(varargs)):
        array_order = 0
        for f in range(len(varargs[list_order])):
            new_array.append((varargs[list_order])[array_order])
            array_order += 1
        list_order += 1
    return new_array
