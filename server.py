from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
from pitmon import persist, poller, threads, config


class MyHandler(BaseHTTPRequestHandler):

    def default(self):
        self.serve_static("static/index.html")

    def static(self):
        self.serve_static(self.path)

    def favicon(self):
        self.send_response(404)

    def current(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps(threads.getlast()))

    def data(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

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
        self.wfile.write(json.dumps(data))

    def do_GET(self):

        # Must be entirely unique, not sorted so order unpredictable
        prefixes = {
            '/favicon.ico': self.favicon,
            '/static': self.static,
            '/current': self.current,
            '/data': self.data
        }

        for prefix in prefixes:
            if self.path.startswith(prefix):
                prefixes[prefix]()
                return

        self.default()

    def serve_static(self, filename):
        resource = open("./%s" % filename)
        self.send_response(200)
        type = 'text/html'
        if filename.endswith('.css'):
            type = 'text/css'
        if filename.endswith('.js'):
            type = 'text/javascript'
        self.send_header('Content-type', type)
        self.end_headers()
        self.wfile.write(resource.read())
        resource.close()


def main():
    threads.start()

    try:
        server = HTTPServer(('', config.port), MyHandler)
        print 'started... Listening on port', config.port
        server.serve_forever()
    except KeyboardInterrupt:
        print 'shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
