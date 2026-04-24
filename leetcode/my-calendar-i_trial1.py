from bisect import bisect_left
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        self.events.sort()
        if self.events:
            i = bisect_left(self.events, (startTime, endTime))
            if i == 0:
                if endTime <= self.events[0][0]:
                    self.events.append((startTime, endTime))
                    return True
                else: return False
            if i == len(self.events):
                if startTime >= self.events[-1][1]:
                    self.events.append((startTime, endTime))
                    return True
                else: return False
            if startTime >= self.events[i-1][1] and endTime <= self.events[i][0]:
                self.events.append((startTime, endTime))
                return True
            else: return False
        else:
            self.events.append((startTime, endTime))
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)