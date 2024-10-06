#iterators example...list set, tuples are iterator example..\
#bcoz it implements __iter__ and __next__ methods

#creation  of iterator
class Test:
    def __init__(self,limit):

        .limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if(x > self.limit):
            raise StopIteration

        self.x= x+1
        return x

for x in Test(15):
    print(x)
for x in Test(5):
    print(x)
