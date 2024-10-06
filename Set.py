thisset = set(("apple", "banana", "cherry"))
print(thisset)


thisset.update("a", "b")
print(thisset)


thisset.discard("c")
print(thisset)
##thisset.remove("c")  # Will raise error if c not present in set
##print(thisset)
