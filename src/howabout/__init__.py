from itertools import groupby

from six.moves import map


def get_levenshtein(first, second):
    """\
    Get the Levenshtein distance between two strings.

    :param first:     the first string
    :param second:    the second string
    """
    if not first:
        return len(second)

    if not second:
        return len(first)

    prev_distances = range(0, len(second) + 1)
    curr_distances = None

    # Find the minimum edit distance between each substring of 'first' and
    # the entirety of 'second'. The first column of each distance list is
    # the distance from the current string to the empty string.
    for first_idx, first_char in enumerate(first, start=1):
        # Keep only the previous and current rows of the
        # lookup table in memory
        curr_distances = [first_idx]

        for second_idx, second_char in enumerate(second, start=1):
            # Take the max of the neighbors
            compare = [
                prev_distances[second_idx - 1],
                prev_distances[second_idx],
                curr_distances[second_idx - 1],
            ]

            distance = min(*compare)

            if first_char != second_char:
                distance += 1

            curr_distances.append(distance)

        prev_distances = curr_distances

    return curr_distances[-1]


class Matcher(object):
    """\
    TODO
    """

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
