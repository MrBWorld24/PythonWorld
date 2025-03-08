inputs=[1,2,4,3,2.5,]
print(inputs)

inputs.insert(3,23)
print(inputs)

inputs.append("tis")
print(inputs)

inputs.remove(4) #removes first occurance
print(inputs)

inputs.pop() #if no parameter, then removes the last value
inputs.pop(2)
print(inputs)

inputs.reverse()
print(inputs)

inputs.sort()
print(inputs)