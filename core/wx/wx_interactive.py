#!/usr/bin/env python
# -*- coding:utf-8 -*-
__Author__ = "Yasin Li"


import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from core.util.dbutil import dbutil
from  core.tb.tb_change_tbkey import change_Key
from  core.Log import logger
# django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        # 接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        # 服务器配置中的token

        token = '5DgLLq7EBg1NJcnSFylK'
        #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        try:
            hashlist.sort()
        except BaseException as e:
            print(e)


        hashstr = ''.join([s for s in hashlist])
        hashsha = hashlib.sha1()
        hashsha.update(hashstr.encode("utf-8"))
        hashstr = hashsha.hexdigest()

        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        othercontent = autoreply(request)
        print(othercontent)
        return HttpResponse(othercontent)
        # 微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
import xml.etree.ElementTree as ET
from lxml import etree
# import xml.etree as etree
def wx_msg(msg_type):
    wx_dbutil = dbutil().wx_msg(msg_type)
    wx_msg = dict(json.loads(wx_dbutil))
    content = wx_msg.get("wx_msg_value")
    return  content


def autoreply(request):
    try:
        print(request)
        print(request.body)
        webData = request.body
        xmlData = etree.fromstring(webData)
        print(xmlData)
        # msg_type = "text"
        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        wx_res_Content = xmlData.find('Content').text
        # MsgType = xmlData.find('MsgType').text
        # MsgId = xmlData.find('MsgId').text
        toUser = FromUserName
        fromUser = ToUserName
        if msg_type == 'text':
            # content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
            if change_Key(msg_type) == 0:
                content = wx_msg(msg_type)
                replyMsg = TextMsg(toUser, fromUser, content)
                print ("卡券调用失败")
                logger.error("卡券调用失败")
            else:
                content = change_Key(wx_res_Content)
                replyMsg = TextMsg(toUser, fromUser, content)
                logger.info("返回卡券成功！！")

            return replyMsg.send()
        elif msg_type == 'event':
            event = xmlData.find('Event').text
            if event == 'subscribe':
                # content = "欢迎欢迎 热烈欢迎"
                content = wx_msg(msg_type)
                replyMsg = TextMsg(toUser, fromUser, content)
                return replyMsg.send()

        elif msg_type == 'image':
            content = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'video':
            content = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'location':
            content = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        else:
            msg_type == 'link'
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
    except Exception as Argment:
        return Argment
class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text
import time
class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
            <xml>
            <ToUserName> <![CDATA[{ToUserName}]]> </ToUserName>
            <FromUserName> <![CDATA[{FromUserName}]]> </FromUserName>
            <CreateTime> {CreateTime} </CreateTime>
            <MsgType> <![CDATA[text]]> </MsgType>
            <Content> <![CDATA[{Content}]]> </Content>
            </xml>
        """
        return XmlForm.format(**self.__dict)
