# SECTION 1.1: GETTING STARTED

"""
Python 2 has a number of functionalities that can be optionally imported from Python 3 using the __future__
module, as discussed here.

P: 4
"""

from __future__ import print_function

# ----------------------------------------------------------------------------

# SECTION 1.2: CREATING VARIABLES AND ASSIGNING VALUES

"""
You can not use python's keywords as a valid variable name. You can see the list of keyword by:
P: 7
"""

import keyword
print(keyword.kwlist)

"""
You can assign multiple values to multiple variables in one line. Note that there must be the same number of arguments on the right and left sides of the = operator:

--

You can also assign a single value to several variables simultaneously.

p: 8
"""

a, b, c = 1, 2, 3

a = b = c = 1

"""
Things are a bit different when it comes to modifying the object (in contrast to assigning the name to a different object, which we did above) when the cascading assignment is used for mutable types. Take a look below, and you will see it first hand:

P: 9
"""


x = y = [7, 8, 9]
x[0] = 13
print(y) # Output: [13, 8, 9]

"""
Python 3 disallows mixing the use of tabs and spaces for indentation. In such case a compile-time error is generated: Inconsistent use of tabs and spaces in indentation and the program will not run.
P: 10
"""

# ----------------------------------------------------------------------------

# SECTION 1.4: Datatypes

"""
In Python 2.x and in Python 3.x, a boolean is also an int. The bool type is a subclass of the int type and True and False are its only instances:
"""


