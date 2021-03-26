import os, asyncio, logging, canvasapi
from core.exception import AuthenticateException
log = logging.getLogger()
class Canvas:
    def __init__(self, *args):
        try:
            self.obj = canvasapi.Canvas(*args)
            log.info(f"Successfully established a connection with Canvas! ({self.obj})")
        except:
            raise AuthenticateException("There was an error while logging in to StudentVUE.")
    def object(self):
        return self.obj