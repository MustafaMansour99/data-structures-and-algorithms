from hashtable.hashtable import Hashtable
def tree_intersection(num1,num2):
    result=set()
    hash=Hashtable()
    for i in num1:
        if i in num1:
            hash.set(i)
    for i in num2:
        if i in hash:
            result.add(i)
    if num1 is None or num2 is None:
        return "Empty Trees"
    return result

num1=[1,2,3,4]
num2=[1,5,2,.4,7]
print("Tree Intersection:",tree_intersection(num1,num2))
