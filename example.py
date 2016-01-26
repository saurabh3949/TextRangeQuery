from Interval import Interval
from IntervalArray import IntervalArray

intervals = [ Interval('["A","D"]'),
              Interval('["B","C"]'),
              Interval('("H","Z"]'),
              Interval('["H","I"]'),
              Interval('["X", "ZZ"]')]

array = IntervalArray(intervals)
print array.list
# [[A , D], [H , ZZ]]

array.remove_interval(Interval('("H","SE"]'))
print array.list
#[[A , D], [SE , ZZ]]

array.add_interval(Interval('("F","SE"]'))
print array.list
# [[A , D], (F , ZZ)]

array.query("F")
# False

array.query("ZA")
# True














