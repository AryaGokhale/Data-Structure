from Node import Node
#class Node:
    
    #def __init__(self,data):
        #self.data = data
        #self.next = None

class Linkedlist:
    
    def __init__(self):
        self.__head = None
        self.__current = None
        self.__llsize = 0
     
    def add(self, data):
        
        node = Node(data)
        
        if(self.__current == None):
            self.__head = node
            self.__current = node
            self.__llsize += 1
            return
        
        self.__llsize += 1        
        self.__current.next = node
        self.__current = node
        
    
    def insert(self,position,data):

        if(position < 1 or self.__llsize < position ):
            
            print("Invalid position")
            return

        node = Node(data)
        temp = self.__head

        if(position == 1):
            
            self.__llsize += 1
            node.next = temp
            self.__head = node
            return

        i = 1
        while(temp != None):
                    
            if (i < position):
                temp = temp.next
                i += 1
                
            else :    
                self.__llsize += 1
                node.next = temp.next
                temp.next = node
                break
                
        return 
        

    def delete(self,position,should_delete = True):
        
        if ( position < 1 or self.__llsize < position  ):
            
            print("Invalid position")
            return None

        temp = self.__head
        
        if (position == 1):
            if should_delete == True:
                self.__llsize -= 1
                self.__head = temp.next
            return temp.data

        deleted_item = None
        i = 1
        while( temp != None):

            if(i < position-1):
                temp = temp.next
                i += 1
                continue
            else:
                deleted_item = temp.next.data
                if should_delete == True:
                    self.__llsize -= 1                
                    temp.next = temp.next.next                

                break

        return deleted_item

    def print_linked_list(self):
        temp = self.__head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def size(self):
        
        return self.__llsize 

#Entry point:
if __name__ == '__main__':
    #start with empty list
    llist = Linkedlist()
    llist.add(1)
    llist.add(2)
    llist.add(4)
    llist.add(5)
    #llist.insert(1,0)
    #llist.insert(3,3)
    #llist.insert(6,6)
    #llist.insert(7,7)
    #llist.insert(1,-1)
    #llist.insert(5,8)
    #llist.delete(3)
    #llist.delete(1)
    #llist.delete(-1)
    llist.print_linked_list()