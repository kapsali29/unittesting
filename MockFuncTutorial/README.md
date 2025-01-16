# Notes from this tutorial
https://codefather.tech/blog/python-mock-and-patch/
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
### @patch Decorator
The **unittest.mock** library provides the patch decorator that can 
replace the behaviour of a target.

#### Decorator Usage
1. import patch instead of MagicMock `from unittest.mock import patch`
2. add the decorator to the test method
```python
@patch(unique_names.get_file_names)
```
3. Add the argument `mock_get_file_names.return_value`, follows the pattern `mock_${patch_target}` inside your test method. This automatically passed by the decorator
4. Set the `mock_get_file_names` return value

Example is given to the following code snippet

```python
# tests/test_names_patch.py
import unique_names
from unittest.mock import patch

class TestNamePatch(unittest.TestCase):
    @patch('unique_names.get_file_names')
    def test_names_patch(self, mock_get_file_names):
        mock_get_file_names.return_value = ["Panos", "Vas", "Ellie"]
        names = unique_names.get_unique_names("names.txt")
        self.assertIsEqual(names, ["Ellie", "Panos", "Vas"])
        
```