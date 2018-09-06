from urllib .parse import urlencode

params = {
    'name': 'tom',
    'age': 23
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
