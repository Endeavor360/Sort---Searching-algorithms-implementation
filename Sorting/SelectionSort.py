def selectionSort(List):
    sortedList = []
    while len(List)>0:
        minI = List[0]
        for i in List:
            if i <= minI:
                minI = i
        List.remove(minI)
        sortedList.append(minI)
    return sortedList

print(selectionSort([1,2,5,2,3,86,3,1,-3]))