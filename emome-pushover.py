#!/usr/bin/env python3

import configparser
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

if '__main__' == __name__:
    work()
