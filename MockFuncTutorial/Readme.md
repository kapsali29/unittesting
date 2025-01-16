## How to use MagicMock

Mocking is a technique used to replace part of the code that
cannot be easily tested and replaces the functionality of real objects.
Using mocks is quite useful especially when someone wants to **test
code that relies to external dependencies and components like APIs or files.**

An example case is that if a file is depending on an external file and if this gonna be deleted
then your tests will fail

### Magicmock

```python
from unittest.mock import MagicMock
```

MagicMock is used to functions or other objects with Mock objects

for instance imagine a scenario where we have a file called `file1.py`
with 2 functions func1 and func2 where func1 calls func2
```python
# file1.py

def func1():
    return 1

def func2():
    res = func1()
    return res + 5
```

MagicMock can be used to emulate the result of func1 in order to control the behaviour of the object
as follows:

```python
# file2.py

from unittest.mock import MagicMock
import file1

file1.func1 = MagicMock()
file1.func1.return_value = 7
print(file1.func2)
>>> 12
```
The following snippet depicts how MagicMock can be used inside
a Test Class

```python
# tests/test_func2.py
import unittest
import file1
from unittest.mock import MagicMock

class TestFunc2(unittest.TestCase):
    def test_this(self):
        file1.func1 = MagicMock()
        file1.func1.return_value = 7
        result = file1.func2()
        self.assertEqual(result, 12)
        
### execute this file with this command
### python -m unittest test_func2.TestFunc2.test_this
```