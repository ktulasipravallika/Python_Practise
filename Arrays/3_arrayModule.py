import array

arr= array.array('i', [1,2,3,4,5,6,7,8])

print("Initial Array: ", arr)
arr.append(10)
arr.append(11)
arr.pop()
arr.insert(3,89)
arr.remove(7)
print("Modified Array: ", arr)

