from Node import Node
from LinkedList import Linkedlist 

class Stack:
    #Creating empty linked list to store stack
    __llist = None
    
    def __init__(self):
        self.__llist = Linkedlist()
    
    def Push(self,data):

        self.__llist.add(data)
        return 
    
    def Pop(self):

        return self.__llist.delete(self.__llist.size())
    
    def Peek(self):

        return self.__llist.delete(self.__llist.size() , False)

    def print(self):

        self.__llist.print_linked_list()
            
    
    

#Entry point:
if __name__ == "__main__":
    
    stack = Stack()
    stack.Push(2)
    stack.Push(5)
    stack.Push(7)
    stack.print()
    print("Peeked value is:" + str(stack.Peek()) + "\n")
    print("\n")
    stack.print()