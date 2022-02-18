#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
Requirements:
    Prototype: def count_words(subreddit, word_list)
    Note: You may change the prototype, but it must be able to be called
        with just a subreddit supplied and a list of keywords.
        AKA you can add a counter or anything else, but the function must work
        without supplying a starting value in the main.
    If word_list contains the same word (case-insensitive), the final count
        should be the sum of each duplicate (example below with java)
    Results should be printed in descending order, by the count,
        and if the count is the same for separate keywords, they should then be
        sorted alphabetically (ascending, from A to Z). Words with no matches
        should be skipped and not printed. Words must be printed in lowercase.
    Results are based on the number of times a keyword appears, not titles
        it appears in. java java java counts as 3 separate occurrences of java.
    To make life easier, java. or java! or java_ should not count as java
    If no posts match or the subreddit is invalid, print nothing.
    Note: Invalid subreddits may return a redirect to search results.
        Ensure that you are NOT following redirects.
    Your code will NOT pass if you are using a loop and not recursively calling
        the function! This /can/ be done with a loop but the point is to use
        a recursive function. :)
Disclaimer: number presented in this example cannot be accurate now - Reddit is
    hot articles are always changing.
"""
from requests import get


def count_words(subreddit, word_list, payload={}, hot_list=[]):
    """
    Queries the Reddit API, parses the title of all hot articles,
        and prints a sorted count of given keywords
    """
    if payload == {}:
        payload = {'limit': 100}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent_str = ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0)'
                      'Gecko/20190101 Firefox/77.0')
    user_ag = {'User-Agent': user_agent_str}

    request = get(url, headers=user_ag)
    if (request.status_code == 404):
        return

    request = get(url, headers=user_ag, params=payload)
    request_data = request.json().get('data')

    post_page = request_data.get('children')
    hot_list.extend([post.get('data').get('title') for post in post_page])

    if (request_data.get('after') is not None):
        payload = {
            'after': request_data.get('after'),
            'limit': 100
        }
        return count_words(subreddit, word_list, payload, hot_list)

    word_list = [word.lower() for word in word_list]
    freq_dict = {word: 0 for word in word_list}
    for title in hot_list:
        title_words = title.lower().split(' ')
        for word in word_list:
            freq_dict[word] += title_words.count(word)

    freq_list = [(key, val) for key, val in freq_dict.items() if val != 0]
    for entry in sorted(freq_list, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(entry[0], entry[1]))
