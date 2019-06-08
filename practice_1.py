#!/usr/bin/env python 
# -*- coding:utf-8 -*-


def greet_users(names):
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)


usernames = ['hannah', 'try', 'morgot']
greet_users(usernames)
