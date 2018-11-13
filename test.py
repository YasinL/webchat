#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"
# import  hashlib
# upwd="test"
# s1 = hashlib.sha1()
# s1.update(upwd.encode("utf8"))  # 指定编码格式，否则会报错
# upwd3 = s1.hexdigest()
# print(upwd3)

from lxml import etree

webData='''<xml>
<ToUserName><![CDATA[gh_b398b71327f3]]></ToUserName>
<FromUserName><![CDATA[o7Ceh1UB2YhA4qzfebmoofesYw6s]]></FromUserName>
<CreateTime>1542075747</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[subscribe]]></Event>
<EventKey><![CDATA[]]></EventKey>
<Encrypt><![CDATA[j9XHABzbtMjv09WJ0QDjRczfzyGV8GrVRoGIonRBOvF+BIeKG2nSIwJ7N6CiGq3VAiyhF35L3lM6CjqKhpslLjOQFhFH1VGbiA+CTmSYhs4Nxt2Eel2p2o6mrU24HRFVSEsu4sOXD3Su+zgXUWVbxXUuFKfgb0WNIIlAg5GwnGmvnrVZJJs/4C9QbJoITqrrPt8dootCXw8qK/VoE6Ektl33Nawaa1jhEiH0Ok4Qz9yv0JPGnxfqgAIUx9/IxwGhly9fs8fx0MGVPOFu8P2D0BRUDJg3YRkP0eaCzlSV7EXLLZdcnlbLwTr3AIBRM84YRCFpo7gV2ONXMornVKknPwOJvlTgi9fFNwIcORQgn7Hle8QOU28aANBc3bPIBbZZqrR7VZC/JYUkFvhZgvaLR3j6UyyvTLXaQVxzLXXLGto=]]></Encrypt>
</xml>'''

xmldata = etree.fromstring(webData)

print(xmldata.find('ToUserName').text)
print(xmldata.find('FromUserName').text)
print(xmldata.find('CreateTime').text)
print(xmldata.find('MsgId').text)
print(xmldata.find('MsgType').text)
