# Finger exercise: Why does the code use mid+1 rather than mid in
# the second recursive call?

def search(L, e):
    """Assumes L is a list, the elements of which are in
       ascending order
       Returns True if e is in L and False otherwise"""
    
    def bin_search(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (high + low) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                # Nothing else to search
                return False
            else:
                return bin_search(L, e, low, mid-1)
        else:
            return bin_search(L, e, mid+1, high)
        
    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)
    
# We have already checked L[mid] and so we can start the next 
# level of recursion with the element to the right of the midpoint