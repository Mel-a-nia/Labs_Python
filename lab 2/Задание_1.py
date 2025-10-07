def min_max(nums: list [float | int])-> tuple [float | int, float | int]:
    if not nums: 
        raise ValueError ("пустой список")
    return(min(nums), max(nums))
def unique_sorted (nums:list [float | int])-> list [float | int]:
    return sorted(set(nums))
def flatten(mat:list[list | tuple])-> list:
    result=[]
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("строка не является ни списком, ни кортежем")
        result.extend(row)
        return result 
    print(min_max([3, -1, 5, 5, 0]))
    print(unique_sorted([3, 1, 2, 1, 3]))
    print(flatten([[1, 2], [3, 4]]))