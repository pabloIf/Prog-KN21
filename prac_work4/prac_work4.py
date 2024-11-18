def binary_search(lst, value):
    first = 0
    last = len(lst) - 1
    while first <= last:
        mid = (first + last) // 2
        mid_value = lst[mid]
        if mid_value == value:
            return mid
        elif mid_value < value:
            first = mid + 1
        else:
            last = mid - 1
    

nums = [1,2,3,4,9,11,17,22,32,81]
my_value = 17
res = binary_search(nums, my_value)
print(res)