"""
>>> is_balanced2("({[]})")
Given input: ({[]})
True
>>> is_balanced2("(){}[]([])")
Given input: (){}[]([])
True
>>> is_balanced2("[]{]")
Given input: []{]
False
>>> is_balanced2("([]}")
Given input: ([]}
False
"""


import doctest
#import pdb

mapping = {
    '}':'{',
    ']': '[',
    ')': '(',
}

stack = []

def push(item):
    stack.append(item)

def pop(item):
    return stack.pop(-1)

def clear():
    global stack
    stack = []


def is_balanced2(input_string):
    """
    >>> is_balanced2("({[]})")
    Given input: ({[]})
    True
    >>> is_balanced2("(){}[]([])")
    Given input: (){}[]([])
    True
    >>> is_balanced2("[]{]")
    Given input: []{]
    False
    >>> is_balanced2("([]}")
    Given input: ([]}
    False
    """
    print "Given input: %s" % input_string
    #pdb.set_trace()
    clear()
    for item in input_string:
        if item in mapping.values():
                push(item)
        else:
            try:
                value = pop(-1)
            except IndexError:
                return False
            if mapping[item] == value:
                continue
            else:
                return False
    if stack:
        return False
    else:
        return True


if __name__ == "__main__":
    doctest.testmod()

    print is_balanced2("({[]})")  # should return True
    print is_balanced2("(){}[]([])") # should return True
    print is_balanced2("[]{]") # should return False
    print is_balanced2("([]}") # should return False
