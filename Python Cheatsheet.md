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
8. dictionary

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
lists are mutable. This means we can change an item in a list by accessing it directly as part of the assignment statement.
```python
list=[1,0.75,'rose','knife']
```
```python
fruits = ['apple','pears','orange','banana','pineapple']

```
```python
fruits[0:2] list[start-index : stop]
fruits[0::2]  list[[start-index : stop : step]
```
#### List Methods
append()	Adds an element at the end of the list
```python
>>> fruits.append('strawberry')
>>> fruits
['apple', 'pears', 'orange', 'banana', 'pineapple', 'strawberry']
```
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
```python
>>> fruits = ['apple','pears','orange','banana','pineapple']
>>> fruits.extend(['Avacado','Mango'])
>>> fruits
['apple', 'pears', 'orange', 'banana', 'pineapple', 'Avacado', 'Mango']
```
index()	Returns the index of the first element with the specified value

insert()	Adds an element at the specified position
```python
>>> fruits.insert(3,'Blueberry')
>>> fruits
['apple', 'pears', 'orange', 'Blueberry', 'banana', 'pineapple', 'strawberry']
``` 
pop()	Removes the element at the specified position
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
remove()	Removes the first item with the specified value
```python
>>> fruits = ['apple', 'pears', 'banana', 'pineapple', 'Avacado']
>>> fruits.remove('banana')
>>> fruits
['apple', 'pears', 'pineapple', 'Avacado']
```
clear()	Removes all the elements from the list
```python
>>> fruits.clear()
>>> fruits
[]
```
reverse()	Reverses the order of the list
sort()	Sorts the list

### Most commonly used file formats in Python
1. CSV file
2. JSON file
3. XML file
4. Docx file
5. PDF file
