# todo: implement this class
from urllib.request import urlopen
from bs4 import BeautifulSoup


class LinkCrawler(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def collect_main_menu_links(self):
        html = urlopen(self.base_url)
        bs = BeautifulSoup(html, 'html.parser')
        links = bs.find('nav', id='menu').find_all('a')
        return links




