class Interval(object):
    """
    Attributes:
    left: Boolean. Type of left bracket. Closed = True. Open = False
    right: Boolean. Type of right bracket. Closed = True. Open = False
    begin: Str. Left string of the interval
    end: Str. Right string of the interval
    """
    def __init__(self, interval_string):
        interval_string = interval_string.strip()
        self.interval_string = interval_string
        left = interval_string[0]
        right = interval_string[-1]

        self.left = get_edge_type(left)
        self.right = get_edge_type(right)

        if self.left == self.right:
            interval = eval(interval_string)
            self.begin = interval[0]
            self.end = interval[1]

        else:
            interval_string = list(interval_string)
            interval_string[0] = "["
            interval_string[-1] = "]"
            interval_string = "".join(interval_string)
            interval = eval(interval_string)
            self.begin = interval[0]
            self.end = interval[1]

    def contains(self, string):
        if string > self.begin and string < self.end:
            return True
        if string == self.begin and self.left:
            return True
        if string == self.end and self.right:
            return True
        return False


    def __lt__(self, other):
        if self.begin == other.begin:
            if not self.left and other.left:
                return False
            else:
                return True
        return self.begin < other.begin

    def __repr__(self):
        left = "[" if self.left else "("
        right = "]" if self.left else ")"
        return left + self.begin + " , " + self.end + right

# Helper function
def get_edge_type(bracket):
    if bracket in ["[" ,"]"]:
        return True
    elif bracket in ["(", ")"]:
        return False
    else:
        # Raise exception
        return None
