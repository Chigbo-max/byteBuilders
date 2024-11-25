class Stack:

    def __init__(self, size):
        self.size = size
        self.items = []


    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.isFull(): raise ValueError('Stack is full')
        self.items.append(item)

    def getItems(self):
        return self.items

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isFull(self):
        return self.size == len(self.items)