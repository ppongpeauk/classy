"""
    discord_rpc.py
    @restrafes
    
    Handles integration with Discord's rich presence toolkit
"""

import os, asyncio, logging, datetime, time
from pypresence import Client, Presence
from core.exception import DiscordException

log = logging.getLogger()
default_rpc = {
    "large_image": "sleep",
    "large_text": "classy 📖",
    "state": "loading",
    "small_image": "available",
    "small_text": "Available"
}

class DiscordRPC:
    def __init__(self, pipe=0, loop=asyncio.get_event_loop(), autoconnect=True):
        try:
            self.obj = Presence("757346500484268152", pipe=pipe, loop=loop)
            if autoconnect:
                self.obj.connect()
                log.info(f"Successfully established a connection with Discord RPC! ({self.obj})")
        except:
            raise Exception(0, "There was a problem while creating a Discord RPC object.")
    def connect(self):
        try:
            self.obj.connect()
        except:
            raise DiscordException(100, "There was a problem connecting a Discord RPC object.")
    def update(self, **kwargs):
        try:
            self.obj.update(
                **kwargs,
                **{x: y for x, y in default_rpc.items() if x not in kwargs}
            )
        except:
            raise DiscordException(300, "There was a problem while updating a Discord RPC object.")
        