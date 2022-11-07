from main import *

def testResults():
    response = requests.get(
        "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1&no_html=1&skip_disambig=1")
    test = getText(response)
    assert test == 0