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


start = time.perf_counter()
print(quickSort([5, 4, 3, 2, 1, 4.5, 23, -4, -7, -9, 3.4]))
end = time.perf_counter()
print(end - start)
