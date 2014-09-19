import json
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.template import loader, Context
import config
import threads


def home(request):
    reading = threads.getlast()
    t = loader.get_template('home.html')
    c = Context({
        'reading': reading,
        'probes': ['COOK', 'FOOD1', 'FOOD2', 'FOOD3']
    })
    return HttpResponse(t.render(c))


def current(request):
    return HttpResponse(json.dumps(threads.getlast()))

def plot(request):
    response = HttpResponse(content_type='image/png')

    statefile = open(config.output)
    readings = json.load(statefile)
    x = []
    y1 = []
    y2 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    y7 = []
    l = []
    t = []

    idx = 0
    tick = 0
    if (len(readings) < 11):
        intvl = len(readings)
    else:
        intvl = len(readings)/10
    for reading in readings:
        # ignore bad data
        if 'COOK_TEMP' in reading:
            x.append(idx)
            y1.append(reading['COOK_TEMP'])
            y2.append(reading['FOOD1_TEMP'])
            y3.append(reading['FOOD2_TEMP'])
            y4.append(reading['FOOD3_TEMP'])
            y5.append(reading['OUTPUT_PERCENT'])
            y6.append(reading['COOK_SET'])
            y7.append(reading['FOOD1_SET'])
            if idx % intvl == 0:
                t.append(idx)
                l.append(reading['TIME'][:5])
                tick += 1
            idx += 1

    plt.plot(x, y1, "rs", x, y2, "b^", x, y3, "gp", x, y4, "mD", x, y5, "k+--",
             x, y6, "r+--", x, y7, "b+--")
    plt.ylabel('Temperature F')
    plt.xticks(t, l)
    plt.gcf().set_size_inches(9, 4.5)
    plt.savefig(response, dpi=100)
    plt.close()

    return response
