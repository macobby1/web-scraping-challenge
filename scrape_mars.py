#Dependencies
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd
import requests

#Choose the executable path to driver
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

#Visit Nasa news url
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

#HTML object
html = browser.html

#Parse HTML
soup = BeautifulSoup(html, 'html.parser')
slide_element = soup.select_one("ul.item_list li.slide")
slide_element.find("div", class_="content_title")

#Scrape the news
news_title = slide_element.find("div", class_="content_title").get_text()
print(news_title)

#scrape the latest paragraph text
news_paragraph = slide_element.find("div", class_="article_teaser_body").get_text
print(news_paragraph)

#Choose the executable path for NASA JPL
executable_path = {"executable_path":"chromedriver.exe"}
browser = Browser("chrome", **executable_path)

#Visit the Nasa JPL (Jet Propulsion Laboratory) Site
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)

full_image_button = browser.find_by_id("full_image")
full_image_button.click()

browser.is_element_present_by_text("more info", wait_time=1)
more_info_element = browser.find_link_by_partial_text("more info")
more_info_element.click()

html = browser.html
image_soup = BeautifulSoup(html, "html.parser")

img_url = image_soup.select_one("figure.lede a img").get("src")
img_url

img_url = f"https://www.jpl.nasa.gov{img_url}"
print(img_url)

#Dependencies
from twitterscraper import query_tweets
from twitterscraper import query_tweets_from_user as q

#Visit Mars Twitter account("MarsWxReport")
mars_tweets = q(user='MarsWxReport', limit=5)
mars_tweets_df=pd.DataFrame(t.__dict__ for t in mars_tweets)

#Display tweets
mars_tweets_df.head()
mars_weather = mars_tweets_df.loc[0,'text']
mars_weather

#Visit the Mars Facts site
mars_df = pd.read_html("https://space-facts.com/mars/")[0]
print(mars_df)
mars_df.columns=["Description", "Value"]
mars_df.set_index("Description", inplace = True)
mars_df

mars_html_table = mars_df.to_html()
mars_html_table = mars_html_table.replace("\n"," ")
mars_html_table

#Visit the USGS Astrogeology Science Center Site
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
#HTML Object
html = browser.html

#Parse HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

#Create empty list for hemisphere urls
hemisphere_image_url = []

#Retrive all items that contain mars hemispheres information
products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

# Loop through to get information for all hemispheres
for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    
    #Retrieve image source
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    
    html = browser.html
    
    #Parse HTML with Beautiful Soup
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    
    #Append retrieved information into list of dictionaries
    hemisphere_image_url.append({"title": title, "img_url": image_url})

#Display hemisphere urls
hemisphere_image_url
