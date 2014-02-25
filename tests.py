import random

from howabout import get_levenshtein

def test_levenshtein_recursion_limit():
   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   random_str = lambda size: [random.choice(alphabet) for i in range(0, size)]

   first = random_str(1024)
   second = random_str(1024)

   # This should work
   try:
      get_levenshtein(first, second)
   except RuntimeError:
      raise AssertionError('Recursion limit exceeded')

def test_levenshtein_distance():
   first = 'fitting'
   second = 'sitting'

   distance = get_levenshtein(first, second)
   assert distance == 1

   first = ''
   second = 'sitting'

   distance = get_levenshtein(first, second)
   assert distance == 7

   first = 'sitting'
   second = ''

   distance = get_levenshtein(first, second)
   assert distance == 7

   first = ''
   second = ''

   distance = get_levenshtein(first, second)
   assert distance == 0

def test_get_closest_choice():
   choices = [
      'sitting',
      'fitting',
      'flitting',
   ]

   string = 'spitting'

   # These should be returned sorted by rank, then alphabetically
   #get_closest(string, choices

def test_ranked_choices():
   pass
