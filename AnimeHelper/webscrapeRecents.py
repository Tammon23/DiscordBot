import os
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from helperFunctions import folderMaker


class Weeb:
    def __init__(self):
        pass

    def parseWebsites(self):
        parsed_sites = {}

        # parsing structure for wcostream.com
        wcoWebsite = "https://www.wcostream.com/last-50-recent-release"

        # opening up connection and grabbing the page
        uClient = urlopen(wcoWebsite)

        # reading the content into a var then closing the client
        parsed_sites["www.wcostream.com"] = (uClient.read())
        uClient.close()

        return parsed_sites


    def scrapeWebsites(self, websites_to_scrape):
        scraped_websites = {}
        for website_HTML in websites_to_scrape:

            stew = soup(websites_to_scrape[website_HTML], "html.parser")

            # in this case we are accessing the top50anime page
            recentAnime = stew.findAll("div", {"class": "menulaststyle"})

            result = recentAnime[0].findAll("li")

            episodedata = {}
            for row in result:
                # key = episode name, value = url for episde
                episodedata[row.a.text.strip()] = row.a["href"]

            scraped_websites[website_HTML] = episodedata.copy()

        return scraped_websites


    def updateJSON(self, newData):
        if os.path.exists("config/recentAnimeQuery.JSON"):
            with open("config/recentAnimeQuery.JSON", 'r') as inFile:
                oldData = json.load(inFile)
                # print(oldData["www.wcostream.com"].keys())

                # Iterating through each website with anime listings
                for website in oldData:
                    numNewTitles = set(newData[website].keys()) - set(oldData[website].keys())
                    keysToRemove = list(oldData[website].keys())[-len(numNewTitles):]

                    # print(keysToRemove)
                    # print(oldData[website].keys())
                    # print(newData[website].keys())

                    # Making space for new entries by removing n old entries
                    for key in keysToRemove:
                        del oldData[website][key]

                    # entries that a shared in both lists
                    titles_shared = set(newData[website].keys()) & set(oldData[website].keys())
                    for title in titles_shared:
                        del newData[website][title]

                    # merging old list with new list
                    newData[website].update(oldData[website])

        # saving the results to a file
        with open("config/recentAnimeQuery.JSON", 'w') as outFile:
            json.dump(newData, outFile)

    def runFile(self):
        folderMaker("config")

        parsed_websites = self.parseWebsites()

        results = self.scrapeWebsites(parsed_websites)

        self.updateJSON(results)

        print("fuck me")
#
# if __name__ == "__main__":
#     folderMaker("config")
#
#     parsed_websites = parseWebsites()
#
#     results = scrapeWebsites(parsed_websites)
#
#     updateJSON(results)