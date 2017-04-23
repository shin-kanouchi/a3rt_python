#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests

def main(q):
  url = "https://api.a3rt.recruit-tech.co.jp/proofreading/v1/typo?"
  s = requests.session()
  params = {"apikey":"By5lfKeVeDawRvmBLg3iFPMt1MV1nCZw", "sentence":q}
  r =  s.post(url, data=params)
  try:
    if r.json()["status"] == 0:
      print("ok")
    elif  r.json()["status"] == 1:
      for one_json in r.json()["alerts"]:
        print(one_json)
    else:
      print(r.json()["status"])
  except:
    print(r.json())

if __name__=='__main__':
  while(True):
    print("入力: ", end="")
    main(input())
