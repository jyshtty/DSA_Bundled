# def deco(func):
#     def inner_func():
#         print("start time")
#         func()
#         print("end time")
#     return inner_func


# @deco
# def foo():
#     print("JP Morgan")

# foo()

def foo(li, l2):
    ans = []
    i = 0
    j = 0

    while (i<len(l1) and j <len(l2)):
        if l1[i] <= l2[j]:
            ans.append(l1[i])
            i += 1
        else:
            ans.append(l2[j])
            j += 1
    
    if len(l1) > len(l2):
        ans = ans + l1[len(l2):]
    else:
        ans = ans + l2[len(l1):]

    if i < j:
        ans = ans + l1[i:]
    else:
        ans = ans + l2[j:]

    return ans

l1 = [1,2,3,4]
l2 = [6,7,8,9]
print(foo(l1, l2))


# with file.txt as f:
#     a = f.read()
#     count = 0
#     for i in a:
#         if i == ' ':
#             count += 1
#     print(count + 1)

    
