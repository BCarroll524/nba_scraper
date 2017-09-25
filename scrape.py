from splinter import Browser
import pandas as pd

# open a browser
browser = Browser('chrome')

# width, height
browser.driver.set_window_size(640,480)
browser.visit('https://www.google.com')

search_bar_xpath = '//*[@id="lst-ib"]'

# index 0 to select from the list
search_bar = browser.find_by_xpath(search_bar_xpath)[0]

# two useful methods for crawling are fill() and click()

search_bar.fill("CodingStartups.com")

# Now let's set up code to click the search button
search_button_xpath = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
search_button = browser.find_by_xpath(search_button_xpath)[0]
search_button.click()

# Xpath is used to grab the html element, then using fill 
# and click you can navigate elsewhere

search_results_xpath = '//h3[@class="r"]/a'
search_results = browser.find_by_xpath(search_results_xpath)

scraped_data = []
for search_result in search_results:
	title = search_result.text.encode('utf8') # trust
	link = search_result["href"]
	scraped_data.append((title, link)) # put in tuples


# cleaning the data in search_result.text can sometimes be messy
# .replace() .encode() and .strip() are helpful

df = pd.DataFrame(data=scraped_data, columns=['Title', 'Link'])
df.to_csv("links.csv")