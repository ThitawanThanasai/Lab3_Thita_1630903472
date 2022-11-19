class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)

stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
stack.push("E")
stack.push("F")
print("Part 3.1.2: First in first out (FIFO) exercise")
print("Stack: ", end="")
print(stack.items)
stack.pop()
print("FIFO: ", end="")
print(stack.items)
stack.pop()
print("FIFO: ", end="")
print(stack.items)
stack.pop()
print("FIFO: ", end="")
print(stack.items)
stack.pop()
print("FIFO: ", end="")
print(stack.items)
stack.pop()
print("FIFO: ", end="")
print(stack.items)
stack.pop()
print("FIFO: ", end="")
print(stack.items)