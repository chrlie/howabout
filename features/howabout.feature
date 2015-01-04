Feature: a Howabout matcher

  Scenario Outline: A matcher should list the best exact match first
    Given a "<type>" matcher and some strings
      | cordite  |
      | ant      |
      | rant     |
      | rent     |
      | vacation |
      | a        |
      | an       |
      | antler   |

     When finding the best match for "ant"
     Then "ant" should be the first match

    Examples:
     | type    |
     | global  |
     | new     |