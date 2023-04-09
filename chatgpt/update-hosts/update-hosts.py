import http.server
import socketserver
import urllib.parse

# 本地 hosts 文件的路径
HOSTS_FILE = '/etc/hosts'

# HTTP 请求处理器
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 解析请求参数
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        domain = params.get('domain', [''])[0]
        ip = params.get('ip', [''])[0]

        # 更新 hosts 文件
        if domain and ip:
            with open(HOSTS_FILE, 'a') as f:
                f.write(ip + ' ' + domain + '\n')

        # 返回响应
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')

# 启动 HTTP 服务器
with socketserver.TCPServer(('', 8080), RequestHandler) as httpd:
    print('Server started at http://localhost:8080')
    httpd.serve_forever()
