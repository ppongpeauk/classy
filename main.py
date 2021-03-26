"""
    main.py
    @restrafes
    
    Initializes all core functions
"""

import os, asyncio, json, sys, logging, re, time
from core.array_tools import without_keys, on_first_index
from core.scheduler import Scheduler
from core.canvas import Canvas
from core.studentvue import StudentVue
from core.discord_rpc import DiscordRPC
from core.webserver import WebServer
from core.microsoft_teams import open_url as ms_open_url
from core.exception import AuthenticateException, DiscordException

# asynchronous loop
loop = asyncio.get_event_loop()
# access user/app configuration
app_settings = json.load(open("settings/app.json", "r"))
user_settings = json.load(open("settings/user.json", "r"))
# logging
logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", filename="eve.log", level=logging.DEBUG)
log = logging.getLogger()
log.setLevel(app_settings["debugLevel"])
log.addHandler(logging.StreamHandler(sys.stdout))
# main application
log.info("Starting application..")

# authenticate with core libraries
c_canvas = Canvas(*user_settings["credentials"]["canvas"].values())
c_studentvue = StudentVue(**user_settings["credentials"]["studentVue"])
c_discord_rpc = DiscordRPC(loop=loop)
c_discord_rpc.update(
    state="waiting for class",
    details="idle",
    party_size=[1, 1],
)
c_webserver = WebServer(c_canvas, debug=False)

# studentvue's api is complicated >_<
c_studentvue_schedule = c_studentvue.object().get_schedule()
c_studentvue_school_info = c_studentvue.object().get_school_info()
c_studentvue_student_info = c_studentvue.object().get_student_info()
c_studentvue_class_list = c_studentvue_schedule["StudentClassSchedule"]["ClassLists"]["ClassListing"]
print(c_studentvue_student_info["StudentInfo"]["FormattedName"]["$"])
c_sorted_period_listing = {}
for x in c_studentvue_class_list:
    c_sorted_period_listing[str(x["@Period"])] = {
        "course_title": x["@CourseTitle"],
        "course_teacher": x["@Teacher"],
        "course_teacher_email": x["@TeacherEmail"],
        "course_room": x["@RoomName"]
    }
# schedule handling
async def on_schedule_event(**kwargs):
    #if kwargs["type"] in c_sorted_period_listing:  # period listing found!
    print(kwargs)
    if "url" in user_settings["schedule"][kwargs["type"]]:
        ms_open_url(url=user_settings["schedule"][kwargs["type"]]["url"])

s_scheduler = Scheduler()
# this list comprehension should never enter a codebase but...
s_jobs = [s_scheduler.object().add_job(on_schedule_event, "cron", kwargs={"schedule": {**y}, "type": x}, **on_first_index(without_keys(y, {"type", "url"}))) for x, y in user_settings["schedule"].items()]
log.debug(f"Added {len(s_jobs)} jobs!")

# run the application indefinitely
try:
    loop.run_forever()
except KeyboardInterrupt: # incase of ctrl-c while testing :"
    loop.close()
finally:
    loop.close()