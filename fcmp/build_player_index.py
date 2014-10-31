import logging
import logging.config
import os
import sys
import urllib2

from BeautifulSoup import BeautifulSoup

from db_models import Download, Status, db


def find_players(players_soup):
    for tr in players_soup.table.tbody.findAll('tr'):
        for td in tr.findAll('td', attrs={'class': 'text-left'}):
            player = td.div.a
            name = player.strong.text
            url = player['href']

            yield (name, url, Status.NEW)


def __download_page__(page_number):
    logger.info("Processing page %d", page_number)
    link = "http://www.futwiz.com/en/career-mode/players?page=%s" % page_number

    return urllib2.urlopen(urllib2.Request(link, headers={'User-Agent': 'Mozilla/5.0'}))


def __insert_data__(data_tuples):
    for data in data_tuples:
        logger.debug("Name: %s | URL: %s | Status: %s", data[0], data[1], data[2])

        Download.create(name=data[0], url=data[1], status=data[2])


def __setup__():
    # Encoding
    reload(sys)
    sys.setdefaultencoding("latin-1")

    # Logging
    for attempt in range(0, 2):
        try:
            logging.config.fileConfig('../conf/logging.conf')
        except IOError as e:
            os.makedirs(os.path.dirname(e.filename))
        else:
            break
    else:
        print "Unable to create a directory for the log file. Exiting"
        exit()
    global logger
    logger = logging.getLogger()

    # Database init
    db.create_table(Download, True)


if __name__ == "__main__":
    __setup__()

    for page_count in range(0, 660):
        __insert_data__(find_players(BeautifulSoup(__download_page__(page_count))))
