import doctest
import pdb

MAPPING = {
    '}': '{',
    ']': '[',
    ')': '(',
}

class Stack(object):
    """
    Stack datastructure. To keep it simple, there is no
    upper bound for our stack. i.e you can put as many items
    as you can inside a stack and there will be no stack
    overflow.

    This is how stack should work:

    Create stack object to hold stack of items

    >>> stack = Stack()

    Initially stack will be empty.

    >>> stack.isEmpty()
    True

    Use .push() to push item in stack

    >>> stack.push("{")

    You can pop item from stack using .pop()

    >>> stack.pop()
    '{'

    Write a representation of your stack object.
    >>> stack.push("[")
    >>> stack.push("{")
    >>> stack.push("(")
    >>> stack
    <Stack with length: 3>

    >>> stack.pop()
    '('

    >>> repr(stack)
    '<Stack with length: 2>'

    Write a better string representation of stack
    >>> print stack
    Stack: [{
    >>> stack.push("(")
    >>> print stack
    Stack: [{(
    >>> str(stack)
    'Stack: [{('
    >>> "My stack is as follows: %s" % stack
    'My stack is as follows: Stack: [{('
    """

    def __init__(self):
        self.data = []  # empty list

    # write remaining methods here

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(-1)

#    def clear(self):
#        self.data = []

    def isEmpty(self):
        if not self.data:
            return True
        else:
            return False

    def __repr__(self):
        return "<Stack with length: %s>" % self.data.__len__()

    def __str__(self):
        mystack = ""
        for mychar in self.data:
            mystack += mychar
        return "Stack: %s" % mystack



def is_balanced(input_string):
    """
    Return True if all paraentheses are balanced, otherwise return False.

    >>> is_balanced("({})")
    True

    >>> is_balanced("({}[[]])")
    True

    >>> is_balanced("([]}")
    False

    >>> is_balanced("(((()")
    False

    >>> is_balanced("}")
    False

    >>> is_balanced("")
    True

    """

    stack = Stack()
    for item in input_string:
        if item in MAPPING.values():
            stack.push(item)
        else:
            if stack.isEmpty():
                return False
            value = stack.pop()
            if value != MAPPING[item]:
                return False

    if not stack.isEmpty():
        return False
    return True


if __name__ == "__main__":
#    pdb.set_trace()
    doctest.testmod()

