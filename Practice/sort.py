sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
def binary_search(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
print(f"List is {sorted_list}")
print(f"Searching for 12: {binary_search(sorted_list, 12)}")

def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j + 1], arr[j] 
                swapped = True
            if not swapped:
                break
print("\n--- Bubble Sort ---")
list=[21,1,12,45]
bubble_sort(list)
