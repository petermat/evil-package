import sys
import os
import urllib.request
import pwd

"""
T1592  Gather Victim Host Information
Platforms: Windows, Linux, Darwin 
https://medium.com/checkmarx-security/17-malicious-python-packages-targeting-selenium-users-to-steal-crypto-8d24628ec656
https://unit42.paloaltonetworks.com/malicious-packages-in-pypi/
"""
def get_os_info(platform):

    myip = ""
    if platform in ('Linux', 'Darwin'):  # 'Linux', 'Darwin', 'Java', 'Windows'
        # [Get IP] Method #1 wget
        myip = os.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()

    try:
        import requests  # not a Standard lib
    except: pass
    else:
        # [Get IP] Method #2 python requests lib
        myip = requests.get('https://www.wikipedia.org').headers['X-Client-IP']

    # [Get IP] Method #3 python urllib lib
    myip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    # [Get Geolocation Method #1 Geolocation-db]
    ip_geo = urllib.request.urlopen(f'https://geolocation-db.com/jsonp/{myip}').read().decode('utf8')

    # [Get Username] Method #1 OS Env
    myusername = os.getenv("USERNAME")


    # Works for MacOS and Win ?
    # [Get Username] Method #2 python pwd lib
    myusername2 = pwd.getpwuid(os.getuid()).pw_name



    return myusername or myusername2 #username