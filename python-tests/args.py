#!/usr/bin/python3
# def subtract(*, x, y):
# 	"""Return the subtraction of passed args"""
# 	r = x - y
# 	return r

# print(subtract(2, 3)) # positional arguments yields error

# def combine_args(positional_arg, /, regular_arg, *, keyword_arg):
# 	"""Print passed arguments"""
# 	print(positional_arg, regular_arg, keyword_arg)
	
# combine_args('positional', 'regular', keyword_arg='keyword_arg')

# def var_args(*args):
# 	for i in args:
# 		print(i)

# x = ('Foo', 'Bar')
# y = ('Baz')
# #var_args(x)
# #var_args(y, x)
# print(x)

# def var_args(*args):
# 	for i in args:
# 		print(i)

# x = ('a', 'b')
# y = ('c', 'd')
# var_args(y, x)

# def product(*args, sci = False):
#     """Return multiplication of args.
    
#     Keyword arguments:
#     sci -- scientific notation (default False)
#     """
#     x = 1
#     for i in args:
#     	x *= i
#     if sci == True:
#         print(f"{x:e}")
#     else:
#         print(x)

# product(0.2, 0.3)
# product(0.2, 0.3, sci = True)
# product(0.2, 0.3, 0.5)
# product(0.2, 0.3, 0.5, sci = True)

# def keyword_args(**kwargs):
#     """Print keyword and values passed"""
#     for keyword, value in kwargs.items():
#         print(f"{keyword}: {value}")
 
# keyword_args(foo = 'foo', bar = 'bar')
# keyword_args(foo = 'foo', bar = 'bar', baz = 'baz')

def hello_names(arg0, *args, sep = ", "):
    s = f"Hello {arg0}"
    

hello_names("Alice")
hello_names("Alice", "Bob", "Charlie")