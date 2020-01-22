from list_algos import text_to_words

from_file = open("/Users/sadeliyi/Documents/alice_in_wonderland.txt","r")
words = from_file.read()
from_file.close()
# words.lower()
word_list = text_to_words(words)
# word_list.sort()
# print(word_list)

# print(word_list)
#
# largest = ""
# for i in word_list:
#     if len(i) > len(largest):
#         largest = i

# print("Largest word is {0} and the length is {1}".format(largest, len(largest)))

all_words = {}

for elem in word_list:
    all_words[elem] = all_words.get(elem,0) + 1

word_count = list(all_words.items())
word_count.sort()


layout = "{0}{1:>14}"
header1 = "Word"
header2 = "Count"
start = "======================\n"

to_file = open("/Users/sadeliyi/Documents/alice_description.txt","w")
to_file.write(layout.format(header1,header2) + "\n")
to_file.write(start)

for word,count in word_count:
    to_file.write(layout.format(word, str(count))+ "\n")

to_file.close()