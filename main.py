from bs4 import BeautifulSoup
import requests

# allows user to input search
search = input("Enter for:")
# attaches search to url
params = {"q": search}
# creates request for url
r = requests.get("http://www.bing.com/search", params=params)

# variable is created to get all information on the search page
soup = BeautifulSoup(r.text, "html.parser")
# this narrows down the text information to specific items
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

# loops though all of the content to find a tags and attributes of href
for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]


    # conditional statement that says if the item has an atag and a href then print the atag and href
    if item_text and item_href:
        print(item_text)
        print(item_href)
        # parent.parent goes back to the parent of the parent. Parsing up and down

        # print("summary:", item.find("a").parent.parent.find("p").text)
        # parse sideways
        children = item.find("h2")
        print("Next sibling of the h2:", children.next_sibling)
