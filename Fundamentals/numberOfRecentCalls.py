# fifth time
class RecentCounter:

    def __init__(self):
        self.queue = []
        self.count = 0
        
    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count += 1
        
        while self.count > 0 and self.queue[0] < t-3000:
            self.queue.pop(0)
            self.count -= 1
        
        return self.count


# Fourth time

class RecentCounter:

    def __init__(self):
        self.queue = []
        
    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        while len(self.queue) > 0 and self.queue[0] < t - 3000 :
            self.queue.pop(0)
        
        return len(self.queue)




# third time
def __init__(self):
        self.count = 0
        self.queue = []

    def ping(self, t: int) -> int:
        self.count += 1
        self.queue.append(t)
        
        while len(self.queue) > 0 and self.queue[0] <  t - 3000 :
            self.queue.pop(0)
            self.count -= 1
        return self.count






# second time, after having seen solution the day prior
class RecentCounter:

    def __init__(self):
        self.count = 0
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.count += 1
        
        #print(self.queue)
        #print(t)
        while self.queue[0] < t - 3000 and self.count >= 0:
            #print("popped " + str(self.queue.pop(0)))
            self.queue.pop(0)
            self.count -= 1
        return self.count






#first bad solution


class RecentCounter:

    def __init__(self):
        self.count = 0
        self.currentTime = 0
        self.reports = ListNode(-10000)

    def ping(self, t: int) -> int:
        # update current time
        self.currentTime = t
        
        # add a new linkedList node to the reports list
        newReport = ListNode(t)
        newReport.next = self.reports.next
        self.reports.next = newReport
        
        # trim reports and update count
        cur = self.reports.next
        self.count = 0
        #print("currentTime is " + str(self.currentTime))
        #print("starting list print")
        while cur:
            #print(cur.val)
            if cur.val < self.currentTime - 3000:
                cur = None
            else:
                self.count += 1
                cur = cur.next
        #print("end of list print")
        #print("count was " + str(self.count))
        return self.count