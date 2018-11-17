#!/usr/bin/env python3

import configparser
import mechanicalsoup
import os

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

    url = 'https://member.cht.com.tw/HiReg/checkcookieservlet?version=1.0&curl=https://auth.emome.net/emome/membersvc/AuthServlet&siteid=76&sessionid=&channelurl=https://auth.emome.net/emome/&others=mobilebms&checksum=a2e0f826bd63084eae045041af9b6d57';
    b.open(url)

    b.select_form('#form1')
    b['uid'] = uid
    b['pw'] = pw
    b.submit_selected()

    url = 'https://bms.emome.net/proxy/mbms/service.jsp?leftmenu=bill&url=notPayBill.jsp'
    b.open(url)

if '__main__' == __name__:
    work()
