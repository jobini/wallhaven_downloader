<h1><b>Wallhaven Downloader</b></h1>

<h2><b>Synopsis</b></h2>

These are two Python scripts to either (a) completely scrape or (b) search and download wallpapers, with pause/resume capability, from [Wallhaven](alpha.wallhaven.cc). They're implemented without using browser automation or a headless browser.

<h2><b>Requirements</b></h2>

1. Python version 2.7.6+ 
2. [requests](https://pypi.python.org/pypi/requests)
3. [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)
4. [clint](https://pypi.python.org/pypi/clint)

<h2><b>Usage</b></h2>

<h3>To scrape</h3>

Open `wallhaven_scraper.py` using a text editor and set the `path` variable to the directory where you wish to download the images to. Then, run `python wallhaven_scraper.py` in the Terminal, from the directory of the extracted files. This starts downloading wallpapers to the path provided. Use `Ctrl-C` to stop the scraping at any point of time. Running the script again would resume scraping from the last completely downloaded wallpaper.

<h3>To search and download</h3>

Open `wallhaven_searcher.py` using a text editor and set the `path` variable to the directory where you wish to download the images to. Then, run `python wallhaven_searcher.py` in the Terminal, from the directory of the extracted files. This prompts a search query, entering which, relevant wallpapers are downloaded to a folder (named according to query) in the path provided. Use `Ctrl-C` to stop the downloading at any point of time. Running the script again with the same search query would resume downloading from the last completely downloaded wallpaper.

<h2><b>To add</b></h2>

1. More relevant wallpapers for search query by browsing tags

<h2><b>License</b></h2>

Please view LICENSE.md for details on the usage of code in this repository.
