from bs4 import BeautifulSoup
import requests
from clint.textui import progress
import cPickle
import os
from time import sleep

def download():
    searchtermraw = raw_input("Enter your search term: ")
    path = '/home/jobsism10/Downloads/Wallpapers/' + searchtermraw
    searchterm = '+'.join(searchtermraw.split(" "))

    response = requests.get('https://alpha.wallhaven.cc/search?q={0}'.format(searchterm))
    soup = BeautifulSoup(response.text,"lxml")
    soup.prettify()

    pagenumheader = soup.find("h2",class_="thumb-listing-page-header")
    try:
        pages = int(pagenumheader.contents[-1][-1])
    except AttributeError:
        print "Sorry, no images for found for '{0}'!".format(searchtermraw)
        more = raw_input("Do you want to search for more? [y]: ")
        if more == 'y':
            print ""
            download()
            return
        else:
            return

    urlnumlist = []

    print ""
    print "Generating search results..."
    for page in range(1,pages+1):
        response = requests.get('https://alpha.wallhaven.cc/search?q={0}&page={1}'\
        .format(searchterm,page))
        soup = BeautifulSoup(response.text,"lxml")
        soup.prettify()
        previewlist = soup.find_all("a",class_="preview")

        for preview in previewlist:
            previewurl = preview["href"]
            num = previewurl.split("/")[-1]
            urlnumlist.append(num)

    print ""
    print "Search results: {0} images found for '{1}'.".format(len(urlnumlist),searchtermraw)

    try:
        with open('{0}_triednums.pickle'.format(searchtermraw),'rb') as f:
            triednums = cPickle.load(f)
    except:
        triednums = []

    try:
        for i,num in enumerate(urlnumlist):
            if num not in triednums:
                url = 'https://alpha.wallhaven.cc/wallpapers/full/wallhaven-{0}.jpg'.format(num)
                filename = url.split('/')[-1]
                response2 = requests.get(url)
                if response2.status_code == 404:
                    url = 'https://alpha.wallhaven.cc/wallpapers/full/wallhaven-{0}.png'.format(num)
                    filename = url.split('/')[-1]
                    response2 = requests.get(url)
                total_size = int(response2.headers.get('content-length'))
                try:
                    with open(path+'/'+filename,'wb') as f:
                        print "Downloading image {0}/{1}...".format(i+1,len(urlnumlist))
                        for data in progress.bar(response2.iter_content(chunk_size = 128),\
                        expected_size=total_size/128 + 1):
                            f.write(data)
                    triednums.append(num)
                    sleep(3)
                except IOError:
                    os.mkdir(path)
                    with open(path+'/'+filename,'wb') as f:
                        print "Downloading image {0}/{1}...".format(i+1,len(urlnumlist))
                        for data in progress.bar(response2.iter_content(chunk_size = 128),\
                        expected_size=total_size/128 + 1):
                            f.write(data)
                    triednums.append(num)
                    sleep(3)
        print "Dumping triednums list..."
        with open('{0}_triednums.pickle'.format(searchtermraw),'wb') as f:
            cPickle.dump(triednums,f)
        print "Dumped successfully!"
        print "All images for '{0}' successfully downloaded!".format(searchtermraw)
        more = raw_input("Do you want to search for more? [y]: ")
        if more == 'y':
            print ""
            download()
    except KeyboardInterrupt:
        print ""
        print "Download interrupted at image {0}!".format(i+1)
        print "Dumping triednums list..."
        with open('{0}_triednums.pickle'.format(searchtermraw),'wb') as f:
            cPickle.dump(triednums,f)
        print "Dumped successfully!"
        more = raw_input("Do you want to search for more? [y]: ")
        if more == 'y':
            print ""
            download()

download()
