#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests

def main(q):
  url = "https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk"
  s = requests.session()
  params = {"apikey":"2ApUHmPZc9xaRmlLEMMzybP7WDwb3SqZ", "query":q}
  r =  s.post(url, data=params)
  try:
    print("talk_apiの応答文:", r.json()["results"][0]["reply"])
    print("Perplexity:", r.json()["results"][0]["perplexity"])
  except:
    print(r.json())

if __name__=='__main__':
  while(True):
    print("入力: ", end="")
    main(input())
