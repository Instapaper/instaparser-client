from getpass import getpass
import json
import sys

from instaparser import InstaparserClient


def main():
    if len(sys.argv) != 2:
        print('Usage: %s <URL>' % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    api_key = getpass('API Key: ')
    if not api_key:
        print('Invalid API Key')
        sys.exit(-1)

    client = InstaparserClient(api_key)
    response = client.article_api(url)
    print(json.dumps(vars(response), indent=4))    

if __name__ == '__main__':
    main()
