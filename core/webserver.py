import os, asyncio, logging, datetime, time
from threading import Thread
from sanic import Sanic, response
from jinja2 import Environment, FileSystemLoader, Template
log = logging.getLogger()
cwd = os.getcwd()

# template engine
file_loader = FileSystemLoader(os.path.join(cwd, "html"))
env = Environment(loader=file_loader)

#print(f"WEBSERVER CWD: {cwd}")
def create_server(self, host_addr, host_port, debug):
    asyncio.set_event_loop(asyncio.new_event_loop()) # create a new event loop
    loop = asyncio.get_event_loop() # fetch the newly created event loop
    # create the server
    app = Sanic(__name__)
    app.static("/public", os.path.join(cwd, "html"))
    # endpoints!!
    @app.route("/") # root
    def home(request):
        return response.json({"success": True})
    @app.route("/v1/assignments") # root
    def get_assignments(request):
        assignments_list = [
            {
                "name": "1",
                "class_name": "Introduction to Game Design",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tellus cras adipiscing enim eu turpis egestas.",
                "link": ""
            },
            {
                "name": "2",
                "class_name": "Introduction to Game Design",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tellus cras adipiscing enim eu turpis egestas.",
                "link": ""
            },
            {
                "name": "3",
                "class_name": "Introduction to Game Design",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tellus cras adipiscing enim eu turpis egestas.",
                "link": ""
            }
        ]
        return response.json({"success": True, "assignments": assignments_list}) # dont forget to work on this :))
    @app.route("/v1/get-ongoing-class")
    def get_ongoing_class(request):
        return response.json({
            "success": True,
            "isClassOngoing": True,
            "ongoingClass": {
                "className": "Imposter Academy",
                "classInstructor": "Red",
                "classMeetingLink": "https://www.youtube.com/watch?v=grd-K33tOSM",
                "thumbnail": "http://localhost:3000/sus.png"
            },
        }, headers={'Access-Control-Allow-Origin': '*'}, status=200)
    self.append(app.create_server(host=host_addr, port=host_port, return_asyncio_server=True, debug=debug))
    self.append(app)
    server_task = asyncio.ensure_future(self[0])
    loop.run_forever()
class WebServer:
    def __init__(self, canvas, host_addr="0.0.0.0", host_port=5124, debug=True):
        r_list = []
        t = Thread(target=create_server, args=(r_list, host_addr, host_port, debug))
        t.start() # run the webserver on another thread
        while len(r_list) == 0:
            time.sleep(1) # halt until obj is set
        self.obj = r_list[0]
        self.canvas = canvas
        log.info(f"Successfully established a connection with Sanic! (webserver) ({self.obj})")