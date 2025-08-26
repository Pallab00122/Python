array=[0,8,2,7]
print("Element in index: ",array[1])
array[2]=37
print(array)
del array[0]

print("--Linked List--")
# append,add node ,delete node ,add a node in the last 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
        def __init__(self):
            self.head=None
        def append(self, data):
            new_node=Node(data)
            if self.head is None:
                self.head=new_node
                return
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node

        def display(self): 
            current = self.head
            elements = []
            while current:
                elements.append(current.data)
                current = current.next
            print(" -> ".join(map(str, elements)))

my_list = linkedList()
my_list.append(10)
my_list.append(5)
my_list.append(9)

print("Linked List after appends:")
my_list.display()

# My hash table 
hash_table={}
hash_table["Apple"]=60
hash_table["banana"]=10
hash_table["cherry"]=30

print("Hash table is : ",hash_table)



# def count_fre(sentence):
#     words_count={}
#     words=sentence.lower().split()
#     for word in words:
#         words_count[word]=words_count.get(word,0)+1
#     return words_count
# sentence1 = "The quick brown fox jumps over the lazy dog the fox is brown"
# fre1=count_fre(sentence1)
# print(sentence1)
# print(fre1)

class HashTable:
    def __init__(self):
        self.Max=100
        self.arr=[None for i in range (self.Max)]  
    def get_hash(self,key):
        h=0
        for char in key:
            h =h+ord(char)
        return h % self.Max
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
t=HashTable()
t['march 6']=130
t['april 7']=17
print(t)

