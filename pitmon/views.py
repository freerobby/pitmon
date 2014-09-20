import json
from django.http import HttpResponse
from django.template import loader, Context
import config
import threads


def home(request):
    reading = threads.getlast()
    t = loader.get_template('index.html')
    c = Context()
    return HttpResponse(t.render(c))


def current(request):
    return HttpResponse(json.dumps(threads.getlast()))


def data(request):
    # TODO: Ugly, still code from matplotlib that needs pruning and cleanup
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
    y8 = []
    y9 = []
    l = []
    t = []
    ts = []

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
            y8.append(reading['FOOD2_SET'])
            y9.append(reading['FOOD3_SET'])
            ts.append(reading['TIMESTAMP'])
            if idx % intvl == 0:
                t.append(idx)
                l.append(reading['TIME'][:5])
                tick += 1
            idx += 1

    data = dict()
    data['cook_temp'] = y1;
    data['cook_set'] = y6;
    data['food1_temp'] = y2;
    data['food1_set'] = y7;
    data['food2_temp'] = y3;
    data['food2_set'] = y8;
    data['food3_temp'] = y4;
    data['food3_set'] = y9;
    data['output_percent'] = y5;
    data['food3_temp'] = y4;
    data['timestamp'] = ts;

    return HttpResponse(json.dumps(data))
