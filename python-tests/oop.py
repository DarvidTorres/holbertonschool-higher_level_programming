#!/usr/bin/python3
class MyClass:
    """
    A class that stores a single value and provides a method to display it.

    Attributes
    ----------
    attr : any type
        The value to be stored in the instance.

    Methods
    -------
    show_value()
        Prints the stored value to the console.
    """

    def __init__(self, value):
        self.attr = value

    def show_value(self):
        print(self.attr)

# Creating an instance of MyClass and calling show_value
my_obj = MyClass('Value')

my_obj.show_value()  # Calling the method attribute 'show_value'
