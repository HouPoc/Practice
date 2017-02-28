class Node:
    #Initial the Node
    def __init__(self,data):
        self.data = data
        self.next = None
     

class Linked_List:
    #Initial the Linked List with a Head Node
    def __init__(self,):
        self.head = Node('head')
        self.length = 0
    
    #Overloading Insert function
    def Insert(self, node, after=None):
        next_node = self.head
        current_node = next_node
        self.length += 1
        if after is None:
            #Insert a Node at the end of the linked list
            while next_node != None:
                current_node = next_node
                next_node = current_node.next
            current_node.next = node
        else:
            #Insert a Nose after a certain Node
            while next_node.data != after:
                next_node = next_node.next
            node.next = next_node.next
            next_node.next = node      
    
    #Overloarding Delete function
    def Delete(self, after=None):
        next_node = self.head
        current_node = next_node
        if after is None:
            #Delete the last Node of the linked list
            while next_node.next is not None:
                current_node = next_node
                next_node = current_node.next
            current_node.next = None
            next_node.data = None
        if after is not None:
            #Delete a Node after a certain Node
            while next_node.data != after:
                next_node = next_node.next
            target = next_node.next
            next_node.next = target.next
            target.data = None
            target.next = None     

    #Print out the length of the linked list and all nodes
    def Check(self):
        #print ('Lenght of the list {}'.format(self.length))
        next_node = self.head.next
        while next_node is not None:
            print ('node {}'.format(next_node.data))
            next_node = next_node.next   

def Merge_Sort(list_head):
    # Base Case
    if list_head is None or list_head.next is None:
        return
    else:
        front_half = Node(0)
        back_half = Node(0)
        Half(list_head, front_half, back_half)
        Merge_Sort(front_half) 
        Merge_Sort(back_half) 
        head = Node(0)
        head = Sort_Merge(front_half, back_half)
        list_head.data = head.data
        list_head.next = head.next

def Sort_Merge(front, back):
    #base case
    result = Node(0)
    if front == None:
        result.data = back.data
        result.next = back.next
        return result
    elif back == None:
        result.data = front.data
        result.next = front.next
        return result
    if front.data < back.data:
       result.data = front.data
       result.next = Sort_Merge(front.next, back)
    else: 
        result.data = back.data
        result.next = Sort_Merge(front, back.next)
    return result

def Half(source, front_half, back_half):
    if source is None or source.next is None:
        front_half = source
        if source is not None:
            front_half.data = source.data
            front_half.next = None
        back_half = None
    else:
        slow = source
        fast = source.next
        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next
        back_half.data = slow.next.data
        back_half.next = slow.next.next
        #Ending the frst half by make the mid node point to none
        slow.next = None
        front_half.data = source.data
        front_half.next = source.next
