import urllib,json


def recursive(data):
    v = raw_input('Enter the key: ')
    for key,value in data.items():
        if key == v:
            print value
            if isinstance(value,list):
                print 'yes'





if __name__ == '__main__':
    link = "http://demo6920974.mockable.io/json-example"
    data = json.load(urllib.urlopen(link))
    recursive(data)
