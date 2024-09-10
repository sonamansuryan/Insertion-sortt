def insertion_sort(arr):
   for i in range(1,len(arr)):
       key=arr[i]
       j=i-1

       while j>=0 and arr[j]>key:
          arr[j+1]=arr[j]
          j=j-1

       arr[j+1]=key

user_input=input("Enter the array:")
arr=[int(x) for x in user_input.split(",")]

insertion_sort(arr)
print("Sorted array:",arr)
