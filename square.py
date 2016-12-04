arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 32, 4, 32, 2, 34, 4, 3, 43, 43,2 ,2 ,34 ,43 ,2, 34, 43, 2, 34, 43,24,3, 24, 32, 3, 21 ,64, 6,5, 5,3 ]

def square(arr):
    res = []
    if not arr or sum(arr)%4 != 0 : return res
    bian = sum(arr)/4
    arr = sorted(arr, reverse=True)

    def helper(arr, level, cur, length, tem_res, res):
        if arr == [] and level == 4 and sum(cur) == length:
            tem_res.append(cur)
            res.append(tem_res)
            return True 
        tmp_level = level
        if sum(cur) == length and level != 4:
            tem_res.append(cur)
            cur = []
            tmp_level += 1
    
        for i in xrange(len(arr)):
            if arr[i] + sum(cur) > length:
                continue
            else:
                if helper(arr[:i]+arr[i+1:], tmp_level, cur+[arr[i]],length, tem_res, res):
                    return res

    res = helper(arr, 1, [], bian, [], [])
    print res

square(arr)
