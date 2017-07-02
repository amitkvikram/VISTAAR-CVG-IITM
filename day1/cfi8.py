#!/usr/bin/python3
if __name__ == '__main__':
    class Rectangle:

        def __init__(self, length, width):
            self.length=length
            self.width=width

        def area(self):
            return self.length* self.width

    len= int(input("Enter length of Rectangle: "))
    wid= int(input("Enter width of Rectangle: "))
    rect= Rectangle(len, wid)
    print(rect.area())
