from dt_stc import *
from random import *
import sys

def test(list):
    print(list.data)


if __name__ == "__main__":
    choice = str(sys.argv[1])
    if choice is "L":
        demo_list = Linked_List()
        for num in range(1, 11):
            item = randint(2, 100)
            demo_list.Insert(Node(item))
        demo_list.Check()
        print ('')
        Merge_Sort(demo_list.head.next)
        demo_list.Check()
    if choice is "S":
        demo_stack = Stack(5)
        checker = 0
        for num in range (1,10):
            number = randint(2,100)
            if number%2 == 0:
                demo_stack.Push(number)
                checker +=1
            else:
                demo_stack.Pop()
                checker -=1
        demo_stack.Check()
    if choice is "Q":
        demo_queue =Queue(5)
        for num in range (1,10):
            number = randint(2,100) 
            print(number)      
            if number%2 == 0:
                demo_queue.Enqueue(number)
            else:
                demo_queue.Dequeue()
        demo_queue.Check()
        demo_queue.Peek()
     
