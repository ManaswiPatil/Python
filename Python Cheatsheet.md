# Python Cheatsheet
I have created this Cheat Sheet while learning Python to remember the common syntax and as a future handy reference.
<hr>

**[`Data types`](#python-data-types)**

#### Python Data Types
1. int
2. float
3. boolean
4. string
5. **[`List`](#list)**
6. **[`Tuple`](#tuples)**
7. set
8. **[`Dictionary`](#dictionary)**

#### Arithmetic Operations
```python
print(8 + 3) = 11		<class 'int'>
print(8 - 3) = 5		<class 'int'>
print(8 * 3) = 24		<class 'int'>
print(8 / 3) = 2.66666666665	<class 'float'>
print(8 ** 3) = 512	        <class 'int'> gives power of value.
print(8 // 3) = 2		<class 'int'> returns a divider. 
print(8 % 3) = 2		<class 'int'> returns a remainder.
```

#### Operator precedence : 
```python
()    brackets
**    power of
* /   multiplication and division
+ -   addition and subtraction
```

#### Math functions:
```python
round(4.1) = 4 int
abs(-65) = 65
pow(8, 3)	returns x raised to the power y – similar to 8 ** 3
factorial(8)	returns the factorial of a number
sqrt(8)		returns square root of a number – float
```

#### Conditional statement:
```python
St = “x is greater than y” if (x>y) else “x is less than or same as y”
```

### List
store a collection of data under one variable name<br>
list can store both strings and integers<br>
List is a collection which is ordered and changeable. Allows duplicate members.<br>
lists are mutable. This means we can change an item in a list by accessing it directly as part of the assignment statement.
```python
list=[1,0.75,'rose','knife']
```
```python
fruits = ['apple','pears','orange','banana','pineapple']

```

#### List slicing
```python
fruits[0:2]		list[start-index : stop]
fruits[0::2]	list[[start-index : stop : step]
fruits[::-1]	start from the end-index of list hence reverse the list
```

#### List Methods
<b>append()</b>	Adds an element at the end of the list
```python
>>> fruits.append('strawberry')
>>> fruits
['apple', 'pears', 'orange', 'banana', 'pineapple', 'strawberry']
```

<b>insert()</b>	Adds an element at the specified position
```python
>>> fruits.insert(3,'Blueberry')
>>> fruits
['apple', 'pears', 'orange', 'Blueberry', 'banana', 'pineapple', 'strawberry']
```

<b>extend()</b>	Add the elements of a list (or any iterable), to the end of the current list
```python
>>> fruits = ['apple','pears','orange','banana','pineapple']
>>> fruits.extend(['Avacado','Mango'])
>>> fruits
['apple', 'pears', 'orange', 'banana', 'pineapple', 'Avacado', 'Mango']
```
 
<b>pop()</b>	Removes the element at the specified position
```python
>>> fruits
['apple', 'pears', 'orange', 'banana', 'pineapple', 'Avacado', 'Mango']
>>> 
>>> fruits.pop()    #removes the element from the end of the list
'Mango'
>>> fruits
['apple', 'pears', 'orange', 'banana', 'pineapple', 'Avacado']
>>> fruits.pop(2)   #removes the element from specified index
'orange'
>>> fruits
['apple', 'pears', 'banana', 'pineapple', 'Avacado']
```

<b>remove()</b>	Removes the first item with the specified value
```python
>>> fruits = ['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> fruits.remove('banana')
>>> fruits
['apple', 'pears', 'pineapple', 'Avacado']
```

<b>clear()</b>	Removes all the elements from the list
```python
>>> fruits.clear()
>>> fruits
[]
```

<b>index()</b>	Returns the index of the first element with the specified value
```python
>>> fruits = ['apple','mango', 'pears', 'banana', 'pineapple', 'Avacado','mango']
>>> fruits.index('mango')
1
```

<b>count()</b>	Returns the number of elements with the specified value
```python
>>> fruits = ['apple','mango', 'pears', 'banana', 'pineapple', 'Avacado','mango']
>>> fruits.count('mango')
2
>>> fruits.count('Avacado')
1
```

<b>sort()</b>	Sorts the list
```python
>>> fruits = ['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> fruits.sort()
>>> fruits
['Avacado', 'apple', 'banana', 'pears', 'pineapple']
```

<b>copy()</b>	Returns a copy of the list
```python
>>> fruits = ['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> basket = fruits.copy()
>>> basket
['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> fruits
['apple', 'pears', 'banana', 'pineapple', 'Avacado']
```

<b>reverse()</b>	Reverses the order of the list
```python
>>> fruits = ['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> fruits.reverse()
>>> fruits
['Avacado', 'pineapple', 'banana', 'pears', 'apple']
```

#### list unpacking
```python
>>> a,b,c, *remaining, d = [1,2,3,4,5,6,7,8,9]
>>> a
1
>>> b
2
>>> c
3
>>> d
9
>>> remaining
[4, 5, 6, 7, 8]
```


### Dictionary
A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.</br>
In Python dictionaries are written with curly brackets, and they have keys and values.<br>

```python
dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

#### Dictionary Methods
<b>get()</b>	Returns the value of the specified key
```python
>>> dictionary = {  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
>>> dictionary.get('brand')
'Ford'
>>> dictionary.get('age')
None
>>> dictionary.get('age',40)	#if key-value is not found in given dictionary, use the default value.
40
```

<b>keys()</b>	Returns a list containing the dictionary's keys
```python
>>> dictionary = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> dictionary.keys()
dict_keys(['brand', 'model', 'year'])
```

<b>values()</b>	Returns a list of all the values in the dictionary
```python
>>> dictionary = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
>>> dictionary.values()
dict_values(['Ford', 'Mustang', 1964])
```

<b>items()</b>	Returns a list containing a tuple for each key value pair
```python
>>> dictionary = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature':['EcoBoost','Climate Control','Air filter']}
>>> dictionary.items()
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('feature', ['EcoBoost', 'Climate Control', 'Air filter'])])
```

<b>clear()</b>	Removes all the elements from the dictionary
```python
>>> dictionary = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature':['EcoBoost','Climate Control','Air filter']}
>>> dictionary.clear()
>>> dictionary
{}
```

<b>copy()</b>	Returns a copy of the dictionary
```python
>>> dictionary = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature':['EcoBoost','Climate Control','Air filter']}
>>> dictionary2 = dictionary.copy()
>>> dictionary2
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature': ['EcoBoost', 'Climate Control', 'Air filter']}
>>> dictionary.clear()
>>> dictionary
{}
>>> dictionary2
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature': ['EcoBoost', 'Climate Control', 'Air filter']}
```

<b>pop()</b>	Removes the element with the specified key
```python
>>> dictionary = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature':['EcoBoost','Climate Control','Air filter']}
>>> dictionary.pop()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dictionary.pop()
TypeError: pop expected at least 1 argument, got 0
>>> dictionary.pop('year')
1964
```

<b>popitem()</b>	Removes the last inserted key-value pair
```python
>>> dictionary
{'brand': 'Ford', 'model': 'Mustang', 'feature': ['EcoBoost', 'Climate Control', 'Air filter']}
>>> dictionary= {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature':['EcoBoost','Climate Control','Air filter']}
>>> dictionary.popitem()
('feature', ['EcoBoost', 'Climate Control', 'Air filter'])
```

<b>update()</b>	Updates the dictionary with the specified key-value pairs
```python
>>> dictionary = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'feature':['EcoBoost','Climate Control','Air filter']}
>>> dictionary.update({'year':1965})
>>> dictionary
{'brand': 'Ford', 'model': 'Mustang', 'year': 1965, 'feature': ['EcoBoost', 'Climate Control', 'Air filter']}
>>> dictionary.update({'Airbag':'yes'})
>>> dictionary
{'brand': 'Ford', 'model': 'Mustang', 'year': 1965, 'feature': ['EcoBoost', 'Climate Control', 'Air filter'], 'Airbag': 'yes'}
```

values()	Returns a list of all the values in the dictionary
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value


### Tuples
A tuple is a collection which is ordered and unchangeable. <em>Immutable</em><br>
In Python tuples are written with round brackets.<br>
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.<br>
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
e.g.
For rideshare car services, we can create a new tuple everytime a user requests a new pickup location.

#### Tuples Methods
<b>count()</b>	Returns the number of times a specified value occurs in a tuple
```python
>>> fruits = ('apple','Strawberry', 'mango', 'banana', 'kiwi','pineapple', 'Avacado','mango')
>>> fruits.count('mango')
2
```

<b>index()</b>	Searches the tuple for a specified value and returns the position of where it was found
```python
>>> fruits = ('apple','Strawberry', 'mango', 'banana', 'kiwi','pineapple', 'Avacado','mango')
>>> fruits.index('mango')
2
>>> fruits.index('kiwi')
4
```

#### Tuple slicing
```python
>>> fruit_tuple = ('apple', 'pears', 'banana', 'pineapple', 'Avacado')
>>> fruit_tuple
('apple', 'pears', 'banana', 'pineapple', 'Avacado')
>>> fruit_tuple[1]
'pears'
>>> fruit_tuple[0:2]
('apple', 'pears')
>>> fruit_tuple[:4]
('apple', 'pears', 'banana', 'pineapple')
>>> fruit_tuple[0:4:2]
('apple', 'banana')
>>> fruit_tuple[::-1]
('Avacado', 'pineapple', 'banana', 'pears', 'apple')
```

#### Tuple unpacking
```python
>>> fruits = ('apple','Strawberry', 'pears', 'banana', 'kiwi','pineapple', 'Avacado','mango')
>>> x, y, z, *others = ('apple','Strawberry', 'pears', 'banana', 'kiwi','pineapple', 'Avacado','mango')
>>> x
'apple'
>>> y
'Strawberry'
>>> z
'pears'
>>> others
['banana', 'kiwi', 'pineapple', 'Avacado', 'mango']
```

### Python Keywords
<em>in</em>	To check if a value is present in a list, tuple, etc.
```python
>>> fruits = ['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> 'apple' in fruits
True
>>> 'mango' in fruits
False
```

### Python Built in Functions

<em>sorted()</em>	Returns a sorted list
```python
>>> fruits = ['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> sorted(fruits)
['Avacado', 'apple', 'banana', 'pears', 'pineapple']	#creates new list/array
>>> fruits
['apple', 'pears', 'banana', 'pineapple', 'Avacado']	#doesn't modify the original list
```


### Most commonly used file formats in Python
1. CSV file
2. JSON file
3. XML file
4. Docx file
5. PDF file
