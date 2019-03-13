import random

from django.shortcuts import render
from django.views.decorators.cache import never_cache


@never_cache
def index(request):
    return render(
        request,
        'index.html',
        {'quote': random.choice(quotes)},
    )


quotes = [
    'It is by logic that we prove, but by intuition that we discover.',
    'To know how to criticize is good, to know how to create is better.',
    'Thought is only a gleam in the midst of a long night. But it is this gleam which is everything.',
    (
        'The principal aim of mathematical education is to develop certain faculties of the mind, and among these '
        + 'intuition is not the least precious.'
    ),
    (
        'Time and Space … It is not nature which imposes them upon us, it is we who impose them upon nature because '
        + 'we find them convenient.'
    ),
]
