Named tuples are a convenient and readable way to define simple classes for storing and accessing data in Python. They are part of the `collections` module. Named tuples are similar to regular tuples, but they have named fields, making the code more self-documenting.

```python
from collections import namedtuple

# Define a named tuple type called 'Person' with fields 'name', 'age', and 'gender'
Person = namedtuple('Person', ['name', 'age', 'gender'])

# Create an instance of the named tuple
person1 = Person(name='Alice', age=30, gender='Female')

# Accessing values using dot notation
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
print(person1.gender)  # Output: Female
```

In this example, `Person` is a named tuple type with fields 'name', 'age', and 'gender'. When you create an instance of this named tuple, you can access the values using dot notation, which makes the code more readable compared to using indices as you would with a regular tuple.

Named tuples are immutable, meaning once you create an instance, you can't modify its values. If you need to change values, you would create a new named tuple with the updated values.

They are particularly useful when you have simple data structures and want more clarity and readability in your code.[up](README.md)
[top](../README.md)
