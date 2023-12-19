#iterative approach
def sequentialSearch1(List,item):
    isIn = False
    for i in range(len(List)):
        if List[i] == item:
            isIn = True
            index = i
            break
    
    if isIn ==True:
        return index
    else:
        return "Does not exist"

List = [2,4,6,2,5,3,56,2,2,-43,23,23,55]
print(sequentialSearch1(List,55))



#recursive approach
def sequentialSearch2(List,item, n=0):
    if item == List[0]:
        return n
    elif len(List) == 1:
        return "Does not exist"
    else:
        return sequentialSearch2(List[1:],item, n+1)


List = [2,4,6,2,5,3,56,2,2,-43,23,23,55]
print(sequentialSearch2(List,2))
