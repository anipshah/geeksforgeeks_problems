# this is the problem of sorted list with rotation and find the key element
# I assumed that there is no repeated element
def findelement(a, lower, higher, key):
    # check condition if a exit or not
    if a:
        # if key available in list then print position otherwise it's return None
        if lower > higher:
            return None
        mid = (lower+higher)//2
        if a[mid] == key:
            return mid

        if a[lower]<=a[mid]:
            if key <= a[mid] and key >=a[lower]:
                return findelement(a,lower,mid-1,key)
            return findelement(a,mid+1,higher,key)
        if key >= a[mid] and key <= a[higher]:
            return findelement(a,mid+1,higher,key)
        return findelement(a,lower,mid-1,key)


arr = [3, 4, 5, 1, 2]
key = 3
element = findelement(arr, 0, len(arr)-1, key)
if element is not None:
    print("Element at: "+str(element+1))
else:
    print("Not Found")
