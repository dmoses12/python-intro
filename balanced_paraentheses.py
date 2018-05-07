"""
>>> is_balanced("({[]})")
Given input: ({[]})
True
>>> is_balanced("(){}[]([])")
Given input: (){}[]([])
True
>>> is_balanced("[]{]")
Given input: []{]
False
>>> is_balanced("([]}")
Given input: ([]}
False
"""

import doctest

def is_balanced(input_string):
    """
    Function to detect that paraenthesis specified in `input_string`
    are balanced.

    Returns True if balanced else return False
    """
    print "Given input: %s" % input_string

    # complete this function
    mylist = []

    #if open parens, push, if closed parens pop and compare.  If no match return false.
    for achar in input_string:
        if achar in ( '(', '{', '[' ):
            mylist.append(achar)  # push open paren
        elif achar in ( ')', '}', ']' ):
            bchar = mylist.pop() # pop close paren and compare
            if ( bchar == '(' and achar == ')' ) or ( bchar == '{' and achar == '}' ) or ( bchar == '[' and achar == ']' ):
                continue
            else:
                return False
    return True

if __name__ == "__main__":
    doctest.testmod()
    print is_balanced("({[]})")  # should return True
    print is_balanced("(){}[]([])") # should return True
    print is_balanced("[]{]") # should return False
    print is_balanced("([]}") # should return False

