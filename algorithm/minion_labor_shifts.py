import sys

def main():
    list = argv[1]
    if len(list) > 100:
        return "list length is more than 100"
    else:
        frequency_constrain = int(argv[2])
        if frequency_constrain == 0:
           return list
        else:
           new_list = list.sort()
           keys = set(new_list)
           for key in keys:
               if new_list[new_list.index(key)+freqneucy_constrain] == key:
                   list = filter(lambda x: x==key, list)
           return list
               
