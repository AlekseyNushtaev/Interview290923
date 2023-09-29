class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
def invert(el: str):
    open = '{[('
    close = '}])'
    return close[open.find(el)]
def balance(string: str):
    stack = Stack()
    for i in string:
        if i in '([{':
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            else:
                if i != invert(stack.pop()):
                    return False
    if stack.is_empty():
        return True
    else:
        return False
print(balance('(((([{}]))))'))
print(balance('[([])((([[[]]])))]{()}'))
print(balance('{{[()]}}'))
print(balance('}{}'))
print(balance('{{[(])]}}'))
print(balance('[[{())}]'))