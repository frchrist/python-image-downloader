"""
@author : christian Fare
@username : darich0B1100
@licence : Free

"""
import os
import cloudscraper as csp
from bs4 import BeautifulSoup as bs

base_site = "https://wallpapercave.com"
base_url = "https://wallpapercave.com/cool-blue-wolf-wallpapers"
extention = ".jpg"
download_class = "download"

if(not os.path.exists(download_class)):
    os.mkdir(download_class)
scraper = csp.create_scraper()


class wallpapercave:
    def __init__(self, cat_id):
        self.category = cat_id
        self.base_site = "https://wallpapercave.com"
        self.relative_url = self.base_site + "/" + self.category
        self.download_class = "download"
        self.file_extension = ".jpg"

        self.scraper = csp.create_scraper()
        self.process_request()

    def process_request(self):

        get_response = self.scraper.get(self.relative_url)


        bs_ins = bs(get_response.text, "html.parser")
        links  = bs_ins.find_all("a", class_=self.download_class)



        for link in links:
            llink = self.base_site+link.get("href")
            name = llink.split("/")[-1]+self.file_extension
            # donwload section
         
            data = self.scraper.get(llink)
            data = data.content
            with open(self.download_class+"/"+name, "wb") as files:
                files.write(bytes(data))
                print(f"[+] downloading {name} done. ")

class unsplash:
    def __init__(self, current_link):
        self.current_link = current_link
        self.file_extension = ".jpg"

        self.scraper = csp.create_scraper()
        key_word = current_link.split("/")[-1]
        if(not os.path.exists(key_word)):
            os.mkdir(download_class+"/"+key_word)
        self.download_folder = download_class+"/"+key_word

        self.process_request()

    def process_request(self):

        get_response = self.scraper.get(self.current_link)


        bs_ins = bs(get_response.text, "html.parser")
        links  = bs_ins.find_all("a", title="Download photo")



        for link in links:
            llink = link.get("href")
            name = llink.split("/")[-2]+self.file_extension
            # donwload section
            data = self.scraper.get(llink)
            data = data.content
            with open(self.download_folder+"/"+name, "wb") as files:
                files.write(bytes(data))
                print(f"[+] downloading {name} done. ")


#init = wallpapercave("astronaut-wallpapers")
init = unsplash("https://unsplash.com/s/photos/background")


