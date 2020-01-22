import unit_tester as ut

alreadyknown = {0: 0, 1: 1}

def fib(n):
    if n not in alreadyknown:
        new_value = fib(n-1) + fib(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

print(fib(100))

letter_counts = {}

word = "ThiS is String with Upper and lower case Letters"
p_word = "".join(word.split(" "))
word_lower = p_word.lower()
for letter in word_lower:
    letter_counts[letter] = letter_counts.get(letter,0)+1

letter_items = list(letter_counts.items())
letter_items.sort()
for l,num in letter_items:
    print(l,"\t",str(num))

total = 0

def add_fruit(dict_name,key,value):
    global total
    total += value
    dict_name[key] = total

new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
ut.test("strawberries" in new_inventory)
ut.test(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
ut.test(new_inventory["strawberries"] == 35)

