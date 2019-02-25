#!/usr/bin/env python3

import configparser
import mechanicalsoup
import os
import re
import requests

def work():
    home = os.environ['HOME']
    f_conf = '{}/.config/emome-pushover/config.ini'.format(home)

    c = configparser.ConfigParser()
    c.read(f_conf)

    pushover_api_token = c['default']['pushover_api_token']
    pushover_user_token = c['default']['pushover_user_token']
    pw = c['default']['pw']
    uid = c['default']['uid']

    b = mechanicalsoup.StatefulBrowser()

    url = 'https://bms.emome.net/proxy/mbms/service.jsp?leftmenu=bill&url=notPayBill.jsp'
    b.open(url)

    b.select_form('#form1')
    b['uid'] = uid
    b['pw'] = pw
    b.submit_selected()

    url = 'https://bms.emome.net/proxy/mbms/service.jsp?leftmenu=bill&url=notPayBill.jsp'
    b.open(url)

    text = b.get_current_page().select('table[width="350"]')[0].text
    text = re.sub(r'.*(國內數據.*?\)).*', r'\1', text, flags=re.DOTALL)

    text = '{} 的用量：\n'.format(uid) + text

    requests.post('https://api.pushover.net/1/messages.json', data={
        'token': pushover_api_token,
        'user': pushover_user_token,
        'message': text,
    })

if '__main__' == __name__:
    work()
