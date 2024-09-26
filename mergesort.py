def mergesort(list):
    head= 0 
    rear = len(list) -1
    tmp = [None] * len(list)
    mergesort_aux(list,head,rear,tmp)
    
def mergesort_aux(list,head,rear,tmp):
    mid = ( head + rear) //2
    if head != rear:
        mergesort_aux(list,head,mid,tmp) 
        mergesort_aux(list,mid+1,rear,tmp)
        #we need to now push them to a new list 
        #note we do not actually have two lists, so we are still purely merging based on two indexes
        merge(list,head,mid,rear,tmp)
        for i in range(head, rear + 1):
            list[i] = tmp[i] # we are allocaitng directly to tmp so its ok, tmp is an exact copy 
    print(list)

def merge(list,head,mid,rear,tmp):
    ia= head
    ib = mid+1 #make sure mid _1
    for k in range(head,rear+1): # initally was right
        if ia > mid:
            tmp[k] = (list[ib])
            ib+=1
        elif ib > rear:
            tmp[k] = (list[ia])
            ia+=1
        elif list[ia] <= list[ib]:
            tmp[k] = (list[ia])
            ia += 1
        else:
            tmp[k] = (list[ib])
            ib+=1
    return tmp 
    
list1= [1,2,3,4,5,4,3,2,5,12,5,321]
mergesort(list1)