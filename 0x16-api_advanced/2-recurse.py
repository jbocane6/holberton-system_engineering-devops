#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
Hint: The Reddit API uses pagination for separating pages of responses.
Requirements:
    Prototype: def recurse(subreddit, hot_list=[])
    Note: You may change the prototype, but it must be able to be called
        with just a subreddit supplied. AKA you can add a counter,
        but it must work without supplying a starting value in the main.
    If not a valid subreddit, return None.
    Note: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
    Your code will NOT pass if you are using a loop and
    not recursively calling the function! This /can/ be done with a loop
    but the point is to use a recursive function. :)
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing the titles
        of all hot articles for a given subreddit.
    """
    user_agent_str = ('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0)'
                      'Gecko/20190101 Firefox/77.0')
    user_ag = {'User-Agent': user_agent_str}
    session = requests.Session()
    session.headers.update(user_ag)

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    request = session.get(url)
    if (request.status_code == 404):
        return None

    payload = {'limit': 100}
    return recurse_helper(session, url, payload, hot_list)


def recurse_helper(session, url, payload, hot_list):
    """Actual recursive function that stores the titles of all
    hot topics in the actual subreddit"""
    request = session.get(url, params=payload, allow_redirects=False)
    request_data = request.json().get('data')

    post_page = request_data.get('children')
    hot_list.extend([post.get('data').get('title') for post in post_page])

    if (request_data.get('after') is None):
        return hot_list
    payload = {
        'after': request_data.get('after'),
        'limit': 100
    }
    return recurse_helper(session, url, payload, hot_list)
