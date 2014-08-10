import json
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.template import loader, Context
import config


def home(request):
    t = loader.get_template('home.html')
    c = Context({
    })
    return HttpResponse(t.render(c))


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
    l = []
    t = []

    idx = 0
    tick = 0
    if (len(readings) < 11):
        intvl = len(readings)
    else:
        intvl = len(readings)/10
    for reading in readings:
        x.append(idx)
        y1.append(reading['COOK_TEMP'])
        y2.append(reading['FOOD1_TEMP'])
        y3.append(reading['FOOD2_TEMP'])
        y4.append(reading['FOOD3_TEMP'])
        if idx % intvl == 0:
            t.append(idx)
            l.append(reading['TIME'][:5])
            tick += 1
        idx += 1

    plt.plot(x, y1, "rs", x, y2, "b^", x, y3, "gp", x, y4, "mD")
    plt.ylabel('Temperature F')
    plt.xticks(t, l)
    plt.gcf().set_size_inches(12, 6)
    plt.savefig(response, dpi=100)
    plt.close()

    return response
