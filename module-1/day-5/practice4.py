def func(intervals, newInterval):
    result = []
    # flag to insert new/merged interval
    inserted = False
    
    # check each interval
    for interval in intervals:
        # add interval if old upper bound is smaller than new lower bound
        if interval[1] < newInterval[0]:
            result.append(interval)
        # add interval if old lower bound is greater than new upper bound
        elif interval[0] > newInterval[1]:
            # add merged interval if not yet inserted for sorted result
            if not inserted:
                result.append(newInterval)
                inserted = True
            result.append(interval)
        # otherwise, replace new interval by:
        # new lower bound = minimum between old and new lower bound
        # new upper bound = maximum between old and new upper bound
        # to merge overlapping intervals
        else:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(newInterval[1], interval[1])
        #print(newInterval)
        #print(result)
        
    # add new/merged interval if not yet inserted
    if not inserted:
        result.append(newInterval)

    return result

if __name__ == '__main__':
    l1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]] 
    l2 = [4, 8]
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")
    
    result = func(l1, l2)
    print(f"result = {result}")
    print()
    
    l1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]] 
    l2 = [9, 15]
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")

    result = func(l1,l2)
    print(f"result = {result}")
    print()

    l1 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]] 
    l2 = [20, 23]
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")

    result = func(l1,l2)
    print(f"result = {result}")