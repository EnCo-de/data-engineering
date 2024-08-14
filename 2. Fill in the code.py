# Cheap Crowdfunding Problem
#
# There is a crowdfunding project that you want to support. This project
# gives the same reward to every supporter, with one peculiar condition:
# the amount you pledge must not be equal to any earlier pledge amount.
#
# You would like to get the reward, while spending the least amount > 0.
#
# You are given a list of amounts pledged so far in an array of integers.
# You know that there is less than 100,000 of pledges and the maximum
# amount pledged is less than $1,000,000.
#
# Implement a function find_min_pledge(pledge_list) that will return
# the amount you should pledge.

def find_min_pledge(pledge_list):
  amounts = [False] * (len(pledge_list) + 1)
  for num in pledge_list:
    if 0 < num <= len(pledge_list):
      amounts[num] = True
  the_least_amount = 1
  while the_least_amount < len(amounts) and amounts[the_least_amount]:
    the_least_amount += 1
  return the_least_amount

assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1



# Extract Titles from RSS feed
#
# Implement get_headlines() function. It should take a url of an RSS feed
# and return a list of strings representing article titles.

import urllib.request
import xml.etree.ElementTree as ET

google_news_url="https://news.google.com/news/rss"


def get_headlines(rss_url):
    """
    @returns a list of titles from the rss feed located at `rss_url`
    """
    with urllib.request.urlopen(rss_url) as response:
        if response.status == 200:
            xml = response.read()
            # create element tree object by importing data 
            # directly from a string
            tree = ET.fromstring(xml)
            path = './channel/item/title'
            newsitems = [news.text for news in tree.findall(path)] 
            return newsitems
    return []


print(get_headlines(google_news_url))
