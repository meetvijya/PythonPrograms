#Transpose of Matrix

m = int( input("enter no of rows: "))
n =  int(input("enter no of cols:"))
lst= []
lst2 =[]
output =[]
for i in range(m):
    for j in range(n):
        a = int(input())        
        lst2.append(a)
    lst.insert(i,lst2)
    lst2=[]
  
for row in lst:
    print(row)

for i in range(n):
    for j in range(m):
       # print(i,j)
        lst2.append(lst[j][i])
    #print(lst2)
    output.insert(i,lst2)
    lst2=[]
for row in output:
    print(row)


#***  Single line ***
##m = [[1,2,3],[4,5,6]] 
##for row in m : 
##    print(row) 
##rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
##print("\n") 
##for row in rez: 
##    print(row) 


#*** Using NumPy (install numpy)***
##import numpy
##
##print(numpy.Transpose(lst))


#*** Using zip***

##output = zip(*lst)
##for row in output:
##    print(row)

