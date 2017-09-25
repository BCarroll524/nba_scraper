from splinter import Browser
import pandas as pd

browser = Browser('chrome')
browser.driver.set_window_size(1000,1000)
browser.visit('https://www.nba.com')

search_bar_xpath = '//*[@id="block-mainnavigation"]/nav/div[3]/ul[2]/li[2]/a'
search_bar = browser.find_by_xpath(search_bar_xpath)[0]
search_bar.click()

search_xpath = '//*[@id="block-league-content"]/div/search/search-results/div[1]/form/input[1]'
search = browser.find_by_xpath(search_xpath)[0]
search.fill("chris paul")

search_button_xpath = '//*[@id="block-league-content"]/div/search/search-results/div[1]/form/input[2]'
search_button = browser.find_by_xpath(search_button_xpath)[0]
search_button.click()

# get player info
player_img_xpath = '//*[@id="block-league-content"]/div/search/search-results/div[1]/div/div/section/img'
player_img = browser.find_by_xpath(player_img_xpath)[0]
img_url = player_img["src"]
print(img_url)