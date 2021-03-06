{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import time\n",
    "from selenium import webdriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#URL to be scraped\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "response = requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup = bs(response.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Review html format\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Narrow the div and class to see how best to loop through\n",
    "results = soup.find_all('div', class_=\"content_title\")\n",
    "results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# A blank list to hold the headlines\n",
    "news_titles = []\n",
    "# Loop over div elements\n",
    "for result in results:\n",
    "    # Identify the anchor...\n",
    "    if (result.a):\n",
    "        # And the anchor has non-blank text...\n",
    "        if (result.a.text):\n",
    "            # Append thext to the list\n",
    "            news_titles.append(result)\n",
    "news_titles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "finalnewstitles = []\n",
    "# Print only the headlines\n",
    "for x in range(6):\n",
    "    var=news_titles[x].text\n",
    "    newvar = var.strip('\\n\\n')\n",
    "    finalnewstitles.append(newvar)\n",
    "finalnewstitles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Find classification for description paragraph below title\n",
    "presults = soup.find_all('div', class_=\"rollover_description_inner\")\n",
    "presults"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "news_p = []\n",
    "# Loop through the div results to pull out just the text\n",
    "for x in range(6):\n",
    "    var=presults[x].text\n",
    "    newvar = var.strip('\\n\\n')\n",
    "    news_p.append(newvar)\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### JPL Mars Space Images - Featured Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "#executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "#browser = Browser('chrome', **executable_path, headless=False)\n",
    "#browser.visit(url)\n",
    "response = requests.get(url)\n",
    "soup = bs(response.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Review html format\n",
    "print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "imgs = soup.find_all('a', class_=\"fancybox\")\n",
    "imgs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# pull image link\n",
    "feat_img = []\n",
    "for img in imgs:\n",
    "    pic = img['data-fancybox-href']\n",
    "    feat_img.append(pic)\n",
    "\n",
    "featured_image_url = 'https://www.jpl.nasa.gov' + pic\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Weather\n",
    "\n",
    "Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setting up windows browser with chromedriver\n",
    "\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "\n",
    "url='https://twitter.com/marswxreport?lang=en'\n",
    "\n",
    "browser.visit(url)\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing \n",
    "# facts about the planet including Diameter, Mass, etc.\n",
    "\n",
    "#Use Pandas to convert the data to a HTML table string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://space-facts.com/mars/'\n",
    "response = requests.get(url)\n",
    "soup = bs(response.text, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Review html format\n",
    "#print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables = pd.read_html(url)\n",
    "tables[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "marsdf = tables[0]\n",
    "marsdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "marsdf.columns = ['Stat', 'Measurement']\n",
    "marsdf.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "s = pd.Series(marsdf['Stat'])\n",
    "marsdf['Stat'] = s.str.strip(':')\n",
    "marsdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "marsdf = marsdf.set_index('Stat')\n",
    "marsdf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Use to_html method to generate HTML tables from df\n",
    "html_table = marsdf.to_html()\n",
    "html_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Save as html file\n",
    "marsdf.to_html('mars_table.html')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the USGS Astrogeology site [here]\n",
    "# (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution \n",
    "# images for each of Mar's hemispheres.\n",
    "\n",
    "# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.\n",
    "\n",
    "# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the \n",
    "# hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.\n",
    "\n",
    "# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one \n",
    "# dictionary for each hemisphere.\n",
    "\n",
    "# Example:\n",
    "#hemisphere_image_urls = [\n",
    "#    {\"title\": \"Valles Marineris Hemisphere\", \"img_url\": \"...\"},\n",
    "#    {\"title\": \"Cerberus Hemisphere\", \"img_url\": \"...\"},\n",
    "#    {\"title\": \"Schiaparelli Hemisphere\", \"img_url\": \"...\"},\n",
    "#    {\"title\": \"Syrtis Major Hemisphere\", \"img_url\": \"...\"},\n",
    "#]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#URL to be scraped\n",
    "url = 'https://www.usgs.gov/centers/astrogeology-science-center'\n",
    "response = requests.get(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setting up windows browser with chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setting url for alternate browser\n",
    "url = 'https://www.usgs.gov/centers/astrogeology-science-center'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "nextpage_urls = []\n",
    "imgtitles = []\n",
    "base_url = 'https://astrogeology.usgs.gov'\n",
    "\n",
    "# HTML object\n",
    "html = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = bs(html, 'html.parser')\n",
    "\n",
    "# Retrieve all elements that contain hemisphere photo info\n",
    "divs = soup.find_all('div', class_='description')\n",
    "\n",
    "# Iterate through each div to pull titles and make list of hrefs to iterate through\n",
    "counter = 0\n",
    "for div in divs:\n",
    "        # Use Beautiful Soup's find() method to navigate and retrieve attributes\n",
    "    link = div.find('a')\n",
    "    href=link['href']\n",
    "    img_title = div.a.find('h3')\n",
    "    img_title = img_title.text\n",
    "    imgtitles.append(img_title)\n",
    "    next_page = base_url + href\n",
    "    nextpage_urls.append(next_page)\n",
    "    counter = counter+1\n",
    "    if (counter == 4):\n",
    "        break\n",
    "print(nextpage_urls)\n",
    "print(imgtitles)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating loop for high resolution photo on next page\n",
    "\n",
    "my_images=[]\n",
    "for nextpage_url in nextpage_urls:\n",
    "    url = nextpage_url\n",
    "    browser.visit(url)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'html.parser')\n",
    "    link2 = soup.find('img', class_=\"wide-image\")\n",
    "    forfinal = link2['src']\n",
    "    full_img = base_url + forfinal\n",
    "    my_images.append(full_img)\n",
    "    nextpage_urls = []\n",
    "my_images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating final list of dictionaries\n",
    "# values - imgtitles and my_images\n",
    "#ckeys- img_url and title\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "cerberus = {'title':imgtitles[0], 'img_url': my_images[0]}\n",
    "schiaparelli = {'title':imgtitles[1], 'img_url': my_images[1]}\n",
    "syrtis = {'title':imgtitles[2], 'img_url': my_images[2]}\n",
    "valles = {'title':imgtitles[3], 'img_url': my_images[3]}\n",
    "\n",
    "hemisphere_image_urls = [cerberus, schiaparelli, syrtis, valles]\n",
    "print(hemisphere_image_urls)"
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