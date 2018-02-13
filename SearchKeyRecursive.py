import urllib,json

def recursive(data):
     for key, value in data.items():
         if key == 'content':
             print value
             if isinstance(value, list):
                 print "Yes"


if __name__ == '__main__':
    link = "http://demo6920974.mockable.io/json-example"
    data = json.load(urllib.urlopen(link))
    recursive(data)
