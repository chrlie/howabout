import glob
import sys
import os

from howabout import best_matches

def exists_or_best_match(filename):
   """\
   Returns `Exists` if the file exists or a list
   of the closest matching filenames otherwise.
   """
   if os.path.exists(filename):
      return True

   path = os.path.dirname(filename)
   choices = glob.glob(os.path.join(path, '*'))

   return best_matches(filename, choices)

def usage(name):
   print('usage: {0} [filename]'.format(name))

if __name__ == '__main__':
   if len(sys.argv) != 1:
      usage(sys.argv[0])
      sys.exit(1)

   filename = sys.argv[1]
   matches = exists_or_best_match(filename)

   if matches is True:
      print('Exists')
   else:
      print('Did you mean?')
      for match in matches:
         print('\t{0}'.format(match))
