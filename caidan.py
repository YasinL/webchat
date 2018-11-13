# -*- encoding: utf-8 -*-

import  requests
import json
import sys


appid = 'wxade89b6f7604df3c'
secret = '5bfed939032c0f3f2dd30378a8b7efaf'

gettoken = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret

f = requests.get(gettoken)

stringjson = f.content
print(stringjson)

access_token = json.loads(stringjson)['access_token']

# print access_token

posturl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + access_token

menu = '''
{
	"button": [{
			"name": "帮助系统",
			"sub_button": [{
					"type": "click",
					"name": "帮助系统1",
					"key": "rselfmenu_0_0",
					"sub_button": []
				},
				{
					"type": "scancode_push",
					"name": "帮助系统2",
					"key": "rselfmenu_0_1",
					"sub_button": []
				}
			]
		},
		{
			"name": "测试连接",
			"sub_button": [{
					"type": "view",
					"name": "测试连接1",
					"url": "http://www.jd.com/"
				},
				{
					"type": "view",
					"name": "测试连接1",
					"url": "http://www.baidu.com/"
				}
			]
		}

	]
}
'''

request = requests.post(url=posturl,data=menu.encode("utf-8"))

print(request.content)