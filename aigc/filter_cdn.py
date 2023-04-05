"""
cursor生成，提取公众号封面图，并以文章标题命名图片
"""
import requests
import sys
import re

def main():
    url = sys.argv[1]
    response = requests.get(url)
    html = response.text
    pattern = re.compile(r'var cdn_url_235_1 = "(.*?)";')
    result = pattern.search(html)
    if result:
        image_url = result.group(1)
        pattern_title = re.compile(r"var msg_title = '(.*?)'.html\(false\);")
        result_title = pattern_title.search(html)
        if result_title:
            image_name = result_title.group(1) + '.jpg'
        else:
            image_name = 'image.jpg'
        image_response = requests.get(image_url)
        with open(image_name, 'wb') as f:
            f.write(image_response.content)

        print('[![%s](%s)](%s)' % (result_title.group(1), image_url, url))

if __name__ == '__main__':
    main()
