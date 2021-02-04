def insertion_sort(arr):

    n_=len(arr)
    for i_ in range(1,n_):
        value = arr[i_]
        j_ = i_-1
        while j_>=0 and value<arr[j_]:
            arr[j_+1]=arr[j_]
            j_ -= 1
        arr[j_ + 1] = value

# arr = [12, 11, 13, 5, 6,-1,8,2,7] 
# insertion_sort(arr)
# print(arr)
             