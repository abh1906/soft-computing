#1 2 3 4 5 6 7
#weight:7 8 4 10 4 6 4
#benefit:5 8 3 2 7 9 4
#population-size=10
#chromosome-size=7
#pc=80
#pm=20
import random
weight={0:7,1:8,2:4,3:10,4:4,5:6,6:4}
benefit={0:5,1:8,2:3,3:2,4:7,5:9,6:4}

def mutate(array,n):
  k=random.randint(0,6)
  
  for i in range(n):
     a=list(array[i])
     if(a[k]=='0'):
       a[k]='1'
     else:
       a[k]='0'
    
     x=''.join(a)
     if(cal_weight(x,weight)==True):
      array[i]=x
  return array

def generate_random(weight):
  array=[]
  count=0
  while(count<=10):
     n=random.randint(1,2**7-1)
     n=decToBin(n) 
     k=7-len(n)
     s=''
     for i in range(k):
       s=s+'0'
     n=s+n
     if(cal_weight(n,weight)==True):
      array.append(n)
      count+=1
  return array


def cal_weight(a,weight):
  aa=list(a)
  sum=0
  for i in range(7):
    if(aa[i]=='1'):
       sum=sum+weight[i]
  if(sum<=24):
    return True
  else:
    return False

def cal_fitness(a,benefit):
  aa=list(a)
  sum=0
  for i in range(7):
     if(aa[i]=='1'):
        sum=sum+benefit[i]
  return sum

def cross_over(a,b,k,array):
  
   aa=list(array[a])
   bb=list(array[b])
   
   for i in range(k):
      aa[i], bb[i]=bb[i], aa[i]
   ap=''.join(aa)
   aq=''.join(bb)
      if(cal_weight(ap,weight)==True and cal_weight(aq,weight)==True):
        array[a]=ap
        array[b]=aq
   return array

def fit_sort(array):
  for i in range(len(array)):
    for j in range(len(array)-1):
      if(cal_fitness(array[j],benefit)<cal_fitness(array[j+1],benefit)):
           temp=array[j]
           array[j]=array[j+1]
           array[j+1]=temp
	   
  return array



def decToBin(n):
    if(n==0): 
        return ''
    else:
        return decToBin(n//2) + str(n%2)


random_array=generate_random(weight)
random_array=fit_sort(random_array)
maxx=0

crossover=[]
mut_array=[]
for i in range(10):
  if(maxx < cal_fitness(random_array[i],benefit)):
     maxx=cal_fitness(random_array[i],benefit)
  mut_array.append(random_array[0])
  mut_array.append(random_array[1])
  print("Generation"+str(i+1))
  print()
  print(random_array)
  
  crossover=random_array[2:10]
  mut_array=mutate(mut_array,len(mut_array))
  for k in range(0,len(crossover)-1,2):
     crossover=cross_over(k,k+1,3,crossover)
  random_array=mut_array+crossover   
  random_array=fit_sort(random_array)
print()
print("ANS"+" "+str(maxx))
