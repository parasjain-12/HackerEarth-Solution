'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
class TrieNode:
    def __init__(self):
        self.EndofWord =False
        self.children  = [None]*26
        self.word_count = 0
        
class Trie:
    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        return TrieNode()
    
    def charToint(self,char):
        return ord(char) -ord('a')
    
    def insert(self,key):
        temp = self.root
        l = len(key)
        for i in range(l):
            #print(i)
            x = self.charToint(key[i])
            #print("This is x",x)
            if not temp.children[x]:
                temp.children[x] = self.getNode()
            temp = temp.children[x]
            temp.word_count +=1
        temp.EndofWord = True
        
 
        
    def get_prefix(self,key):
        temp =self.root
        for i in range(len(key)):
            x = self.charToint(key[i])
            if  not temp.children[x]:
                return None
            temp = temp.children[x]
        return temp
    
    
    def find(self,key):
        node = self.get_prefix(key)
        #print(node)
        return node.word_count if node else 0
        
t = Trie()


n,q = map(int,input().split())
for i in range(n):
    t.insert(input())
    
    
for i in range(q):
    x = t.find(input())
    print(x)
