"""A handy script to lookup words."""
#!C:\Python310\python.exe
#Change the above line to where your python is.

import sys

import translate
from PyDictionary import PyDictionary

if len(sys.argv) == 1:
    print('Please put a word.')
    sys.exit()

LANG_CODE = 'zh'
word = sys.argv[1]

trans= translate.Translator(to_lang=LANG_CODE)

try:
    translate_result = trans.translate(word)
except (StopIteration, RuntimeError):
    print(f'Meaning of {word} not found :(')
    sys.exit()

dict_obj = PyDictionary()
meaning = dict_obj.meaning(word)

for word_type, word_meanings in meaning.items():
    print(word_type, ':')
    for word_meaning in word_meanings:
        print(f'\t{word_meaning}')

print(translate_result)
