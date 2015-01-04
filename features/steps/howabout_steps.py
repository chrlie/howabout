from behave import given, when, then

import howabout
from howabout import Matcher


class GlobalMatcher(object):
    def all_matches(self, *args, **kwargs):
        return howabout.all_matches(*args, **kwargs)

    def best_matches(self, *args, **kwargs):
        return howabout.best_matches(*args, **kwargs)

    def best_match(self, *args, **kwargs):
        return howabout.best_match(*args, **kwargs)


@given('a "{type}" matcher and some strings')
def step_impl(context, type):
    if type == 'global':
        matcher = GlobalMatcher()
    elif type == 'new':
        matcher = Matcher()
    else:
        raise ValueError(type)

    context.matcher = matcher
    context.choices = map(lambda row: row[0], iter(context.table))


@when('finding the best match for "{target}"')
def step_impl(context, target):
    context.target = target
    context.best = context.matcher.best_match(target, context.choices)


@then('"{expected}" should be the first match')
def step_impl(context, expected):
    assert context.best == expected