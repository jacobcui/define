"""A handy script to lookup words."""
#!C:\Python310\python.exe
#Change the above line to where your python is.

import sys

import translate
from PyDictionary import PyDictionary
import argparse

def print_title(title):
    print(title)
    print('=' * len(title))

parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', dest='to',
    default='zh', help='Language code as used in Google translator.')
parser.add_argument(
    '--translate-only', action='store_true',
    dest='translate_only', help='Only translate')
parser.add_argument(
    'words', metavar='words', nargs='+',
    help='Words to be explained.')

args = parser.parse_args()

dict_obj = PyDictionary()

if not args.translate_only:
    for word in args.words:
        meaning = dict_obj.meaning(word)
        print_title(word)
        if meaning:
            for word_type, word_meanings in meaning.items():
                print(word_type, ':')
                for word_meaning in word_meanings:
                    print(f'\t{word_meaning}')
            print()

trans= translate.Translator(to_lang=args.to)

try:
    words = ' '.join(args.words)
    translate_result = trans.translate(words)
    print_title(words)
    print(translate_result)
except (StopIteration, RuntimeError):
    sys.exit()
