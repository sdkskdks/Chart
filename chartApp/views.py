import json

from django.shortcuts import render
import requests


def index(request):
    URL = "https://api.etherscan.io/api"
    PARAMS = {
        'module': 'account',
        'action': 'txlistinternal',
        'address': '0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3',
        'startblock' : 0,
        'enblock': 2702578,
        'page': 1,
        'offset': 100,
        'sort': 'asc',
        'apikey': '8P5RPD7P652D1CQFFS3ESDRKWNU2DZKRFB'

    }
    r = requests.get(url=URL, params= PARAMS)

    data = []
    labels = []
    c = 0
    mx = 0
    for d in r.json()['result']:
        labels.append(c)
        c += 1
        data.append(int(d['value']))

    mx = max(data)
    data2 = [0,0,0,0]
    for i in data:
        if mx*0.75 <= i:
            data2[0] += 1
        elif mx*0.5 <= i:
            data2[1] += 1
        elif mx*0.25 <= i:
            data2[2] += 1
        else:
            data2[3] += 1
    labels2 = []
    a1 =  mx*0.75
    a2 = mx*0.5
    a3 = mx*0.25
    a4 = "Others"
    print(labels2)
    content = {
        'data': data,
        'labels': labels,
        'data2': data2,
        'a1': a1,
        'a2': a2,
        'a3': a3,
        'a4': a4
    }
    print(data)
    print(data2)
    print(labels2)
    # return json.load(r.json())
    return render(request, 'chartApp/index.html', content)
