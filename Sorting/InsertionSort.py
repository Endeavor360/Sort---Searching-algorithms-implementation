def insertionSort(List):
    for i in range(len(List)):
        for j in range(i,0,-1):
            if List[j] < List[j-1]:
                List[j], List[j-1] = List[j-1], List[j]
            else:
                break
    return List

print(insertionSort([4,8,6,7,4352,232,-454,23.54,12.1,-56.8,9,7,-56.9,-56.8]))