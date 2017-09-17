fitness=[5,10,15,25,50,100]
probability={}
expected_count={}
actual_count={}
for i in range(6):
  probability[fitness[i]]=fitness[i]/sum(fitness)

avg=sum(fitness)/6
for i in range(6):
  expected_count[fitness[i]]=fitness[i]/avg
for i in range(6):
  actual_count[fitness[i]]=int(round(expected_count[fitness[i]]))

print("fitness: initial_actual_count")
print()
print(actual_count)
print()
count=0
for i in actual_count:
   count=count+actual_count[i]

while(count<=6):
 key=max(actual_count, key=actual_count.get)
 actual_count[key]+=1
 count+=1

print("fitness : probability")
print()
print(probability)

print()
print("fitness : expected count")
print()
print(expected_count)
print()

print("fitness : final_actual_count")
print()
print(actual_count)
