def get_levenshtein(first, second):
   """\
   Get the Levenshtein distance between two strings.
   """

   distances = {}

   def get_distance(i, j):
      # Return the non-zero distance, as it's the maximum
      if min(i, j) == 0:
         return max(i, j)

      try:
         delete = distances[i-1, j]
      except KeyError:
         delete = distances[i-1, j] = get_distance(i-1, j)

      try:
         insert = distances[i, j-1]
      except KeyError:
         insert = distances[i, j-1] = get_distance(i, j-1)

      try:
         differ = distances[i-1, j-1]
      except KeyError:
         differ = distances[i-1, j-1] = get_distance(i-1, j-1)

      # A differing character adds to the distance 
      similarity = 0 if first[i-1] == second[j-1] else 1
      distance = min(
         delete + 1, 
         insert + 1, 
         differ + similarity)

      return distance
   
   first_len = len(first)
   second_len = len(second)

   return get_distance(first_len, second_len)

def get_match(target, choices, max=None):
   """\
   Return the top ranked matches from the given choices for the target string.

   :param max: the maximum number of choices
   
   """
   
   heuristic = get_levenshtein
   distances = sorted([(heuristic(target, choice), sorted) for choice in choices])

   # G
   

   
   best = max(enumerate(distances), key=lambda x:x[1])[0]
   return best
