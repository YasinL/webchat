'''
Created by auto_sdk on 2018.10.10
'''
from  core.tb_sdk.top.api.base import RestApi
class TopSecretGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.customer_user_id = None
		self.random_num = None
		self.secret_version = None

	def getapiname(self):
		return 'taobao.top.secret.get'
