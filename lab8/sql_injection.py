#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 lhuang <lhuang9703@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
import requests
from bs4 import BeautifulSoup
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, 
                    default='http://10.211.55.13/dvwa/vulnerabilities/sqli/', 
                    help='url you want to inject')
parser.add_argument('--security', type=str, 
                    default='medium', 
                    help='security level')
parser.add_argument('--PHPSESSID', type=str, 
                    default='10ce72b2e3f3ea5aa29a1492b7901c47', 
                    help='php session id')
parser.add_argument('--id', type=str, 
                    help='sql injection string')
args = parser.parse_args()


def getHtmlText(url, post_data, cookies):
    r = requests.post(url, data=post_data, cookies=cookies)
    if r.status_code == 200:
        return r.text


def parseHtmlText(text):
    soup = BeautifulSoup(text, features='html.parser')
    exist_pre = soup.select('pre')
    if exist_pre != []:
        for tag in exist_pre:
            content = tag.get_text()
            idx_id = content.find('ID:')
            idx_first_name = content.find('First name:')
            idx_surname = content.find('Surname:')
            print("ID:\n", content[idx_id + len('ID:') : idx_first_name])
            print("First name:\n", 
                    content[idx_first_name + len('First name:') : idx_surname])
            print("Surname:\n", content[idx_surname + len('Surname:') : ], '\n')
    else:
        print('No result returned!')


if __name__ == '__main__':
    kwargs = {
                'url':args.url, 
                'post_data':{'id':args.id, 'Submit':'Submit'}, 
                'cookies':{'security':args.security, 'PHPSESSID':args.PHPSESSID}
            }

    text = getHtmlText(**kwargs)
    parseHtmlText(text)
