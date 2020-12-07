import LinkedList

class InsertNode:

    def insert_node(self, data, node):
        temp = self.__head
        prev = temp
        
        while( temp != None ):
            if(temp.data != data):
                prev = temp
                temp = temp.next
            
            else:
                prev.next = node 
                node.next = temp 

        return(self)       

#Entry point:
if __name__ == '__main__':
    n = int(input("Insert a value:"))
    insert_node(n)