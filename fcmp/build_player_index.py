import urllib2
import sys

from BeautifulSoup import BeautifulSoup

from db_models import Download, Status, db

reload(sys)
sys.setdefaultencoding("latin-1")


def find_players(players_soup):
    for tr in players_soup.table.tbody.findAll('tr'):
        for td in tr.findAll('td', attrs={'class': 'text-left'}):
            player = td.div.a
            name = player.strong.text
            url = player['href']
            yield (name, url, Status.NEW)


def __download_page__(page_number):
    print "\nProcessing page %d" % page_count
    link = "http://www.futwiz.com/en/career-mode/players?page=%s" % page_number
    return urllib2.urlopen(urllib2.Request(link, headers={'User-Agent': 'Mozilla/5.0'}))


def __insert_data__(data_tuples):
    for data in data_tuples:
        print "%s | %s | %s" % (data[0], data[1], data[2])
        Download.create(name=data[0], url=data[1], status=data[2])


if __name__ == "__main__":
    db.create_table(Download, True)

    for page_count in range(0, 660):
        __insert_data__(find_players(BeautifulSoup(__download_page__(page_count))))
