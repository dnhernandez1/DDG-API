""" This program will gather search results from DuckDuckGo API and
verify the accuracy of the returned results.
"""
import requests
import json
"""
params = {
    "engine": "duckduckgo",
    "q": "Presidents of the united states",
    "output": "JSON",
    "api_key": "994b429f5f2d6895d2f69d0bfb16d7a5f9bb1f55c73da8ae8882fead2e3a33f8"
}
"""
response = requests.get(
    "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json&pretty=1&no_html=1&skip_disambig=1")
print(response.status_code)
print(response.text)
data = json.loads(response.text)
