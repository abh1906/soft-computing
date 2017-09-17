import random
def mutate(array,n):
  k=random.randint(0,20)
  
  for i in range(n):
     a=list(array[i])
     if(a[k]=='0'):
       a[k]='1'
     else:
       a[k]='0'
     array[i]=''.join(a)
  return array
     
def crossover(a,b,k,array):
   aa=list(a)
   bb=list(b)
   
   for i in range(k):
      aa[i], bb[i]=bb[i], aa[i]
      a=''.join(aa)
      b=''.join(bb)
   return array
def cal_fitness(a):
  s=a.count('1')
  return s
   
  
def fit_sort(array):
  for i in range(len(array)):
    for j in range(len(array)-1):
      if(cal_fitness(array[j])<cal_fitness(array[j+1])):
           temp=array[j]
           array[j]=array[j+1]
           array[j+1]=temp
	   
  return array

  
 
def decToBin(n):
    if(n==0): 
        return ''
    else:
        return decToBin(n//2) + str(n%2)


       
#population size=50
#no.of generation=30
#cross prob=80
#mp=10
#reprod=10


random_array=[]
reprod_array=[]
cross_over=[]
mut_array=[]
for i in range(50):
  k=random.randint(0,2**32-1)
  n=decToBin(k)
  q=32-len(n)
  s=''
  for i in range(q):
       s=s+'0'
  n=s+n
  random_array.append(n)
  
#print(fit_sort(random_array))
random_array = fit_sort(random_array)

maxx=0
for i in range(30):
    print("Generation:"+str(i))
    print()
    print(random_array)
    if(maxx < cal_fitness(random_array[0])):
       maxx=cal_fitness(random_array[0])
    for j in range(5):
      reprod_array.append(random_array[j])
    mut_array=random_array[5:10]
    
    cross_over=random_array[10:50]
    for k in range(len(cross_over)-1):
     cross_over=crossover(cross_over[k],cross_over[k+1],3,cross_over)
    mut_array=mutate(mut_array,len(mut_array))
    
    random_array=[]
    random_array=mut_array+cross_over+reprod_array  
    random_array=fit_sort(random_array)
print()
print("ANS:"+str(maxx))
     
   

  
