'''
Created by auto_sdk on 2018.10.17
'''
from  core.tb_sdk.top.api.base import RestApi
class OpenuidGetBytradeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.tid = None

	def getapiname(self):
		return 'taobao.openuid.get.bytrade'