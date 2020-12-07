from Node import Node
from LinkedList import Linkedlist 

class Queue:
    #Creating empty linked list to store stack
    __llist = None
    
    def __init__(self):
        
        self.__llist = Linkedlist()
    
    def Add(self,data):

        self.__llist.add(data)
        return 
    
    def Remove(self):

        return self.__llist.delete( 1 )
    
    def Peek(self):

        return self.__llist.delete( 1 , False)

    def print(self):

        self.__llist.print_linked_list()
            
    
#Entry point:
if __name__ == "__main__":
    queue = Queue()
    queue.Add(1)
    queue.Add(2)
    queue.Add(3)
    queue.Remove()
    queue.print()  