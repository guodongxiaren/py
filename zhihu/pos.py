import http.client

conn = http.client.HTTPSConnection("www.zhihu.com")

headers = {
    'User-Agent': "PostmanRuntime/7.17.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "2a2065cf-3b46-4c7c-8d6f-67464348c10c,ce109c7c-125e-4bf1-91f6-94ce1f593c52",
    'Host': "www.zhihu.com",
    'Accept-Encoding': "gzip, deflate",
    'Cookie': '_zap=d8d61208-2d92-461e-ae7d-645f374aa419; _xsrf=eca9c5e4-62e6-45c6-86c9-faf922add43f; d_c0="APDiR5XfGA-PTqhxkZ9Ehxd97v7AzxPp10g=|1552147261"; KLBRSID=4843ceb2c0de43091e0ff7c22eadca8c|1590765750|1590765750',
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

conn.request("GET", "/people/guodongxiaren", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
