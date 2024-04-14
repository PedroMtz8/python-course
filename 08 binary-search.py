
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) # 4

print(result) # 4


def binary_search_recursive(arr, target):
    left, right = 0, len(arr) - 1
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    
result = binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) # 4
print(result) # 4


