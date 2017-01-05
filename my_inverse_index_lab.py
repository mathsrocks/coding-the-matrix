# inverse index lab
## 1 Using existing modules
import math
help(math)

### Python represents nonintegral real numbers with limited precision, and the following is only approximate.
math.sqrt(3)**2
math.sqrt(-1)
math.cos(math.pi)
math.log(math.e)

from random import randint
randint(0, 10)
randint(3, 999)
randint(-99, 99.1)

## 2 Creating own modules
from dictutil import dict2list
from dictutil impoort list2dict

### 2.1 Reloading
#### It is useful when debugging our own module to be able to edit it and load the edited version into the current Python session. Python provides the procedure reload(module) in the module imp. Note if a specific definition is imported using the from ... import ... syntax, it cannot be reloaded.
L = ['A', 'B', 'C']

## 3 Loops and conditional statements
### Comprehensions are not the only way to loop over elements of a set, list, dictionary, tuple, range, or zip. Loop structures (e.g. for-loops, while-loops and etc) and contional statements (usually if)in Python all use semi-colon to separate the binding and execution parts.

## 4 Grouping in Python using identation
### Python uses indentation to indicate grouping of statements. All the statements forming a block should be indented the same number of spaces. Statements at the top level should have no indentation. The group of statements forming the body of a control statement should be indented more than the control statement.

def quadratic(a, b, c):
    discriminant = math.sqrt(b*b-4*a*c)
    return ((-b+discriminant)/(2*a), (-b-discriminant)/(2*a))

def print_greater_quadratic(L):
    for a, b, c in L:
        plus, minus = quadratic(a, b, c)
        if plus > minus:
            print(plus)
        else
            print(minus)

## 5 Breaking out of a loop
### When Python executes the break statement, the loop execution is terminated, and execution continues immediately after the innermost nested loop containing the statement.
s = "There is no spoon."
for i in range(len(s)):
    if s[i] == 'n':
        break
i

## 6 enumerate
### Often one wants to iterate through the elements of a list while keeping track of the indices of the elements. Python provides enumerate(L) for this purpose.
list(enumerate(['A', 'B', 'C']))
[i*x for (i, x) in enumerate([10, 20, 30, 40, 50])]
[i*s for (i, s) in enumerate(['A', 'B', 'C', 'D', 'E'])]
for (i, s) in enumerate(['A', 'B', 'C']):
    print(i, s)

## 7 Reading from a file
### In Python, a file object is used to refer to and access a file.
f = open('stories_big.txt')
for line in f:
    print(line)

f = open('stories_small.txt')
stories = list(f) # list() obtains a list of lines in the file
len(stories)

## Mini-search engine
mystr = 'Ask not what you can do for your country .'
mystr.split()
