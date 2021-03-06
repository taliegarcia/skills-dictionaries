# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    unique_wc = {} # initialize empty dictionary

    for word in string1.split(" "):  # split string by word into iterable list
    	# optional: remove punctuation and case from words:
    	# word = word.rstrip("\n,.").lower() 
		
		if word in unique_wc: 	# if the word is already in the dict, increase count value by one
			unique_wc[word] += 1
		else:
			unique_wc[word] = 1 # else initialize key with count of 1, for the first time we see the word!
    	
    return unique_wc





def common_items(list1, list2):	
	"""Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
	# super_list = list1 + list2 --> Don't need! w00t. see below.
	item_counts = {} # init empty dict
	common_list = [] # init empty list

	for i in (list1 + list2): # pretty cool iteration and looks good too
		item_counts[i] = item_counts.get(i,0) + 1 
		# if item is not in the list, it is now defined here with default value of 0, then adding 1 for its 1 appearance in the list!
		# if the item is already in the list, .get ignores the default 0 value and returns the currnt value, increasing by 1 per appearnce on the list
		if item_counts[i] > 1: # this will append an item to the common_list everytime it appears more than once
			common_list.append(i)		
	
	return common_list # returns sorted list of shared items

 


def unique_common_items(list1, list2):
	"""Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
	item_counts = {} 
	unique_list = []

	for i in (list1 + list2):
		item_counts[i] = item_counts.get(i,0) + 1 

	# item_counts = { i: 1 for i in (list1 + list2) if item_counts.get(1,0) = 0}
	unique_list = [i for i in item_counts if item_counts[i] > 1]
	
	return unique_list

def sum_zero(list1):
	pairs_summing_zero = {}
	for idx in range(len(list1)):
	    copy_list = list1[:] # creates a copy to manipulate
	    start_num = copy_list.pop(idx) 
	    	# pops out the value we are looking at now
	        # copy_list are the numbers we will be testing our popped number with to sum zero
	        # and binds that starting number to a variable
	    for num in copy_list:
	    	# I think there has to be a way more efficient way to do this
	    	# seems like I shouldnt have to test the sum of every number
	    	# especially if there is already a key for that number pair
	    	# one solution would be doing the sort formatting business 
	    	# on the tuple pair before I do in the if statement below (pair_list.sort())
	    	# then if (first, second) tuple-key is in dictionary, could skip the if == 0 statement and actions (break)
	    	# but then that would still be computing all..
	        if start_num + num == 0:
	        	pair_list = [start_num, num] # put in list (could not chain these methods so all separate lines)
	        	pair_list.sort() # so the values can be sorted uniformly
	        	first, second = pair_list # unpack list to put in dictionary as tuple
	        	pairs_summing_zero.setdefault((first, second),True) 
	        	# previously, thinking I could avoid repetition by popping out pairs from the copy_list that I already knew were sume zero: copy_list.pop(copy_list.index(num))
	
	# list comprehension on dictionary to format answer
	zero_pair_list = [[pair[0], pair[1]] for pair in pairs_summing_zero.keys()]
	# prevoiusly, return pairs_summing_zero.keys() --> not exactly the right format
	return zero_pair_list

	# """Return list of x,y number pair lists from a list where x+y==0

 #    Given a list of numbers, add up each individual pair of numbers.
 #    Return a list of each pair of numbers that adds up to 0.


 #    For example:

 #        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
 #        [[-2, 2], [-1, 1]]

 #    This should always be a unique list, even if there are
 #    duplicates in the input list:

 #        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
 #        [[-2, 2], [-1, 1]]

 #    Of course, if there are one or more zeros to pair together,
 #    that's fine, too:

 #        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
 #        [[-2, 2], [-1, 1], [0, 0]]

 #    """




def find_duplicates(words):
	dupes_removed = [] 

	for word in string1: 
		if word not in dupes_removed: 	
			dupes_removed.append(word)

	return dupes_removed
#     """Given a list of words, return the list with duplicates removed.

#     For example:

#         >>> sorted(find_duplicates(
#         ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['a', 'is', 'rose']

#     You should treat differently-capitalized words as different:

#         >>> sorted(find_duplicates(
#         ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['Rose', 'a', 'is', 'rose']

#     """





def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    words_by_length = {}

    for word in words:
    	words_by_length.setdefault(len(word), []).append(word)

    return sorted(words_by_length.items())


def pirate_talk(phrase):
	proper_english = ['sir', 'hotel', 'student', 'boy', 'madam',
		'professor',  'restaurant', 'your', 'excuse', 'students', 'are', 
		'lawyer', 'the', 'restroom', 'my', 'hello', 'is', 'man']

	pirate_english = ['matey', 'fleabag inn', 'swabbie', 'matey', 'proud beauty', 'foul blaggart', 'galley', 'yer', 'arr', 'swabbies', 'be', 'foul blaggart', "th'", 'head', 'me', 'avast', 'be', 'matey']

	pirate_dictionary = { w : pirate_english[proper_english.index(w)] for w in proper_english}

	pirate_phrase = ""
	for word in phrase:
		pirate_phrase = pirate_phrase + pirate_dictionary.get(word, word)

	return pirate_phrase

#Translate phrase to pirate talk.

# #     Given a phrase, translate each word to the Pirate-speak equivalent.
# #     Words that cannot be translated into Pirate-speak should pass through
# #     unchanged. Return the resulting sentence.

# #     Here's a table of English to Pirate translations:

    # English     Pirate
    # ----------  ----------------
    # sir         matey
    # hotel       fleabag inn
    # student     swabbie
    # boy         matey
    # madam       proud beauty
    # professor   foul blaggart
    # restaurant  galley
    # your        yer
    # excuse      arr
    # students    swabbies
    # are         be
    # lawyer      foul blaggart
    # the         th'
    # restroom    head
    # my          me
    # hello       avast
    # is          be
    # man         matey

# #     For example:

# #         >>> pirate_talk("my student is not a man")
# #         'me swabbie be not a matey'

# #     You should treat words with punctuation as if they were different
# #     words:

# #         >>> pirate_talk("my student is not a man!")
# #         'me swabbie be not a man!'

# #     """

# #     return ""

def adv_word_length_sorted_words(words):
	abcwords_by_length = {}

	for word in words:
		abcwords_by_length.setdefault(len(word), []).append(word).sort()

	return sorted(abcwords_by_length.items())

# #     """Given list of words, return list of ascending [(len, [sorted-words])].

# #     Given a list of words, return a list of tuples, ordered by word-length.
# #     Each tuple should have two items--the length of the words for that
# #     word-length, and the list of words of that word length. The list of words
# #     for that length should be sorted alphabetically.

# #     For example:
# 
# #         >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
# #         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

# #     """

# #     return []


# ##############################################################################
# # You can ignore everything after here

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
