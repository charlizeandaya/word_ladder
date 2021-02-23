#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder
    between the two words,
    the function returns `None`.
    '''

    with open(dictionary_file) as f:
        dictionary_file_handle = f.readlines()

    dictionary_list = []
    for item in dictionary_file_handle:
        dictionary_list.append(item.strip())

    if start_word == end_word:
        return list([start_word])

    stack = []
    stack.append(start_word)
    queue = deque([])
    queue.append(stack)

    while queue:
        word_list = queue.popleft()
        for word in list(dictionary_list):
            if _adjacent(word_list[-1], word):
                if word == end_word:
                    word_list.append(word)
                    return word_list
                word_list_copy = copy.copy(word_list)
                word_list_copy.append(word)
                queue.append(word_list_copy)
                dictionary_list.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    if (len(ladder) == 0):
        return False
    for i in range(0, len(ladder) - 1):
        if (not _adjacent(ladder[i], ladder[i + 1])):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) != len(word2):
        return False

    mismatch_index = []

    for index, letter in enumerate(word1):
        if letter is not word2[index]:
            mismatch_index.append(index)

    if len(mismatch_index) == 1:
        return True
    else:
        return False
