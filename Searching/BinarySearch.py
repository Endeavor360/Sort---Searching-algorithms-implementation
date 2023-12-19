import time

def quickSort(List):
    if len(List) == 1 or len(set(List)) == 1 or List == []:
        return List
    else:
        repeat = True
        k = 0
        while repeat:
            low_List, high_List = [], []
            for i in List:
                if i <= List[k]:
                    low_List.append(i)
                else:
                    high_List.append(i)
            if low_List == [] or high_List == []:  # if the first element is max or a min it will run indefinitely. this will change the pivot element to next element
                repeat = True
                k += 1
            else:
                repeat = False
        return quickSort(low_List) + quickSort(high_List)

#iterative approach
def binarySearch1(List, item):
    found = False
    n = len(List)
    while found==False:
        n = n //2
        if len(List) ==0:
            break
        elif List[n] < item:
            List = List[n+1:]
            continue
        elif List[n] >  item:
            List = List[ :n]
            continue
        else:
            found = True
            break
    return found

#recursive approach
def binarySearch2(List,item):
    n = len(List)//2
    if List ==[]:
        return False
    elif List[n] > item:
        return binarySearch2(List[:n],item)
    elif List[n] < item:
        return binarySearch2(List[n+1:],item)
    elif List[n] == item:
        return True


List = [2,4,6,2,5,3,56,2,456,2,-43,23,23,55]

start1 = time.perf_counter()
print(binarySearch2(quickSort(List),456))
end1 = time.perf_counter()
print(end1 - start1)


start2 = time.perf_counter()
print(binarySearch1(quickSort(List),456))
end2 = time.perf_counter()
print(end2 - start2)