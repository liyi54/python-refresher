class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """Create a MyTime object initialized to hrs, mins, secs"""
        tsecs = hrs * 3600 + mins * 60 + secs
        self.hours = tsecs // 3600
        rem = tsecs % 3600
        self.minutes = rem // 60
        rem %= 60
        self.seconds = rem


    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    def add_time(self, t2):
        tot_secs = self.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, tot_secs)

    def __add__(self, other):
        """Overloading the plus operator"""
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        """Overloading the minus operator"""
        return MyTime(0,0, self.to_seconds() - other.to_seconds())

    # def add_time(self,t2):
    #     """Pure function"""
    #     h = self.hours + t2.hours
    #     m = self.minutes + t2.minutes
    #     s = self.seconds + t2.seconds
    #
    #     if s > 60:
    #         m += 1
    #         s -= 60
    #     if m >= 60:
    #         h += 1
    #         m -= 60
    #     if h >= 24:
    #         h -= 24
    #     return MyTime(h, m, s)

    # def increment(self,secs):
    #     """Modifier"""
    #     self.seconds += secs
    #     if self.seconds >= 60:
    #         self.seconds -= 60
    #         self.minutes += 1
    #
    #     if self.minutes >= 60:
    #         self.minutes -= 60
    #         self.hours += 1
    #
    #     if self.hours >= 24:
    #         self.hours -= 24

    # def increment(self, secs):
    #     """Increment the time with seconds"""
    #     self.seconds += secs
    #     while self.seconds >= 60:
    #         self.seconds -= 60
    #         self.minutes += 1
    #     while self.minutes >= 60:
    #         self.minutes -= 60
    #         self.hours += 1
    #     while self.hours >= 24:
    #         self.hours -= 24
    #     return self

    def increment(self,secs):
        tot_secs = self.to_seconds() + secs
        if tot_secs < 0:
            raise ValueError("Value is larger than time object : {0}".format(ValueError))
        self.hours = tot_secs // 3600
        remd = tot_secs % 3600
        self.minutes = remd // 60
        remd %= 60
        self.seconds = remd

    def to_seconds(self):
        """Convert object to seconds"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    # def is_after(self,t2):
    #     if self.hours > t2.hours:
    #         return True
    #     elif self.hours < t2.hours:
    #         return False
    #     elif self.minutes > t2.minutes:
    #         return True
    #     elif self.minutes < t2.minutes:
    #         return False
    #     elif self.seconds > t2.seconds:
    #         return True
    #     else:
    #         return False

    # def is_after(self, t2):
    #     return self.to_seconds() > t2.to_seconds()

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

# print(MyTime(10,30,50).increment(200))
# print(time1)
# print(MyTime(100,26,72))

t1 = MyTime(1, 15, 42)
# t2 = MyTime(3, 50, 30)
# t3 = t1 + t2
# print(t2 > t1)

t1.increment(-5000)
t1.increment(-1000)
print(t1)