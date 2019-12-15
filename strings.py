import sys
import string


def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
       end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

# s1 = "His name is {0}!".format("Arthur")
# print(s1)
#
# name = "Alice"
# age = 10
# s2 = "I am {1} and I am {0} years old.".format(age, name)
# print(s2)
#
# n1 = 4
# n2 = 5
# s3 = "2**10 = {0} and {1} * {2} = {3:.2f}".format(2**10, n1, n2, n1 * n2)
# print(s3)

# n1 = "Paris"
# n2 = "Whitney"
# n3 = "Hilton"
#
# print("Pi to three decimal places is {0:.3f}".format(3.1415926))
# print("123456789 123456789 123456789 123456789 123456789 123456789")
# print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||"
#         .format(n1,n2,n3,1981))
# print("The decimal value {0} converts to hex value {0:x}"
#         .format(123456))

# layout = "{0:<}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"
#
# print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
# for i in range(1, 11):
#     print(layout.format(i, i**2, i**3, i**5, i**10, i**20))


# prefixes = "JKLMNOPQ"
# suffix = "ack"
#
# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + "u" + suffix)
#     else:
#         print(letter + suffix)


def count_chars(character, word):
    count = 0
    j = 0
    k = 1
    for i in range(len(word)):
        if word.find(character, j, k) != -1:
            count += 1
        j += 1
        k += 1
    # for i in character:
    #     if i == word:
    #         count += 1
    return count


print(count_chars(character = "e", word = "whatever"))

theodore = """It is not the critic who counts; not the man who points out how the strong man stumbles, or where the 
doer of deeds could have done them better. The credit belongs to the man who is actually in the arena, whose face is 
marred by dust and sweat and blood; who strives valiantly; who errs, who comes short again and again, because there 
is no effort without error and shortcoming; but who does actually strive to do the deeds; who knows great 
enthusiasms, the great devotions; who spends himself in a worthy cause; who at the best knows in the end the triumph 
of high achievement, and who at the worst, if he fails, at least fails while daring greatly, so that his place shall 
never be with those cold and timid souls who neither know victory nor defeat. """


def remove_punct():
    count = 0
    quote = ""
    for i in theodore:
        if i not in string.punctuation:
            quote += i

    words = quote.split()
    for j in words:
        if j.find("e") != -1:
            count += 1

    output = "Your text contains {0} words, of which {1} ({2:.1f}%) contain an \"e\"".format(len(words),count,((count/len(words))*100))
    return output


print(remove_punct())

layout = "{0:>4}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"
print(layout.format("1*", "2*", "3*", "4*", "5*", "6*", "7*", "8*", "9*", "10*", "11*", "12*"))

for i in range(1, 13):
    for j in range(1, 13):
        mult = i * j
        print("{0:>4}".format(mult), end = "")
    print()


def rev_string(x):
    reverse = ""
    for i in range(-1,-(len(x)+1),-1):
        reverse += x[i]
    return reverse


def mirror(x):
    mirrored = x + rev_string(x)
    return mirrored


def test(did_pass):
    """  Print the result of a test.  """
    line_num = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(line_num)
    else:
        msg = "Test at line {0} FAILED.".format(line_num)
    print(msg)


def test_suite():
    ss = "Python strings have some interesting methods."
    test(find(ss, "s") == 7)
    test(find(ss, "s", 7) == 7)
    test(find(ss, "s", 8) == 13)
    test(find(ss, "s", 8, 13) == -1)
    test(find(ss, ".") == len(ss) - 1)

    test(ss.find("s") == 7)
    test(ss.find("s", 7) == 7)
    test(ss.find("s", 8) == 13)
    test(ss.find("s", 8, 13) == -1)
    test(ss.find(".") == len(ss) - 1)
    test(ss.find("str") == 7)

    test(remove_punctuation('"Well, I never did!", said Alice.') ==
         "Well I never did said Alice")
    test(remove_punctuation("Are you very, very, sure?") ==
         "Are you very very sure")

    my_story = """
    Pythons are constrictors, which means that they will 'squeeze' the life
    out of their prey. They coil themselves around their prey and with
    each breath the creature takes the snake will squeeze a little tighter
    until they stop breathing completely. Once the heart stops the prey
    is swallowed whole. The entire animal is digested in the snake's
    stomach except for fur or feathers. What do you think happens to the fur,
    feathers, beaks, and eggshells? The 'extra stuff' gets passed out as ---
    you guessed it --- snake POOP! """

    wds = remove_punctuation(my_story).split()
    # print(wds)

    test(rev_string("happy") == "yppah")
    test(rev_string("Python") == "nohtyP")
    test(rev_string("") == "")
    test(rev_string("a") == "a")

    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")


test_suite()


