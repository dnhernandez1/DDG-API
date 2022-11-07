""" This program will gather search results from DuckDuckGo API and
verify the accuracy of the returned results.
"""
import requests
import json
import pytest

# List of President last names.
presLastName = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump', 'Biden']
response = requests.get("https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1&no_html=1&skip_disambig=1")


def getText(response):
    data = json.loads(response.text)
    # list of all text words
    dataText = []
    for i in data["RelatedTopics"]:
        dataText.append(i["Text"].split())
    confirm = removeName(dataText)
    return confirm


def removeName(dataText):
    # this will remove the last name of the president that was found in the
    # returned Text field. Once the loop has gone through all names that were
    # returned, if successful, will return a 0 confirming that all names were
    # successfully included in the search results provided by duckduckgo.
    count = len(presLastName)
    textBreakDown = []
    for i in dataText:
        for j in i:
            if j in presLastName:
                presLastName.remove(j)
                textBreakDown.append(j)
                count -= 1
    return count

if __name__ == '__main__':
    print(getText(response))