# Ex14: removing duplicates from lists

def dup_rmv_loop(a_list):
    newList = []
    for x in a_list:
        if x not in newList:
            newList.append(x)
    return newList

def dup_rmv_set(a_list):
    return list(set(a_list))

a = [1,1,2,3,4,4,5,6]
print(a)
print(dup_rmv_loop(a))
print(dup_rmv_set(a))
