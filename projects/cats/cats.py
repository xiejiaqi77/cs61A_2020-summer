"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    result = []
    for i in paragraphs:
        if select(i):
            result.append(i)
    if len(result) <= k:
        return ''
    return result[k]

    # END PROBLEM 1


def about(topic):  # ok
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def check(x):
        x = lower(x)
        x = remove_punctuation(x)
        x = split(x)

        for i in topic:
            if i in x:
                return True
        return False

    return check
    # END PROBLEM 2


# about_dogs = about(['dogs', 'hounds'])
# print(about_dogs('Release the Hounds!'))
# print(choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0))


def accuracy(typed, reference):  # ok 先理解题意啊
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if typed == '' or reference == '':
        return 0.0

    len_type = len(typed_words)
    result = 0
    i = 0
    while i < len_type and i < len(reference_words):
        if typed_words[i] == reference_words[i]:
            result += 1
        i = i + 1

    return round(result / len_type * 100, 2)


# print(accuracy('A Cute Dog!', 'Cute Dog.'))

# END PROBLEM 3


def wpm(typed, elapsed):  # ok
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    n_char = len(typed) / 5
    speed = n_char / elapsed * 60
    return speed
    # END PROBLEM 4


# print(wpm("a  b  c  d", 5))

import sys


def autocorrect(user_word, valid_words, diff_function, limit):  # ok
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    small_diff = sys.maxsize
    closet_one = user_word
    for word in valid_words:
        if diff_function(user_word, word, limit) < small_diff and diff_function(user_word, word, limit) <= limit:
            # the boundary is really important "<= limit" , if there is only "< limit", some result will not be taken into count
            small_diff = diff_function(user_word, word, limit)
            closet_one = word
    return closet_one

    # END PROBLEM 5


# abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
# print(autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10))


def shifty_shifts(start, goal, limit, i=0, result=0):  # ok
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    '''
    ##iterative way, which is baned 
    result = 0
    i = 0
    l_start = list(start)
    l_goal = list(goal)
    while i < min(len(start), len(goal)):
        if l_goal[i] != l_start[i]:
            result = result + 1
            if result > limit:
                return limit + 1
        i = i + 1
    return result + abs(l_start-l_goal)

    '''
    l_start = list(start)
    l_goal = list(goal)
    if result > limit:
        return limit + 1
    if i == min(len(start), len(goal)) - 1:
        if l_goal[i] != l_start[i]:
            return result + abs(len(l_start) - len(l_goal)) + 1
        else:
            return result + abs(len(l_start) - len(l_goal))
    else:
        if l_goal[i] != l_start[i]:
            result += 1
            i += 1
            return shifty_shifts(start, goal, limit, i, result)
        else:
            i += 1
            return shifty_shifts(start, goal, limit, i, result)

    # END PROBLEM 6


def meowstake_matches(start, goal, limit):   # ok still need review
    """A diff function that computes the edit distance from START to GOAL."""
    n1 = len(start)
    n2 = len(goal)
    #dp = [[0 for i in range(n1 + 1)] for n in range(n2 + 1)]
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    if n1 * n2 == 0:
        return n1 + n2

    for i in range(n1 + 1):
        dp[i][0] = i

    for j in range(n2 + 1):
        dp[0][j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            left = dp[i - 1][j] + 1
            down = dp[i][j - 1] + 1
            left_down = dp[i - 1][j - 1]
            if start[i - 1] != goal[j - 1]:
                left_down += 1
            dp[i][j] = min(left, down, left_down)

    if dp[n1][n2] > limit:
        return limit + 1

    return dp[n1][n2]


#(meowstake_matches('start', 'goal', 3))

"""
if ______________: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    else:
        add_diff = ...  # Fill in these lines
        remove_diff = ... 
        substitute_diff = ... 
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
"""


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send): # ok 一把过  -> progress
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    assert len(typed) <= len(prompt)
    # END PROBLEM 8
    i = 0
    k = 0
    while i < len(typed):
        if typed[i] == prompt[i]:
            k = k + 1
            i = i + 1
        else:
            break
    result = k/len(prompt)
    dic = {'id': id, 'progress': result}
    send(dic)
    return result





def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words): # ok -----> game(words, times) 一把过
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    num_play = len(times_per_player)
    times = []
    for i in times_per_player:
        times_n = []
        t = 1
        while t < len(i):
            times_n.append(i[t]-i[t-1])
            t = t + 1
        times.append(times_n)
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):  # ok
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))  # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"


    """ 
    # the first solution, which can not solve the duplicate case
    result = []
    for one in players:
        tem_result = []
        for char in words:
            min = 0
            for other in players:
                if time(game, one, char) > time(game, other, char):
                    min = min + 1

            if min == 0:
                tem_result.append(word_at(game, char))

        result.append(tem_result)

    return result
    
    """
    dic = {}
    for char in words:

        i = 0
        min_one = 0
        min = time(game, i, char)
        while i < len(all_times(game)):
            if time(game, i, char) < min:
                min_one = i
                min = time(game, i, char)
            i = i + 1


        dic[word_at(game, char)]=min_one

    result = []
    for one in players:
        tem = []
        for i in dic:
            if dic[i] == one:
                tem.append(i)
        result.append(tem)

    return result
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])


enable_multiplayer = False  # Change to True when you



# p0 = [2, 2, 3]
# p1 = [6, 1, 3]
# print(fastest_words(game(['What', 'great', 'luck'], [p0, p1])))
##########################
# Extra Credit #
##########################

key_distance = get_key_distances()


def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower()  # converts the string to lowercase
    goal = goal.lower()  # converts the string to lowercase

    # BEGIN PROBLEM EC1
    "*** YOUR CODE HERE ***"
    dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x':23, 'y': 24, 'z': 25}
    # END PROBLEM EC1
    if abs(dic[start]-dic[goal])>limit:
        return limit + 1
    else:
        return abs(dic[start]-dic[goal])


def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}

    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return memoized


key_distance_diff = count(key_distance_diff)


def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    "*** YOUR CODE HERE ***"
    # END PROBLEM EC2


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
