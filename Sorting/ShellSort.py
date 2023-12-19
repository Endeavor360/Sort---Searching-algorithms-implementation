def shellSort(List):
    n = len(List)
    while n >0:
        n = n//2
        k = 0
        while k+n < len(List):
            if List[k] > List[k+n]:
                List[k], List[k+n] = List[k+n], List[k]
                p = k
                while p-n >-1: #if values swaped then go and check reverese and swap if necessary
                    if List[p] < List[p-n]:
                        List[p], List[p-n] = List[p-n], List[p]
                    p -= n
            k += 1
    return List

print(shellSort([4,8,6,7,4352,232,-454,23.54,12.1,-56.8,9,7,-56.9,-56.8]))
