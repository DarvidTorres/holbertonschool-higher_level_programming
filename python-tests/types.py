#!/usr/bin/python3
#print(type("Hello World"))
#print(type(20))
#print(type(20.5))
#print(type(1j))
#print(type(["apple", "banana", "cherry"]))
#print(type(("apple", "banana", "cherry")))
#print(type(range(6)))
#print(type({"name" : "John", "age" : 36}))
#print(type({"apple", "banana", "cherry"}))
#print(type(frozenset({"apple", "banana", "cherry"})))
#print(type(True))
#print(type(b"Hello"))
#print(type(bytearray(5)))
#print(type(memoryview(bytes(5))))
#print(type(None))

#print(type(c := True))
#print(type(b := 10.5))
#print(type(c + b))

#'12' + 13

#print(type(a := "10.5"))
#print(type(int(a)))
#
#print(type(b := "100"))
#print(type(int(b))) #converts a string object to int

a=[1,2,3,4,5]   # List Object
b=(1,2,3,4,5)   # Tupple Object
c="Hello"       # String Object

### list() separates each character in the string and builds the list
obj=list(c)
print(obj)

### The parentheses of tuple are replaced by square brackets
obj=list(b)
print(obj)

### tuple() separates each character from string and builds a tuple of characters
obj=tuple(c)
print(obj)

### square brackets of list are replaced by parentheses.
obj=tuple(a)
print(obj)

### str() function puts the list and tuple inside the quote symbols.
obj=str(a)
print(obj)

obj=str(b)
print(obj)