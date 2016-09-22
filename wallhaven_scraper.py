from time import sleep
import requests
from clint.textui import progress
import cPickle

try:
    with open('last_tried_number.pickle','rb') as f:
        last_tried_number = 0
        last_tried_number = cPickle.load(f)
except:
    last_tried_number = 0

tally = 0
i = last_tried_number + 1
path = '/home/jobsism10/Downloads/Wallpapers/'

try:
    while tally != 50:
        url = 'https://alpha.wallhaven.cc/wallpapers/full/wallhaven-{0}.jpg'.format(i)
        response = requests.get(url, stream = True)
        if response.status_code == 404:
            url = 'https://alpha.wallhaven.cc/wallpapers/full/wallhaven-{0}.png'.format(i)
            response = requests.get(url, stream = True)
            if response.status_code == 404:
                print 'Tally encountered at {0}!'.format(i)
                tally += 1
                last_tried_number = i
                i += 1
                continue
            elif response.status_code == 200:
                tally = 0
                file_name = url.split("/")[-1]
                print "Downloading image {0}...".format(i)
                total_size = int(response.headers.get('content-length'))
                with open(path + file_name, "wb") as handle:
                    for data in progress.bar(response.iter_content(chunk_size = 128),\
                    expected_size = (total_size/128 + 1)):
                        handle.write(data)
                last_tried_number = i
                i += 1
                sleep(3)
            else:
                print "Response status code:", response.status_code
        elif response.status_code == 200:
            tally = 0
            file_name = url.split("/")[-1]
            print "Downloading image {0}...".format(i)
            total_size = int(response.headers.get('content-length'))
            with open(path + file_name, "wb") as handle:
                for data in progress.bar(response.iter_content(chunk_size = 128),\
                expected_size = (total_size/128 + 1)):
                    handle.write(data)
            last_tried_number = i
            i += 1
            sleep(3)
        else:
            print "Response status code:", response.status_code
    print "Tally of 50 reached!"
    print "Last response status code:",response.status_code
    print "Dumping last tried number '{0}'...".format(last_tried_number)
    with open('last_tried_number.pickle','wb') as f:
        cPickle.dump(last_tried_number,f)
    print "Dumped successfully!"

except:
    print ""
    print "Dumping last tried number '{0}'...".format(last_tried_number)
    with open('last_tried_number.pickle','wb') as f:
        cPickle.dump(last_tried_number,f)
    print "Dumped successfully!"
