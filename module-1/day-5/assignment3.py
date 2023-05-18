def sumList(nums):
    result = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp = [nums[i], nums[j], nums[k]]
                    tmp.sort()
                    if tmp not in result:
                        result.append(tmp)
    return result

if __name__ == '__main__':
    nums = [-1, 0, 1, -2, -1, 2, -4]
    result = sumList(nums)
    print(result)