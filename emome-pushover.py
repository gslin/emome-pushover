#!/usr/bin/env python3

import configparser
import os

def work():
    home = os.environ['HOME']
    f_conf = '{}/.config/emome-pushover/config.ini'.format(home)

    c = configparser.ConfigParser()
    c.read(f_conf)

if '__main__' == __name__:
    work()
