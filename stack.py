import subprocess
from time import sleep

class Node:
    def __init__ (self, x):
        self.x = x
        self.next = None

class Stack:
    def __init__ (self):
        self.head = None
        self.lenght = 0

    def push(self, x):
        if(self.head == None):
            self.head = Node(x)
        else: 
            node = Node(x)
            node.next = self.head
            self.head = node
        self.lenght += 1
        print("{x} pushed to the stack.".format(x=x))

    def pop(self):
        if(self.head != None):
            self.head = self.head.next
            self.lenght -=1
            print("Popped.")
        else:
            print("There is no element to pop.")

    def printStack(self):
        pointer = self.head
        for i in range(self.lenght):
            print("-{p}-".format(p=pointer.x))
            pointer = pointer.next

stack = Stack()

def clearScreen():
    try:
        subprocess.run(['clear'], check = True, shell=True) #linux
    except:
        subprocess.run('cls', shell=True)

while True:

    clearScreen()

    try:
        selection = int(input("Select a function to do. \n1-Push\n2-Pop\n3-PrintStack\n4-Exit\n"))
        clearScreen()

        if(selection==1):
            x = int(input("Enter a value to push.\n"))
            stack.push(x)
            stack.printStack()        

        elif (selection==2):
            stack.pop()
            stack.printStack()  
            
        elif(selection==3):
            stack.printStack()

        elif(selection==4):
            break

        else:
            print("Invalid input.")
        sleep(2)

    except:
        print("Invalid input.")
        sleep(2)










