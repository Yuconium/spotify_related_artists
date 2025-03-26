
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
from bs4 import BeautifulSoup

import time
import json

class Driver:
	def __init__(self, name, id):
	
		self.driver = driver = webdriver.Firefox()
		self.site = ""
		self.soup = ""
		self.start_artist = name
		self.dicts = []
		self.first_time = True
		counter = 1

		self.get_site("https://open.spotify.com/artist/"+ id +"/related")

		self.get_info(self.start_artist)
		print(self.dicts)
		print()
		for i in self.dicts[0][self.start_artist]:

			self.get_site("https://open.spotify.com/artist/" + i["ID"] + "/related")
			self.get_info(i["name"])
			print(counter)
			counter += 1		
		


		self.write_data(self.dicts)
		self.driver.close()	
		print("DONE!")

	def get_site(self, link):
		self.driver.get(link)

		if self.first_time == True:
			blocker = getpass.getpass("Press Enter to continue")
			self.first_time = False
		else:
			pass
		time.sleep(10)
		self.site = self.driver.page_source

	def get_info(self, name):
		print(name)
		self.soup = BeautifulSoup(self.site, features="lxml")
		raw_text = self.soup.find_all("a", {"class": "Gi6Lr1whYBA2jutvHvjQ"})

		list = []
		for i in raw_text:
		
			
			list.append({"name": i.text, "ID": i["href"][8:]})
			

		self.dicts.append({name: list})

	def write_data(self, data):
		with open(self.start_artist + ".json", "w") as f:
			json.dump(data, f)

	
if __name__ == "__main__":
	name = input()
	id = input()
	driver = Driver (name, id)