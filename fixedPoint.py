# Find a Fixed Point (Value equal to index) in a given array
"""
 Input: arr[] = {-10, -5, 0, 3, 7}
  Output: 3  // arr[3] == 3

  Input: arr[] = {0, 2, 5, 8, 17}
  Output: 0  // arr[0] == 0


  Input: arr[] = {-10, -5, 3, 4, 7, 9}
  Output: -1  // No Fixed Point
"""
def fixes_point(arr):
    f=False
    for i in range(0, len(arr)-1):
        if arr[i] == i:
            print(i)
            f = True
            
    if f == False:
        print("Not found")
        
ar=[10,4,8,7,0]
fixes_point(ar)
