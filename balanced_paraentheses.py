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
    for c in input_string:
        if c in ( '(', '{', '[' ):
            mylist.append(c)  # push open paren
        elif c in ( ')', '}', ']' ):
            b = mylist.pop() # pop close paren and compare
            if ( b == '(' and c == ')' ) or ( b == '{' and c == '}' ) or ( b == '[' and c == ']' ):
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

