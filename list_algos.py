import unit_tester
import time


def search_linear(ls, target):
    # x = time.process_time()
    for i,v in enumerate(ls):
        if target == v:
            # y = time.process_time()
            # diff = y - x
            # print(diff)
            return i
    return -1


def search_binary(ls, target):
    """ Find and return the index of key in sequence ls """
    lb = 0
    ub = len(ls)
    while True:
        if lb == ub:  # If region of interest (ROI) becomes empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = ls[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index  # Found it!
        if item_at_mid < target:
            lb = mid_index + 1  # Use upper half of ROI next time
        else:
            ub = mid_index  # Use lower half of ROI next time


def remove_adjacent_dups(ls):
    result = []
    most_recent_item = None
    for e in ls:
        if e!= most_recent_item:
            result.append(e)
            most_recent_item = e
    return result


def merge(xs,ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result  # And we're done.

        if yi >= len(ys):  # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if search_binary(vocab, w) <0 :
            result.append(w)
        # if (search_linear(vocab, w) < 0):
        #     result.append(w)
    return result


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:  # Good, word exists in vocab
            yi += 1

        elif vocab[xi] < wds[yi]:  # Move past this vocab word,
            xi += 1

        else:                     # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


bigger_vocab = load_words_from_file("/Users/sadeliyi/Documents/Data Science/build/_downloads/vocab.txt")
# print("There are {0} words in the vocab, starting with\n {1} "
#               .format(len(bigger_vocab), bigger_vocab[:6]))

# vocab = ["apple", "boy", "dog", "down",
#                           "fell", "girl", "grass", "the", "tree"]
# book_words = "the apple fell from the tree to the grass".split()
#
# unit_tester.test(find_unknown_words(vocab, book_words) == ["from", "to"])
# unit_tester.test(find_unknown_words([], book_words) == book_words)
# unit_tester.test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])
#
#
# friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# unit_tester.test(search_linear(friends, "Zoe") == 1)
# unit_tester.test(search_linear(friends, "Joe") == 0)
# unit_tester.test(search_linear(friends, "Paris") == 6)
# unit_tester.test(search_linear(friends, "Bill") == -1)
#
# unit_tester.test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
# unit_tester.test(text_to_words('"Well, I never!", said Alice.') ==
#                              ["well", "i", "never", "said", "alice"])

all_words = get_words_in_book("/Users/sadeliyi/Documents/Data Science/build/_downloads/alice_in_wonderland.txt")
t0 = time.process_time()
all_words.sort()
book_words = remove_adjacent_dups(all_words)
missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
t1 = time.process_time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))

# book_words = remove_adjacent_dups(all_words)
# print("There are {0} words in the book. Only {1} are unique.".
#                       format(len(all_words), len(book_words)))
# print("The first 100 words are\n{0}".
#            format(book_words[:100]))
# book_words = get_words_in_book("/Users/sadeliyi/Documents/Data Science/build/_downloads/alice_in_wonderland.txt")
# print("There are {0} words in the book, the first 100 are\n{1}".
#            format(len(book_words), book_words[:100]))

# t0 = round(time.process_time(),3)
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = round(time.process_time(),3)
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0} seconds.".format(t1-t0))

# ls = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
# unit_tester.test(search_binary(ls, 20) == -1)
# unit_tester.test(search_binary(ls, 99) == -1)
# unit_tester.test(search_binary(ls, 1) == -1)
# for (i, v) in enumerate(ls):
#     unit_tester.test(search_binary(ls, v) == i)

# t0 = round(time.process_time(),3)
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = round(time.process_time(),3)
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0} seconds.".format(t1-t0))

# unit_tester.test(remove_adjacent_dups([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
# unit_tester.test(remove_adjacent_dups([]) == [])
# unit_tester.test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
#                                    ["a", "big", "bite", "dog"])

# xs = [1,3,5,7,9,11,13,15,17,19]
# ys = [4,8,12,16,20,24]
# zs = xs+ys
# zs.sort()
# unit_tester.test(merge(xs, []) == xs)
# unit_tester.test(merge([], ys) == ys)
# unit_tester.test(merge([], []) == [])
# unit_tester.test(merge(xs, ys) == zs)
# unit_tester.test(merge([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
# unit_tester.test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
#                ["a", "big", "big", "bite", "cat", "dog"])

