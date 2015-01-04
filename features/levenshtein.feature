Feature: ensure the Levenshtein algorithm is implemented correctly

  Scenario: Compute distances without overflowing the interpreter
    Given two long strings
     When we compare them
     Then the interpreter should not overflow

  Scenario: Compute the distance between the empty string and itself
    Given two empty strings
     When we compare them
     Then the distance is 0

  Scenario Outline: Compute the distance between a string and an empty string
    Given "<string>" and the empty string
     When we compare them
     Then the distance is <distance>

    Examples:
     | string   | distance |
     | moreover |        8 |
     | a        |        1 |

  Scenario Outline: Compute the distance between identical strings
    Given a string "<string>"
     When we compare it to itself
     Then the distance is 0

    Examples:
     | string    |
     | landslide |
     | I         |
     | 4d3d3d3   |

  Scenario Outline: Compute the distance between strings differing by a prefix
    Given the first string "<first>" and the second string "<second>" starting with "<prefix>"
     When we compare them
     Then the distance is <distance>

    Examples:
     | first   | second  | prefix | distance |
     | render  | roll    | r      | 5        |
     | redo    | revisit | re     | 5        |
     | record  | retest  | re     | 4        |
     | rain    | rail    | rai    | 1        |