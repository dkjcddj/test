def check(r1, o):
    d = {}
    for num in r1:
        d[num] = d.get(num,0) + 1
        diff = o - num
        if d.get(diff) == None:
            continue    
        if diff == num and d.get(diff) > 1: # if mulitiple num is required
            return True
        elif diff != num and d.get(diff) > 0:
            return True
    return False

print(check([1,3,5,7,9,11,13,15], 24))
print(check([1,3,5,7], 5))
print(check([1,3,5,7], 6))
print(check([12,13,15], 24))
print(check([12,13,12], 24))
