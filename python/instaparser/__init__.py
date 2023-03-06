import json
import requests


class InstaparserResponse(object):
    def __init__(self, r):
        self.status_code = r.status_code
        json = r.json() if r.status_code == 200 else {}
        self.url = json.get('url', None)
        self.title = json.get('title', None)
        self.site_name = json.get('site_name', None)
        self.thumbnail = json.get('thumbnail', None)
        self.description = json.get('description', None)
        self.author = json.get('author', None)
        self.date = json.get('date', None)
        self.html = json.get('html', None)
        self.text = json.get('text', None)
        self.words = json.get('words', None)
        self.is_rtl = json.get('is_rtl', None)
        self.images = json.get('images', None)
        self.videos = json.get('videos', None)


class InstaparserClient(object):
    ENDPOINT = 'https://instaparser.com/api/1'
    def __init__(self, api_key):
        self.api_key = api_key

    def article_api(self, url, use_cache=True):
        params = {
            'url': url,
            'api_key': self.api_key,
            'use_cache': use_cache
        }
        r = requests.get('%s/%s' % (self.ENDPOINT, 'article'), params=params)
        return InstaparserResponse(r)
    
    def text_api(self, url, use_cache=True):
        params = {
            'url': url,
            'api_key': self.api_key,
            'use_cache': use_cache
        }
        r = requests.get('%s/%s' % (self.ENDPOINT, 'text'), params=params)
        return InstaparserResponse(r)
    
    def document_api(self, url, html, use_cache=True):
        params = {
            'url': url,
            'api_key': self.api_key,
            'use_cache': use_cache
        }
        r = requests.post('%s/%s' % (self.ENDPOINT, 'document'), params=params, body=html)
        return InstaparserResponse(r)
