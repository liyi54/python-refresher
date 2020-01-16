import urllib.request
import string


# def retrieve_page(url):
#     """ Retrieve the contents of a web page.
#         The contents is converted to a string before returning it.
#     """
#     my_socket = urllib.request.urlopen(url)
#     dta = my_socket.read()
#     my_socket.close()
#     return dta
#
# the_text = retrieve_page("http://xml.resource.org/public/rfc/html/rfc2010.html")
# print(the_text)

input_file = open("/Users/sadeliyi/Downloads/-.txt", "r")
output_file = open("reversed.txt", "w")

read_file = input_file.readlines()

input_file.close()

for i in range(-1, -(len(read_file)+1), -1):
    output_file.write(read_file[i] + "\n")

output_file.close()
