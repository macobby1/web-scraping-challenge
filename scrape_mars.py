{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dependencies\n",
    "from bs4 import BeautifulSoup \n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Choose the executable path to driver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit Nasa news url\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "#HTML object\n",
    "html = browser.html\n",
    "\n",
    "#Parse HTML\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "slide_element = soup.select_one(\"ul.item_list li.slide\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\"><a href=\"/news/8654/how-nasas-perseverance-mars-team-adjusted-to-work-in-the-time-of-coronavirus/\" target=\"_self\">How NASA's Perseverance Mars Team Adjusted to Work in the Time of Coronavirus </a></div>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_element.find(\"div\", class_=\"content_title\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How NASA's Perseverance Mars Team Adjusted to Work in the Time of Coronavirus \n"
     ]
    }
   ],
   "source": [
    "#Scrape the news\n",
    "news_title = slide_element.find(\"div\", class_=\"content_title\").get_text()\n",
    "print(news_title)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<bound method Tag.get_text of <div class=\"article_teaser_body\">Like much of the rest of the world, the Mars rover team is pushing forward with its mission-critical work while putting the health and safety of their colleagues and community first.</div>>\n"
     ]
    }
   ],
   "source": [
    "#scrape the latest paragraph text\n",
    "news_paragraph = slide_element.find(\"div\", class_=\"article_teaser_body\").get_text\n",
    "print(news_paragraph)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# JPL MARS Space"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Choose the executable path for NASA JPL\n",
    "executable_path = {\"executable_path\":\"chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit the Nasa JPL (Jet Propulsion Laboratory) Site\n",
    "url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image_button = browser.find_by_id(\"full_image\")\n",
    "full_image_button.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.is_element_present_by_text(\"more info\", wait_time=1)\n",
    "more_info_element = browser.find_link_by_partial_text(\"more info\")\n",
    "more_info_element.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "image_soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/largesize/PIA19046_hires.jpg'"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_url = image_soup.select_one(\"figure.lede a img\").get(\"src\")\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA19046_hires.jpg\n"
     ]
    }
   ],
   "source": [
    "img_url = f\"https://www.jpl.nasa.gov{img_url}\"\n",
    "print(img_url)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit Mars Weather Twitter Account\n",
    "executable_path = {\"executable_path\":\"chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless=False)\n",
    "url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML Object \n",
    "html_weather = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html_weather, 'html.parser')\n",
    "\n",
    "# Find all elements that contain tweets\n",
    "latest_tweets = soup.find_all('div', class_='js-tweet-text-container')\n",
    "\n",
    "# Retrieve all elements that contain news title in the specified range\n",
    "# Look for entries that display weather related words to exclude non weather related tweets \n",
    "for tweet in latest_tweets: \n",
    "    weather_tweet = tweet.find('p').text\n",
    "    if 'Sol' and 'pressure' in weather_tweet:\n",
    "        print(weather_tweet)\n",
    "        break\n",
    "    else: \n",
    "        pass\n",
    "   "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit the Mars Facts site\n",
    "mars_df = pd.read_html(\"https://space-facts.com/mars/\")[0]\n",
    "print(mars_df)\n",
    "mars_df.columns=[\"Parameter\", \"Value\"]\n",
    "mars_df.set_index(\"Parameter\", inplace = True)\n",
    "mars_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">   <thead>     <tr style=\"text-align: right;\">       <th></th>       <th>Value</th>     </tr>     <tr>       <th>Parameter</th>       <th></th>     </tr>   </thead>   <tbody>     <tr>       <th>Equatorial Diameter:</th>       <td>6,792 km</td>     </tr>     <tr>       <th>Polar Diameter:</th>       <td>6,752 km</td>     </tr>     <tr>       <th>Mass:</th>       <td>6.39 × 10^23 kg (0.11 Earths)</td>     </tr>     <tr>       <th>Moons:</th>       <td>2 (Phobos &amp; Deimos)</td>     </tr>     <tr>       <th>Orbit Distance:</th>       <td>227,943,824 km (1.38 AU)</td>     </tr>     <tr>       <th>Orbit Period:</th>       <td>687 days (1.9 years)</td>     </tr>     <tr>       <th>Surface Temperature:</th>       <td>-87 to -5 °C</td>     </tr>     <tr>       <th>First Record:</th>       <td>2nd millennium BC</td>     </tr>     <tr>       <th>Recorded By:</th>       <td>Egyptian astronomers</td>     </tr>   </tbody> </table>'"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mars_html_table = mars_df.to_html()\n",
    "mars_html_table = mars_html_table.replace(\"\\n\",\" \")\n",
    "mars_html_table"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Hemisphere"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Visit the USGS Astrogeology Science Center Site\n",
    "hemispheres_url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(hemispheres_url)\n",
    "#HTML Object\n",
    "html = browser.html\n",
    "\n",
    "#Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, \"html.parser\")\n",
    "\n",
    "#Create empty list for hemisphere urls\n",
    "hemisphere_image_url = []\n",
    "\n",
    "#Retrive all items that contain mars hemispheres information\n",
    "products = soup.find(\"div\", class_ = \"result-list\" )\n",
    "hemispheres = products.find_all(\"div\", class_=\"item\")\n",
    "\n",
    "# Loop through to get information for all hemispheres\n",
    "for hemisphere in hemispheres:\n",
    "    title = hemisphere.find(\"h3\").text\n",
    "    title = title.replace(\"Enhanced\", \"\")\n",
    "    end_link = hemisphere.find(\"a\")[\"href\"]\n",
    "    \n",
    "    #Retrieve image source\n",
    "    image_link = \"https://astrogeology.usgs.gov/\" + end_link    \n",
    "    browser.visit(image_link)\n",
    "    \n",
    "    html = browser.html\n",
    "    \n",
    "    #Parse HTML with Beautiful Soup\n",
    "    soup=BeautifulSoup(html, \"html.parser\")\n",
    "    downloads = soup.find(\"div\", class_=\"downloads\")\n",
    "    image_url = downloads.find(\"a\")[\"href\"]\n",
    "    \n",
    "    #Append retrieved information into list of dictionaries\n",
    "    hemisphere_image_url.append({\"title\": title, \"img_url\": image_url})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere ',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Display hemisphere urls\n",
    "hemisphere_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
