# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认40次/20分钟
READ_NUM = int(os.getenv('READ_NUM') or 40)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'RK': '8b8IPkxLPX',
    'ptcz': '44866af3012d4100cd8d840d0a81f70af8ff7e8887a9105d266712edec417331',
    '_clck': '1xr709b|1|g2h|0',
    '_qimei_uuid42': '1a1080b2f391003f718dbc6784da2191eabd1748e4',
    '_qimei_fingerprint': '46d124002cf7d99787d08337dcd33c84',
    '_qimei_i_3': '27bc4ad19c08548d939eff62098270e7f3e7a4f3145c0a8ab7dd2b0d24c5246b336337943989e2949ebf',
    'pgv_pvid': '5185920880',
    'wr_localvid': '4b8327f0711133e34b84c1f',
    'wr_name': 'Charlie',
    'wr_avatar': 'https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0010-IMOW_s1Y7fwyHB16rCT1jf3%2F0',
    'wr_gender': '1',
    '_qpsvr_localtk': '0.285836598468007',
    'pgv_info': 'ssid=s9233582944',
    'wr_gid': '215214924',
    'wr_skey': 'yWoj8bg7',
    'wr_vid': '17904611',
    'wr_ql': '0',
    'wr_rt': 'web%40QaLP1~Rps6Jn9_ac1CI_AL',
    'wr_fp': '1878795642',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=dev-1770724961596,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=a9eae182337843e098ee4ad2fc74378b',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://weread.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/20e32f20813abb43fg01262c',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'a9eae182337843e098ee4ad2fc74378b-8e0b68c64a556b72',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'x-wrpa-0': 'c65674eec2bdf6051b7a4a28430c187ba9f7c284edc6be3b1935f0931edb146bc5a482543942b001588a6cfa54c5e5158ffa2a116603427797dd6da101444bdd,JGphRipvaVdlVsOzRMKow7gXNigcwp4JHyHCjTlfwq4IJsKIQcK0wqfDj8KLLGd8w6XDlcKSWCvCulvDucKcwqzDgMKnwqZ+T8KdwqHCjlIqw5TDk8OqFcOWwqbCp8KwJ0lzwqLDplozVEPDmsKwwrhCdMO0HArDhF3DrG7CvsOEwojCm1cLwo3CusORUSjDvcO5w6oPw4jCoMOAwpDCrcOtwr3DvMOiwr3CuEHCl8K6w54HEldQbsOKwonDhcOaPAjChMK3w6Q0wqrChkIww53Cpyhrw5rCuBdiwqPDiMK5NG/DpMOow7krX8K8wr4qR8KGwpfDgk/DgWYXc8OWwqnDrz1mfHlRwopLWsKIw4PDqhTClsOsRRPDgj9rRMKow5nDqMKew6nCo0ZVwp5OBmPCjGMYw7owWMOkdSI9wrk1wrnDgcOSQDRUVsOUfMOFw6IhOMOSMz1mYcO1OsOqaBjDsjLDksOYwozDjn7ChMOawq7DhjMYw7wCw5DChsKK,WntILW5YXcOOw4BWH2PDr8KmBH3Cn8KTw57DqB3Dq8KMXXwZVGHDmMK5G15HasOScsKjw61aw4VxZHfCph55Q8KvdMOWBsO8EVgRamVlXsOvwrocwp7CmsOcw5tLwp1ZOTZnOxVJHUfDgDBzekHDsnTCkHENYHrDkX3CkAIHw68jw4zDj1rCtxpfU8K5w4TCkF3CjcOzaTE=',
    # 'cookie': 'RK=8b8IPkxLPX; ptcz=44866af3012d4100cd8d840d0a81f70af8ff7e8887a9105d266712edec417331; _clck=1xr709b|1|g2h|0; _qimei_uuid42=1a1080b2f391003f718dbc6784da2191eabd1748e4; _qimei_fingerprint=46d124002cf7d99787d08337dcd33c84; _qimei_i_3=27bc4ad19c08548d939eff62098270e7f3e7a4f3145c0a8ab7dd2b0d24c5246b336337943989e2949ebf; pgv_pvid=5185920880; wr_localvid=4b8327f0711133e34b84c1f; wr_name=Charlie; wr_avatar=https%3A%2F%2Fres.weread.qq.com%2Fwravatar%2FWV0010-IMOW_s1Y7fwyHB16rCT1jf3%2F0; wr_gender=1; _qpsvr_localtk=0.285836598468007; pgv_info=ssid=s9233582944; wr_gid=215214924; wr_skey=yWoj8bg7; wr_vid=17904611; wr_ql=0; wr_rt=web%40QaLP1~Rps6Jn9_ac1CI_AL; wr_fp=1878795642',
}


# 书籍
book = [
    "36d322f07186022636daa5e","6f932ec05dd9eb6f96f14b9","43f3229071984b9343f04a4","d7732ea0813ab7d58g0184b8",
    "3d03298058a9443d052d409","4fc328a0729350754fc56d4","a743220058a92aa746632c0","140329d0716ce81f140468e",
    "1d9321c0718ff5e11d9afe8","ff132750727dc0f6ff1f7b5","e8532a40719c4eb7e851cbe","9b13257072562b5c9b1c8d6"
]

# 章节
chapter = [
    "ecc32f3013eccbc87e4b62e","a87322c014a87ff679a21ea","e4d32d5015e4da3b7fbb1fa","16732dc0161679091c5aeb1",
    "8f132430178f14e45fce0f7","c9f326d018c9f0f895fb5e4","45c322601945c48cce2e120","d3d322001ad3d9446802347",
    "65132ca01b6512bd43d90e3","c20321001cc20ad4d76f5ae","c51323901dc51ce410c121b","aab325601eaab3238922e53",
    "9bf32f301f9bf31c7ff0a60","c7432af0210c74d97b01b1c","70e32fb021170efdf2eca12","6f4322302126f4922f45dec"
]

"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    "appId": "wb182564874603h266381671",
    "b": "ce032b305a9bc1ce0b0dd2a",
    "c": "7f632b502707f6ffaa6bf2e",
    "ci": 27,
    "co": 389,
    "sm": "19聚会《三体》网友的聚会地点是一处僻静",
    "pr": 74,
    "rt": 15,
    "ts": 1744264311434,
    "rn": 466,
    "sg": "2b2ec618394b99deea35104168b86381da9f8946d4bc234e062fa320155409fb",
    "ct": 1744264311,
    "ps": "4ee326507a65a465g015fae",
    "pc": "aab32e207a65a466g010615",
    "s": "36cc0815"
}


def convert(curl_command):
    """提取bash接口中的headers与cookies
    支持 -H 'Cookie: xxx' 和 -b 'xxx' 两种方式的cookie提取
    """
    # 提取 headers
    headers_temp = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_temp[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    
    # 从 -H 'Cookie: xxx' 提取
    cookie_header = next((v for k, v in headers_temp.items() 
                         if k.lower() == 'cookie'), '')
    
    # 从 -b 'xxx' 提取
    cookie_b = re.search(r"-b '([^']+)'", curl_command)
    cookie_string = cookie_b.group(1) if cookie_b else cookie_header
    
    # 解析 cookie 字符串
    if cookie_string:
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key.strip()] = value.strip()
    
    # 移除 headers 中的 Cookie/cookie
    headers = {k: v for k, v in headers_temp.items() 
              if k.lower() != 'cookie'}

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
