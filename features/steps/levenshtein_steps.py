import random
from behave import given, when, then
from howabout import get_levenshtein


@given('two long strings')
def step_two_long_strings(context):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    random_str = lambda size: [random.choice(alphabet) for _ in range(0, size)]

    context.first = random_str(1024)
    context.second = random_str(1024)


@given('two empty strings')
def step_two_empty_strings(context):
    context.first = ''
    context.second = ''


@when('we compare them')
def step_compare_two_strings(context):
    context.distance = get_levenshtein(context.first, context.second)


@then('the interpreter should not overflow')
def step_assert_no_overflow(context):
    assert not context.failed


@given('"{string}" and the empty string')
def step_a_string_and_the_emtpy_string(context, string):
    context.first = string
    context.second = ''

@given('a string "{string}"')
def step_a_string(context, string):
    context.first = string


@when('we compare it to itself')
def step_compare_string_to_itself(context):
    string = context.first, context.first
    context.distance = get_levenshtein(string, string)


@then('the distance is {distance:d}')
def step_assert_distance(context, distance):
    assert context.distance == distance


@given('the first string "{first}" and the second string "{second}" starting with "{prefix}"')
def step_impl2(context, first, second, prefix):
    """
    :type context behave.runner.Context
    :type first str
    :type second str
    :type prefix str
    """
    context.first = first
    context.second = second