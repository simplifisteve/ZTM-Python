# try:
#     with open('test.txt', mode='r+') as my_file:
#         text = my_file.write('Hello world!')
#         # my_file.readline()
#         print(text)
# except FileNotFoundError as err:
#     print("File does not exist")
#     raise err
# except IOError as err:
#   print("IO error")
#   raise err

# -w mode will overwrite the existing file and create a file if it doesn't exist
# -a mode will append to the existing file

# Translator exercise
from translate import Translator
translator = Translator(to_lang="ja")

try:
    with open('test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print("File does not exist")
