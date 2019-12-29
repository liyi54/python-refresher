import random
import time
import seqtools
import unit_tester
import calendar

# def make_random_ints_no_dups(num, lower_bound, upper_bound):
#    """
#      Generate a list containing num random ints between
#      lower_bound and upper_bound. upper_bound is an open bound.
#      The result list cannot contain duplicates.
#    """
#    result = []
#    rng = random.Random()
#    for i in range(num):
#         while True:
#             candidate = rng.randrange(lower_bound, upper_bound)
#             if candidate in result:
#                 continue
#             else:
#                 break
#         result.append(candidate)
#    return result
#
#
# xs = make_random_ints_no_dups(10, 1, 6)
# print(xs)


# def do_my_sum(xs):
#     sum = 0
#     for v in xs:
#         sum += v
#     return sum
#
# sz = 10000000        # Lets have 10 million elements in the list
# testdata = range(sz)
#
# t0 = time.process_time()
# my_result = do_my_sum(testdata)
# t1 = time.process_time()
# print("my_result    = {0} (time taken = {1:.4f} seconds)"
#         .format(my_result, t1-t0))
#
# t2 = time.process_time()
# their_result = sum(testdata)
# t3 = time.process_time()
# print("their_result = {0} (time taken = {1:.4f} seconds)"
#         .format(their_result, t3-t2))

s = "A string"
unit_tester.test(seqtools.remove_at(4, s) == "A sting")

cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2012)