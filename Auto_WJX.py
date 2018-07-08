


"""
自动填问卷星（http://www.sojump.com）
单项选择
"""

# 抓包软件： $ sudo apt-get install tshark
# 打开页面如： http://www.sojump.com/jq/4725800.aspx
# 随便填写，但不要提交
# $ sudo tshark -V -i eth0 -f tcp -Y http.request.method=="POST"
# －V 是解析包的所有信息并打印出来， －i 选择设备接口， -f 抓包过滤， -Y 显示过滤
# 打印出HTTP POST请求包的所有内容
# 需要的内容：[Full request URI: http://www.sojump.com/handler/processjq.ashx?
# submittype=1&curID=186257&t=1428725165556&starttime=2015%2F4%2F11%2012%3A01%3A20&rn=1932211292]
# [HTTP request 1/1] xxx
# submitdata=1%241%7D2%242%7D3%243%7D4%241%7D5%242%7D6%243
# 将上述内容解码（http://tool.chinaz.com/Tools/URLEncode.aspx）
# 得到 submitdata=1$1}2$2}3$3}4$1}5$2}6$3

# 举例： http://www.sojump.com/jq/4725800.aspx


from random import randint
import requests
from urllib import request, parse
from time import time, strftime, localtime


# 返回uri参数字典
def gen_uri_param():
    curID = '25890322'  # 问卷号
    submittype = '1'
    t = str(int(time() * 1000))
    starttime = strftime("%Y/%m/%d %H:%M:%S", localtime())
    rn = '1782780138'  # 网页源文件的rndnum
    return locals()


uri_base = "https://www.wjx.cn/joinnew/processjq.ashx?{}"

headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'referer':'https://www.wjx.cn/jq/25890322.aspx',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
proxies = {
  "https": "https://118.31.220.3:8080",
}
post_data = {'submitdata': '1$2}2$2|3}3$}4$1!2,2!4'}
get_data = parse.urlencode(gen_uri_param())

request_url = uri_base.format(get_data)
req = requests.post(request_url, headers=headers,data=post_data, proxies=proxies)
print(req.text)


