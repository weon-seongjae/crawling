# Classes Documentation : https://docs.python.org/3/tutorial/classes.html

import sys
import io


class SelfTest():
    def function1():
        print('function1 called!')

    def function2(self):
        print(id(self))
        print('function2 called!')

f = SelfTest()
print(dir(f))
# f.function1()
f.function2()
print(id(f))
print(SelfTest.function1())