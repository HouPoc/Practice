from dt_stc import *
from random import *

def test(list):
    print(list.data)


if __name__ == "__main__":
    demo_list = Linked_List()
    for num in range(1, 11):
        item = randint(2, 100)
        demo_list.Insert(Node(item))
    demo_list.Check()
    print ('')
    Merge_Sort(demo_list.head.next)
    demo_list.Check()
