"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <=1:
        return x
    else:
        return foo(x-1) + foo(x-2)
    pass

def longest_run(mylist, key):
    ### TODO
    maxCount = 0
    currentCount = 0
    for num in range(len(mylist)):
        if mylist[num] == key:
            currentCount += 1
            maxCount = max(maxCount, currentCount)
        else:
            currentCount = 0
    return maxCount
    


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    ### TODO
    if not mylist:
        return Result(0, 0, 0, False)
    if len(mylist) == 0:
        return Result(0, 0, 0, True)
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)
    #Divide and conquer
    mid = len(mylist) // 2
    leftRun = longest_run_recursive(mylist[:mid],key)
    rightRun = longest_run_recursive(mylist[mid:],key)
    #Merge
    left_size = leftRun.left_size
    right_size = rightRun.right_size
    if leftRun.is_entire_range:
        left_size += rightRun.right_size
    if rightRun.is_entire_range:
        right_size += leftRun.right_size
    # cross boundary
    cross_size =0
    if mylist[mid-1]==key and mylist[mid]==key:
        cross_size = leftRun.right_size + rightRun.left_size
    # longest size
    longest_size = max(leftRun.longest_size, rightRun.longest_size, cross_size)
    # check key for enitre range
    is_entire_range = leftRun.is_entire_range and rightRun.is_entire_range
    return Result(left_size, right_size, longest_size, is_entire_range)
        
        
    
    
    
    



