GOOGLE_URL = 'https://www.google.com'


def change_url(url):
    new_url = GOOGLE_URL + url
    print(new_url)


change_url('/search')