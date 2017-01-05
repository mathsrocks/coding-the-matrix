# 1 Lab: Introduction to Python - sets, lists, dictionaries, and comprehensions

## 1 Simple expressions
### 1.1 Arithmetic and numbers
#### Python uses a traditional programming notation for scientific notation.
#### Since Python uses limited-precision arithmetic, there are round-off errors.
6.022e23
6.626e-34
1e16+1
min(6.02e23, float('infinity'))

### 1.2 Strings
#### Python evaluates the expression. The value of a string is just the string itself.
'This sentence is false.'
"So's this one."

### 1.3 Comparisons and conditions and Booleans
5 == 4
4 == 4
type(5 == 4)
True and False
True and not (5==4)

## 2 Assignment statements
#### A variable name must start with a letter and must exlude certain special symbols such as the dot (period). The underscore _ is allowed in a variable name.
mynum = 4+1
mynum = 'Brown'

#### It is important to remember (and second nature to most experienced programmers) that an assignment statement binds a variable to the value of an expression, not to the expression itself. Python first evaluates the right-hand side and only then assigns the resulting value to the left-hand side. This is the behaviour of most programming languages.

x = 5+4
y = 2*x
y
x = 12
y

## 3 Conditional expressions
x if x > 0 else -x

## 4 Set
### Python provides some simple data structures for grouping together multiple values, and integrates them with the rest of the language. These data structures are called collections.
### A set is an unordered collection in which each value occurs at most once. Curly braces give an expression whose value is a set. 
{1+2, 3, "a"}
{2, 1, 3}

### Note that duplicates are eliminated and the order might change.

### In Python, the cardinality of a set is obtained using the procedure len().
len({'a', 'b', 'c', 'a', 'a'})

### 4.1 Summing: sum of elements of collection of values
sum({1, 2, 3})
#### sum that begins with a figure other than zero.
sum({1, 2, 3}, 10)

### 4.2 Testing set membership

### 4.3 Set union and intersection

### 4.4 Mutating a set
#### A value that can be altered is a mutable value. Sets are mutable; elements can be added and removed using the add and remove methods.
#### The dot syntax is in object-oriented fashion. The operations add() and remove() are methods.
#### Python provides a method update() to add to a set all the elements of another collection (e.g. a set or a list).
#### Suppose two variables are bound to the same value. A mutation to the value made through one variable is seen by the other variable.

### 4.5 Set comprehensions
#### Python provides expressions called comprehensions that allow us to build collections out of other collections. They mimic traditional mathematical notation.

### 4.6 Remarks
#### The empty set is represented by set(), not by {}.

## 5 Lists
### Python represents sequences of values using lists. In a list, order is significant and repeated elements are allowed. The notion for lists uses square brackets instead of curly braces. The empty list is represented by [].
### There is no restrictions on the elements of lists. However, a set cannot contain a list since lists are mutable.

### 5.1 List concatenation
#### List concatenation using overloaded + operator.
#### sum() with [] as the 2nd argument to concatenate collection of lists.

### 5.2 List comprehensions
#### We can use a comprehension over two sets to form the Cartesian product.
#### There are two ways to obtain an individual element of a list. The first is by indexing. As in some other languages (Java and C++, for example), indexing is done using square brackets around the index. 

#### Slices: A slice of a list is a new list consisting of a consecutive subsequence of elements of the old list, namely those indexed by a range of integers. The range is specified by a colon-separated pair i:j where j is the one past the index of the last element.

#### Prefixes: If the first element i of the pair is 0, it can be omitted, my[:2]. Useful for obtaining a prefix of a list.

#### Suffixes: If the second element j of the pair is the length of the list, it can be omitted.

L = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

#### Slices that skip
#### Use a colon-separated triple a:b:c if we want to slice to include every cth element. For example, even-indexed and odd-indexed elements:
L[::2]
L[1::2]

### 5.4 Obtaining elements of a list by unpacking
#### Instead of assigning a list to a single variable, we assign to a list of variables.
#### Note that this is a notational fiction. Python does not allow creating a value that is a list of variables - the assignment is simply a convenient way to assign to each of the variables.

### 5.5 Mutating a list: indexing on the left-hand side of =
#### We can mutate a list, replacing the ith element, using indexing on the left-hand side of the =, analogous to an assignment statement.

## Tuples
### Like a list, a tuple is an ordered sequence of elements. However, tuples are immutable so they can be elements of sets. Ordinary parentheses are used.

### 6.1 Obtaining elements of a tuple by indexing and unpacking
#### Indexing to obtain an element of a tuple. Use unpacking in a comprehension.

### 6.2 Obtaining a list or set from another collection
#### Python can compute a set/list/tuple from another collection (e.g. a list) using the constructor set()/list()/tuple().

## 7 Other things to iterate over
### 7.1 Tuple comprehensions - not! Generators

### 7.2 Ranges
#### A range plays the role of a list consisting of the elements of an arithmetic progression. 
#### Even though a range represents a sequence, it is not a list. Generally we will either iterate through the elements of the range or use set() or list() to turn the range into a collection.

### 7.3 Zip
#### Another collection that can be iterated over is a zip. A zip is constructed from other collection all of the same length. Each element of the zip is a tuple consisting of one element from each of the input collections.
characters = ['Neo', 'Morpheus', 'Trinity']
actors = ['Keanu', 'Laurence', 'Carrie-Anne']
set(zip(characters, actors))
[character + ' is played by ' + actor for (character, actor) in zip(characters, actors)]

### 7.4 reversed

## 8 Dictionaries
### We will often use functions with FINITE DOMAINS. Python provides collections, named dictionaries, that are suitable for representing such functions. Conceptually, a dictionary is a SET of KEY-VALUE PAIRS. In this syntax, each key-value pair is written using colon notation, i.e. key:value.
### As in sets, the order of the key-value pairs is irrelevant, and the keys must be immutable (no sets or lists or dictionaries). So the keys will mostly be integers, strings, or tuples of integers and strings.
### To each key in a dictionary there corresponds only one value (that is in accordance with the definition of a function). If a dictionary is given multiple values for the same key, only one value will be associated with that key.

### 8.1 Indexing into a dictionary
#### Obtaining the value corresponding to a particular key uses the same syntax as indexing a list or tuple: right after the dictionary, use square brackets around the key.
mydict = {'Neo':'Keanu', 'Morpheus':'Laurence', 'Trinity':'Carrie-Anne'}

### 8.2 Testing dictionary membership
#### Check whether a key is in a dictionary using the in operator as in sets.

### 8.3 Lists of dictionaries

### 8.4 Mutating a dictionary: indexing on the left-hand side of =

### 8.5 Dictionary comprehensions

### 8.6 Comprehensions that iterate over dictionaries
#### We can write list comprehensions that iterate over the keys or values of a dictionary, using keys() or values().
[k for k in {'a':1, 'b':2}.keys() | {'b':3, 'c':4}.keys()]
[k for k in {'a':1, 'b':2}.keys() & {'b':3, 'c':4}.keys()]

#### Often we will want a comprehension that iterates over the (key, value) pairs of a dictionary, using items(). Each pair is a TUPLE.
[myitem for myitem in mydict.items()]
#### Since the items are tuples, we can access the key and value separately using unpacking.
[k + " is played by " + v for (k, v) in mydict.items()]
[2*k+v for (k, v) in {4:0, 3:2, 100:1}.items()]

## 9 Defining one-line procedures
### formal argument and actual argument. Wehn the procedure is invoked, the formal argument (the variable) is temporarily bound to the actual argument, and the body of the procedure is executed. At the end, the binding of the actual argument is removed. (The binding was temporary.)
dct = {'a':'A', 'b':'B', 'c':'C'}
keylist = ['b', 'c', 'a']

L = ['A', 'B', 'C']
keylist = ['a', 'b', 'c']
