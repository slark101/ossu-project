"""
Code for testing problem set code
"""
import re
import unittest


def compare_with_regex(compare:str,val:str):
    no_space_word = compare.replace(' ','')
    unique_word = ''.join(set(no_space_word.replace('_','')))
    regex = '^'
    
    for i in compare.replace(' ','').lower():
      if i == '_':
        regex = regex+"(?!["+unique_word+"])[a-z]{1}"
      else:
        regex = regex+i
    return bool(re.match(regex+'$',val.lower()))

class TestCode(unittest.TestCase):
    def test_code(self):
        self.assertTrue(compare_with_regex('s_ l_ ','sold'))
        self.assertFalse(compare_with_regex('s_ l_ ','bold'))

if __name__ == "__main__":
    unittest.main()