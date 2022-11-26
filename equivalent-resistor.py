def check(rl, o):
    valueneeded = 0
    for i in range(len(rl)):
        if rl[i] >= o and o != 0:
            continue
        elif o == 0 and rl[i] == 0:
            continue
        else:
            valueneeded = o - rl[i]
            j = i+1
            for j in range(len(rl)):
                if valueneeded == rl[j]:
                    return True
    return False



print(check([4,5,6,2,3],13))
