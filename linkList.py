class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class link_list:
    def __init__(self):
        self.head=node()

    #insert element in linklist
    def append(self,data):
        new_node=node(data)
        current_node=self.head
        while current_node.next!=None:
            current_node=current_node.next
        current_node.next=new_node

    #length of linklist
    def length(self):
        current_node= self.head
        total=0
        while current_node.next!=None:
            total+=1
            current_node=current_node.next
        return total

    #display linklist
    def display(self):
        ele=[]
        cur_node=self.head
        while cur_node.next !=None:
            cur_node=cur_node.next
            ele.append(cur_node.data)
        print(ele)

    #get element
    def get(self,index):
        if index>=self.length():
            print("Error")
            return None
        current_index=0
        current_node=self.head
        while True:
            current_node=current_node.next
            if current_index==index: return current_node.data
            current_index+=1
    
    #delete element
    def dele(self,index):
        if index>=self.length():
            print("Error")
            return None
        current_index=0
        current_node=self.head
        while True:
            last_node=current_node
            current_node=current_node.next
            if current_index==index:
                last_node.next=current_node.next
                return
            current_index+=1


mylist=link_list()
mylist.append(4)
mylist.append(2)
mylist.append(6)
mylist.append(10)
mylist.append(100)
print(mylist.get(3))
mylist.dele(3)

mylist.display()
