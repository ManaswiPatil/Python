# Python Cheatsheet
I have created this Cheat Sheet while learning Python to remember the common syntax and as a future handy reference.
<hr>

**[`Data types`](#python-data-types)**

#### Python Data Types
1. int
2. float
3. boolean
4. string
5. **[`list`](#list)**
6. tuple
7. set
8. **['dictionary'](#Dictionary)**

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

<b>copy()</b>	Returns a copy of the dictionary

<b>pop()</b>	Removes the element with the specified key





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
