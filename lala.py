from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'

with SB(uc=True, test=True,locale=f"{language_code.upper()}") as ddddda:
    ddddda.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    ddddda.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #"#live-channel-stream-information"
    url = "https://www.twitch.tv/brutalles"
    ddddda.uc_open_with_reconnect(url, 4)
    ddddda.sleep(24)
    ddddda.uc_gui_click_captcha()

    if ddddda.is_element_present("#live-channel-stream-information"):
        url = "https://www.twitch.tv/brutalles"
        ddddda.uc_open_with_reconnect(url, 5)
        if ddddda.is_element_present('button:contains("Accept")'):
            ddddda.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            ddddda2 = ddddda.get_new_driver(undetectable=True)
            ddddda2.uc_open_with_reconnect(url, 5)
            ddddda.sleep(10)
            if ddddda2.is_element_present('button:contains("Accept")'):
                ddddda2.uc_click('button:contains("Accept")', reconnect_time=4)
            while ddddda.is_element_present("#live-channel-stream-information"):
                ddddda.sleep(100)
            ddddda.quit_extra_driver()
    ddddda.sleep(1)
