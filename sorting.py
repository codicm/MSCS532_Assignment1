def sort_descending(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        z = i - 1
        
        while z >= 0 and arr[z] < key:
            arr[z + 1] = arr[z]
            z -= 1
        arr[z + 1] = key
    return arr



if __name__ == "__main__":
    data = [8, 3, 7, 1, 5]
    print("Original array:", data)
    sorted_data = sort_descending(data)
    print("Sorted array (Descending):", sorted_data)