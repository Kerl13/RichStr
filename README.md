# RichStr

`RichStr` defines two mixins allowing to easily define fancy `__str__` methods
for a class.

This is a piece of code I reuse frequently, mostly in programs aiming at
displaying information like [GHA](https://github.com/Kerl13/GHA). I put it on
GitHub because it is more handy for me to have it here but let me know if it is
also useful for you, I would be very happy to have some feedback :)

## How to

### `RichStr`

This mixin allows you to define the `__str__` method implicitly using the class
variable `TEMPLATE`. This variable should be a valid
[format string](https://docs.python.org/3.4/library/string.html#format-string-syntax)
and will be fed by default by the object's `__dict__` attribute.

For example:

```python
from richstr.models import RichStr

class Frac(RichStr):
    TEMPLATE = "{num}/{denom}"

    def __init__(self, num, denom=1):
        self.num = num
        self.denom = denom

str(Frac(2, 3))  # result: "2/3"
```

Two hooks are also available to let you customize this class:

- `get_template` returns the template
- `get_context` returns the dictionary used as keyword arguments for the
  `format` method during the rendering.

An example using theses hooks:

```python
from richstr.models import RichStr

class Frac(RichStr):
    TEMPLATE = "{num}/{denom} = {result}"

    def __init__(self, num, denom=1):
        self.num = num
        self.denom = denom

    def get_context(self):
        context = super().get_context()
        context["result"] = self.num / self.denom
        return context

    def get_template(self):
        if self.denom == 1:
            return "{num}"
        else:
            super().get_template()

str(Frac(2, 4))   # result: "2/4 = 0.5"
str(Frac(42, 1))  # result: "42"
```


### `RichStrList`

This mixin allows you to print a list of objects in a similar way. You specify
how an element is displayed using the `TEMPLATE` class attribute and you can
specify the separator between each element with the `SEPARATOR` attribute (by
default it is `\n`).

The `__init__` method of this class expects a list of dictionaries and use them
as keyword arguments to instantiate multiple `RichStr` objects. (I don't really
like this design, it may change in the future).

Example:

```python
from richstr.models import RichStrList

class FracSum(RichStrList):
    TEMPLATE = "({num}/{denum})"
    SEPARATOR = " + "

str(FracSum([
    {num: 2, denom: 3},
    {num: 1, denom: 4},
    {num: 42, denom: 1}
]))  # result: "(2/3) + (1/4) + (42, 1)"
```
