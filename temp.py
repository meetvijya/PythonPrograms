print("*****String********")

str1 = "Welcome"
str2 = " to Edureka's Python Programming Blog"
str3 = str1 + str2
print('str3 is',str3)
print(str3[0:10])
print(str3[-5:])
print(str3[:-5])

print("*****List********")

countries = ['India', 'Australia', 'United States', 'Canada', 'Singapore']
print(len(countries))
print(countries)
countries.append('Brazil')
print(countries)
countries.insert(2, 'United Kingdom')
print(countries)


print("*****Tuples********")

sports_tuple = ('Cricket', 'Basketball', 'Football')
sports_list = list(sports_tuple)
sports_list.append('Baseball')
print(sports_list)
print(sports_tuple)


print("****** Comprehension List******")

# Python program to demonstrate list comprehension in Python  
  
# below list contains square of all odd numbers from 
# range 1 to 10 
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1] 
print(odd_square )

print("****** Power of 2  list******")
# below list contains power of 2 from 1 to 8 
power_of_2 = [2 ** x for x in range(1, 9)]
print( power_of_2 )
print("*********Prime numbers*******")
# below list contains prime and non-prime in range 1 to 50 
noprimes = [i for i in range(2, 50) for j in range(2, 50) if (i != j and i % j == 0)]
#noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]

print(noprimes)
print(primes)
##isprime = True
##for i in range(2,50):
##    for j in range(2,50):
##        if (i!=j) and i % j == 0:
##            isprime = False
##            break
##    if(isprime == True):    
##        primes.append(i)
##    isprime = True    
##print(primes)
            
            

# list which extracts number 
string = "my phone number is : 11122 !!"
  
print("\nExtracted digits") 
numbers = [x for x in string if x.isdigit()] 
print( numbers )
  
# A list of list for multiplication table 
a = 5
table = [[a, b, a * b] for b in range(1, 11)] 
  
print("\nMultiplication Table") 
for i in table: 
    print( i)

print("*************** Slicing ******")

    
# Let us first create a list to demonstrate slicing 
# lst contains all number from 1 to 10 
lst = range(1, 11) 
print( lst )

#  below list has numbers from 2 to 5 
lst1_5 = lst[1 : 5] 
print( lst1_5 )
  
#  below list has numbers from 6 to 8 
lst5_8 = lst[5 : 8] 
print (lst5_8 )
  
#  below list has numbers from 2 to 10 
lst1_ = lst[1 : ] 
print( lst1_ )
  
#  below list has numbers from 1 to 5 
lst_5 = lst[: 5] 
print( lst_5) 
  
#  below list has numbers from 2 to 8 in step 2 
lst1_8_2 = lst[1 : 8 : 2] 
print( lst1_8_2 )
  
#  below list has numbers from 10 to 1 
lst_rev = lst[ : : -1] 
print( lst_rev )
  
#  below list has numbers from 10 to 6 in step 2 
lst_rev_9_5_2 = lst[9 : 4 : -2] 
print( lst_rev_9_5_2)


print("*** Tuple ***")
list1 = [0, 1, 2] 
print(tuple(list1)) 
print(tuple('python')) # string 'python'

  

L1 = [1, 2, 3, 4]
L2 = L1
L3 = L1.copy()
L4 = list(L1)
L1[0] = [5]
print(L1, L2, L3, L4)

# output of below code 
import sys
L1 = tuple()
print(sys.getsizeof(L1), end = " ")
L1 = (2)
print(sys.getsizeof(L1), end = " ")
L1 = (1, 2)
print(sys.getsizeof(L1), end = " ")
L1 = (1, 3, (4, 5))
print(sys.getsizeof(L1), end = " ")
L1 = (1, 2,3,4)
print(sys.getsizeof(L1), end = " ")
L1 = (1, 2, 3, 4, 5, [3, 4], 'p', '8', 9.777, (1, 3))
print(sys.getsizeof(L1))

# output of below code 
L = [1, 3, 5, 7, 9]
print(L.pop(-3), end = ' ')
print(L.remove(L[0]), end = ' ')
print(L)

# output of below code 
L = list('123456')
L[0] = L[5] = 0
L[3] = L[-2]
print(L)


T = tuple('geeks')
a, b, c, d, e = T
b = c = '*'
T = (a, b, c, d, e)
print((a, b, c, d, e))

print(" *** output of below code ***")
L = [2e-04, 'a', False, 87]
T = [6.22, 'boy', True, 554]
for i in range(len(L)):
    if L[i]:
        L[i] = L[i] + T[i]
    else:
        T[i] = L[i] + T[i]
        break
print(L)

##print(" *** output is Value type ***")
##L = [3, 1, 2, 4]
##T = ('A', 'b', 'c', 'd')
##L.sort()
##counter = 0
##for x in T:
##    L[counter] += int(x)
##    counter += 1
##    break
##print(L)
##
##
##
##tuple = (1, 2, 3, 4)
##tuple.append( (5, 6, 7) )
##print(len(my_tuple))

tuple = {}
tuple[(1,2,4)] = 8
tuple[(4,2,1)] = 10
tuple[(1,2)] = 12
_sum = 0
for k in tuple:
    _sum += tuple[k]
print(len(tuple) + _sum)


def MaxOnes(input):
    result = list(map(sum,input))
    return result.index(max(result))

if __name__ == "__main__":
   input = [[0,0,0,0],[0,0,0,1],[0,0,1,1],[1,1,1,1],[0,1,1,1]]
   print("row index is:",MaxOnes(input))


print("**** Set***")
people = {"Jay", "Idrish", "Archil"}
people.add("Daxit") 
print(people)

print(" union of set")
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
population = people.union(vampires)
print(population)

safe = people.difference(vampires)
print(safe)

print(" *** Array ***")

import array

arr= array.array('i',[1,2,3])

for i in range(len(arr)):
    print( arr[i])
arr.append(4)
for i in range(len(arr)):
    print( arr[i])
arr.insert(2,5)
for i in range(len(arr)):
    print( arr[i])
arr.pop()


arr.append(4)

arr.pop(2)

for i in range(len(arr)):
    print( arr[i])
print(arr.typecode)
print(arr.itemsize)
print(arr.buffer_info())

