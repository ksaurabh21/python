def mergesort( aList ):
  return _mergesort( aList, 0, len( aList ) - 1)

def _mergesort( aList, first, last ):
  # break problem into smaller structurally identical pieces
  mid = ( first + last ) / 2
  if first >= last:
    return 0 #returning 0 inversions for base case
  inv1=  _mergesort( aList, first, mid )
  inv2=  _mergesort( aList, mid + 1, last )
  #when the above _mergesort calls return, the list from index 'first' to 'mid' are in a sorted order. List entries from 'mid+1' to 'last' index are also in sorted  order 
  inv=inv1+inv2
  # merge solved pieces to get solution to original problem
  a, f, l = 0, first, mid + 1
  tmp = [None] * ( last - first + 1 )
 
  while f <= mid and l <= last:
    if aList[f] <= aList[l] :
      tmp[a] = aList[f]
      f += 1
    else:
      tmp[a] = aList[l]
      inv = inv+((mid+1)-f)
      l += 1
    a += 1
 
  if f <= mid :
    tmp[a:] = aList[f:mid + 1]
 
  if l <= last:
    tmp[a:] = aList[l:last + 1]
 
  a = 0
  while first <= last:
    aList[first] = tmp[a]
    first += 1
    a += 1
  return inv

#A = [3,2,1]
#print mergesort(A)
#print A
