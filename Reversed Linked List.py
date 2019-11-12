class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    
    def __init__(self):
        self.head = None
        


    def printl(self):        
        t =self.head
        
        while t:
            print(t.data,end = ' ')
            t = t.next
            
    def atLast(self,new_data):
        new_node = node(new_data)
        if self.head is None: 
            self.head = new_node 
            return
        
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        new_node.next = None
        
    
                    
    def addElement(self,lis):
        lis = lis[::-1]
        for i in range(len(lis)):
            nl.atLast(lis[i])
        
            
                
        
    def reverse(self):
        temp = self.head
        lis = []
        while temp:
            #print(temp.data)
            if int(temp.data)%2==0:
                lis.append(temp.data)
                temp = temp.next
            else:
                if len(lis)>0:
                    nl.addElement(lis)
                    lis = []
                nl.atLast(temp.data)
                temp = temp.next
                
            
        if len(lis)>0:
            nl.addElement(lis)
        
        
l = linkedList()
nl = linkedList()
t = int(input())
arr = list(map(int,input().split()))
for i in range(len(arr)):
    l.atLast(arr[i])
l.reverse()
nl.printl()
        
