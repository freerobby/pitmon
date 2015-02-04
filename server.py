from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import argparse
import json
import os
from pitmon import persist, poller, threads, config


class MyHandler(BaseHTTPRequestHandler):

    def default(self):
        self.serve_static("/static/index.html")

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
            intvl = len(readings) / 10
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
        data['cook_temp'] = y1
        data['cook_set'] = y6
        data['food1_temp'] = y2
        data['food1_set'] = y7
        data['food2_temp'] = y3
        data['food2_set'] = y8
        data['food3_temp'] = y4
        data['food3_set'] = y9
        data['output_percent'] = y5
        data['food3_temp'] = y4
        data['timestamp'] = ts
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
        contenttypes = {
            # Default is text/html
            '.js': 'text/javascript',
            '.css': 'text/css',
            '.ico': 'image/x-icon'
        }

        content = 'text/html'
        for suffix in contenttypes:
            if filename.endswith(suffix):
                content = contenttypes[suffix]

        resourcefile = ".%s" % filename
        if os.path.isfile(resourcefile):
            try:
                resource = open(resourcefile)
                self.send_response(200)
                self.send_header('Content-type', content)
                self.end_headers()
                self.wfile.write(resource.read())
                resource.close()
            except IOError:
                self.send_response(500)
        else:
            self.send_response(404)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-p', '--port', dest='port', type=int, default=config.port, help='Port for HTTP server (default=%d).' % config.port)
    argparser.add_argument('-s', '--simulate', action='store_true', default=False, help='Simulate cyberq (default=false).')
    argparser.add_argument('cyberq', nargs='?', help='Cyberq IP address.')
    args = argparser.parse_args()

    if args.simulate is False and args.cyberq is None:
        print 'ERROR: Either -s (--simulate) or cyberq IP address must be specified.\n'
        argparser.print_help()
        return

    if args.simulate is True and args.cyberq is not None:
        print 'ERROR: Both -s (--simulate) and cyberq IP address cannot be specified. Choose just one.\n'
        argparser.print_help()
        return

    if args.simulate:
        url = 'localhost:%d/static' % args.port
    else:
        url = '%s' % args.cyberq

    server = HTTPServer(('', args.port), MyHandler)
    try:
        print 'HTTP server started... Listening on port', args.port
        print 'Connecting to cyberq with URL %s' % url
        threads.start(url)
        server.serve_forever()
    except KeyboardInterrupt:
        print 'HTTP server stopped'
        server.socket.close()

if __name__ == '__main__':
    main()
