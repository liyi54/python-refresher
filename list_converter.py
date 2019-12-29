def convert_to_query(s):
    list_items = s.split("\n")

    for i in list_items:
        if len(i) == 0:
            continue
        else:
            print("'" + i + "'", end=",") # Ensure you take out the last comma at the end of the file


def convert_to_query_file(s):
    list_items = open("from_file.txt", "w")
    list_items.write(s)
    list_items.close()

    line_item = open("from_file.txt", "r")
    items = line_item.read()
    line_item.close()
    item_list = items.split("\n")

    new_file = open("to_file.txt", "w")

    for i in item_list:
        if len(i) == 0:
            continue
        else:
            new_file.write("'" + i + "'"+",")   # Ensure you take out the last comma at the end of the file

    new_file.close()


