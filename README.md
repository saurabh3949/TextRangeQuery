IntervalArray
============

A mutable, self-balancing IntervalArray for Python 2.

###API and usage:
`from Interval import Interval`

`from IntervalArray import IntervalArray`

`array = IntervalArray()`

* `array.add_interval(Interval)`: Addition of a text range to the set being tracked.
* `array.remove_interval(Interval)`: Deletion of a text range from the set being tracked.
* `array.query(String)`: Query on whether a specific string is inside the set of ranges being
tracked.

**See more examples in example.py**

### Note
Currently the API supports only closed ranges - "[]". Support for open ranges - "()" will be added soon.
