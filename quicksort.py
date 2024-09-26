def quicksort(list):
    start = 0
    end = len(list) -1 # len list -1 
    quicksort_aux(list,start,end)

    #so if we rmbr, we need a partition to sort quicksort 

def quicksort_aux(list,start,end):
    #pivot is not placed here
    #we need to use this pivot to find the partition location
    
    if start < end: 
        split = partition(list,start,end)
        quicksort_aux(list,start,split-1)
        quicksort_aux(list,split+1,end)
    print(list)

def partition(list,start,end):
    pivot= list[start]
    boundary = start # boundary is start not 0 
    for i in range(start+1,end+1): # dont check our pivot again 
        if list[i] < pivot:
            boundary +=1
            list[boundary], list[i] = list[i],list[boundary]
    list[start],list[boundary] = list[boundary],list[start] # stop using list[0]
    return boundary

list1= [1,2,3,4,5,4,3,2,5,12,5,321]
quicksort(list1)