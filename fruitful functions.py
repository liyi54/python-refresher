import sys
import math


def turn_clockwise(direction):
    navigation = ["N","E","S","W"]
    for i in navigation:
        if direction == i:
            new_position = navigation.index(direction) + 1
            if new_position > 3:
                new_position = 0
            return navigation[new_position]


def day_name(number):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if number <= 6:
        return days[number]


def day_num(name):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in days:
        if name == i:
            name = days.index(name)
            return name


def day_add(day, delta):
    leave_date = day_num(day)
    i = 0
    while i < abs(delta):
        if delta < 0:
            leave_date -= 1
            if leave_date < -7:
                leave_date = -1
            i += 1
        else:
            leave_date += 1
            if leave_date > 6:
                leave_date = 0
            i += 1
    return day_name(leave_date)


def days_in_month(month):
    calendar = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    for i in calendar:
        if month == i:
            return calendar[month]


def to_secs(hour, minute, second):
    hour_sec = hour * 60 * 60
    minute_sec = minute * 60
    total = hour_sec + minute_sec + second
    return int(total)


def hours_in(seconds):
    return int(seconds/3600)


def minutes_in(seconds):
    seconds_left = seconds % 3600
    to_minutes = int(seconds_left/60)
    return to_minutes


def seconds_in(seconds):
    seconds_left = seconds % 3600
    to_seconds = seconds_left % 60
    return to_seconds


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def hypotenuse(a,b):
    hypot_squared = a ** 2 + b ** 2
    hypot = math.sqrt(hypot_squared)
    return hypot


def slope(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return m


def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    b = y1 - m * x1
    return b


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if is_even(n) is True:
        return False
    else:
        return True


def is_factor(f, n):
    if n % f == 0:
        return True
    else:
        return False


def is_multiple(n, f):
    if is_factor(f, n) is True:
        return True
    else:
        return False


def f2c(t):
    temp = (t-32) * (5/9)
    celsius = round(temp, 0)
    return celsius


def c2f(t):
    temp = (t * (9 / 5)) + 32
    fahrenheit = round(temp, 0)
    return fahrenheit


def test(did_pass):
    """  Print the result of a test.  """
    line_num = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = "Test at line {0} FAILED.".format(line_num)
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module.
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)

    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)

    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)

    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")

    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("water") == None)
    test(days_in_month(23) == None)

    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)

    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

    # test(3 % 4 == 0)
    # test(3 % 4 == 3)
    # test(3 / 4 == 0)
    # test(3 // 4 == 0)
    # test(3 + 4 * 2 == 14)
    # test(4 - 2 + 2 == 0)
    # test(len("hello, world!") == 13)

    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)

    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)

    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)

    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)

    test(is_even(4) == True)
    test(is_even(6) == True)
    test(is_even(3) == False)
    test(is_even(8.0) == True)

    test(is_odd(4) == False)
    test(is_odd(6) == False)
    test(is_odd(3) == True)
    test(is_odd(8.0) == False)

    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))

    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))

    test(f2c(212) == 100)  # Boiling point of water
    test(f2c(32) == 0)  # Freezing point of water
    test(f2c(-40) == -40)  # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)

    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


test_suite()
