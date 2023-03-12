
import sys

expression = sys.argv[1]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

def evaluate_expression(expression):
    stack = Stack()
    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operand2 is None:
                raise ValueError("Invalid expression")
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.push(result)
        elif token.startswith('('):
            operator = token[1:]
            stack.push(operator)
        elif token.endswith(')'):
            operand2 = stack.pop()
            operator = stack.pop()
            operand1 = stack.pop()
            if operand1 is None or operator is None or operand2 is None:
                raise ValueError
