import urllib,json

def _finditem(obj, key):
    if key in obj:
        return obj[key]
    for k, v in obj.items():
        if isinstance(v,dict):
            return _finditem(v, key)
        if isinstance(v,list):
            for i in v:
                if key in i:
                    print _finditem(i,key)
                # if isinstance(i, dict):
                #     return _finditem(i, key)


if __name__ == '__main__':
    link = "http://demo6920974.mockable.io/json-example"
    data = json.load(urllib.urlopen(link))
    v = raw_input('Enter the key: ')
    d = _finditem(data, v)
    print d