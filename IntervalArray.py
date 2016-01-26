from Interval import Interval

class IntervalArray(object):

    def __init__(self, intervals_list = None):
        self.list = []
        if intervals_list is not None:
            self.list = intervals_list
            self.merge_overlapping()

    def merge_overlapping(self):
        intervals = sorted(self.list)
        result = [intervals[0]]
        for n in intervals[1:]:
            if n.begin <= result[-1].end: result[-1].end = max(n.end, result[-1].end)
            else: result.append(n)
        self.list = result

    def add_interval(self, interval):
        self.list.append(interval)
        self.merge_overlapping()


    def remove_interval(self, interval):
        i = None
        index = binary_search_delete(self.list, interval.begin)

        results = self.list[:index]
        if index > 0:
            if interval.begin < results[-1].end:
                if results[-1].begin != interval.begin:
                    if interval.end < results[-1].end:
                        i = Interval("['%s','%s']" % (interval.end, results[-1].end))
                    results[-1].end = interval.begin
                    if i:
                        results.append(i)
                else:
                    if interval.end >= results[-1].end:
                        results.pop()
                    else:
                        results[-1].begin = interval.end


        for n in self.list[index:]:
            if n.begin < interval.end:
                if n.end < interval.end:
                    pass
                else:
                    n.begin = interval.end
                    results.append(n)
            else:
                results.append(n)
        self.list = results


    def query(self, string):
        first = 0
        last = len(self.list)-1
        found = False

        while first<last and not found:
            midpoint = (first + last)//2
            if self.list[midpoint].begin == string:
                found = True
            else:
                if string < self.list[midpoint].begin:
                    last = midpoint-1
                elif string > self.list[midpoint].begin and string < self.list[midpoint+1].begin:
                    first = midpoint
                    last = midpoint
                else:
                    first = midpoint + 1

        index = midpoint if found else first
        if self.list[index].contains(string):
            return True
        else:
            return False

    def __repr__(self):
        return str(self.list)


# Helper function
def binary_search_delete(list, string):
        first = 0
        last = len(list)-1
        found = False

        if len(list) == 1:
            if string < list[first].begin:
                return 0
            if string >= list[first].begin:
                return 1
        while first<=last and not found:
            if first == last:
                return first + 1

            midpoint = (first + last)//2
            if list[midpoint].begin == string:
                found = True
                return midpoint
            else:
                if string < list[midpoint].begin:
                    last = midpoint-1
                elif string > list[midpoint].begin and string < list[midpoint+1].begin:
                    return midpoint + 1

                else:
                    first = midpoint + 1

        return last
