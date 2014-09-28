from itertools import groupby

from six.moves import map

def get_levenshtein(first, second):
   """\
   Get the Levenshtein distance between two strings.

   :param first:     the first string
   :param second:    the second string 
   """

   first_len = len(first) + 1
   second_len = len(second) + 1

   prev = list(range(0, second_len))

   # If the first string is empty, then the loop will
   # never run. Thus, the edit distance between the
   # second string and empty string for any given
   # position is that position.

   current = prev

   # Keep only the previous and current rows of the
   # lookup table in memory

   for row in range(1, first_len):
      current = [row]

      for col in range(1, second_len):
         compare = []

         if row == col:
            value = prev[col-1]
            value += 0 if first[row-1] == second[col-1] else 1
            compare.append(value)

         compare.append(current[col-1] + 1)
         compare.append(prev[col] + 1)

         distance = min(*compare)
         current.append(distance)

      prev = current
  
   return current[-1]

class Matcher(object):
   def __init__(self):
      self.distance_func = get_levenshtein

   def get_distance(self, first, second):
      """\
      Get the edit distance between the first string and another string.

      :param first:  a string
      :param second: another string
      """

      return self.distance_func(first, second)

   def all_matches(self, target, choices, group=False, include_rank=False):
      """\ 
      Get all choices listed from best match to worst match.  
      
      If `group` is `True`, then matches are grouped based on their distance
      returned from `get_distance(target, choice)` and returned as an iterator.
      Otherwise, an iterator of all matches is returned.

      For example

      ::

         from howabout import all_matches

         choices = ['pot', 'cat', 'bat']

         for group in all_matches('hat', choices, group=True):
            print(list(group))

         # ['bat', 'cat']
         # ['pot']


      :param target:    a string
      :param choices:   a list or iterable of strings to compare with
                        `target` string
      :param group:     if `True`, group 
      """
 
      dist = self.get_distance

      # Keep everything here as an iterator in case we're given a lot of
      # choices
      matched = ((dist(target, choice), choice) for choice in choices)
      matched = sorted(matched)

      if group:
         for rank, choices in groupby(matched, key=lambda m: m[0]):
            yield map(lambda m: m[1], choices)
      else:
         for rank, choice in matched:
            yield choice

   def best_matches(self, target, choices):
      """\ 
      Get all the first choices listed from best match to worst match,
      optionally grouping on equal matches.

      :param target:
      :param choices:
      :param group:
      """

      all = self.all_matches
      
      try:
         matches = next(all(target, choices, group=True))
         for match in matches:
            yield match
      except StopIteration:
         pass

   def best_match(self, target, choices):
      """\
      Return the best match.
      """

      all = self.all_matches
      
      try:
         best = next(all(target, choices, group=False))
         return best
      except StopIteration:
         pass

matcher = Matcher()

# Make these module-level functions

all_matches = matcher.all_matches
best_matches = matcher.best_matches
best_match = matcher.best_match
