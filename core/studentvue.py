import os, asyncio, logging, studentvue
from core.exception import AuthenticateException
log = logging.getLogger()
class StudentVue:
    def __init__(self, **credentials):
        try:
            self.obj = studentvue.StudentVue(
                username=credentials["username"],
                password=credentials["password"],
                district_domain=credentials["url"]
            )
            log.info(f"Successfully established a connection with StudentVUE! ({self.obj})")
        except:
            raise AuthenticateException("There was an error while logging in to StudentVUE.")
    def object(self):
        return self.obj