def bubbleSort(List):
    if List == []:
        return List
    else:
        n = len(List)
        while n > 1:
            n -= 1
            for i in range(n):
                if List[i]>List[i+1]:
                    List[i],List[i+1] = List[i+1],List[i]
        return List
         
print(bubbleSort([4,8,6,7,4352,232,-454,23.54,12.1,-56.8,9,7,-56.9,-56.8]))





# def bubbleSort(List):
#     comparisons = 0
#     isSorted = False
#     if List == []:
#         return List
#     else:
#         while isSorted == False:
#             isSorted = True
#             for i in range(len(List)-1):
#                 if List[i]>List[i+1]:
#                     List[i],List[i+1] = List[i+1],List[i]
#                 comparisons +=1
#                 if i != 0:
#                     if List[i-1]>List[i]:
#                         isSorted = False
#         print(comparisons)
#         return List

# print(bubbleSort([4,8,6,7,4352,232,-454,23.54,12.1,-56.8,9,7,-56.9,-56.8]))
# print(bubbleSort([5,4,1]))
