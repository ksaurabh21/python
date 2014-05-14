def quicksort(aList):
    _quicksort(aList,0,len(aList)-1)
    
def _quicksort(aList,first, last):
    if first<last:
        q = partition(aList, first, last)
        #print "partition location:=", q, " ",aList
        _quicksort(aList, first, q-1)
        _quicksort(aList,q+1,last)
        
def partition(aList, first, last):
    pivot = aList[last]
    i = first
    j = first
    while j < last: #after this loop is over, all numbers from index 'i' till 'last-1' are greater than pivot
        if aList[j] <= pivot:
            aList[i],aList[j] = aList[j],aList[i]
            i=i+1
        j=j+1
    aList[i],aList[last] = aList[last],aList[i] #putting the pivot at index i. Now all elements to the left of the pivot are smaller or equal and all to the right are greater than the pivot
    return i


#A = [3,2,1]
#quicksort(A)
#print A
