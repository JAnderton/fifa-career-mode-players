from BeautifulSoup import BeautifulSoup

link = 'messi.html'
page = open(link, 'r')
soup = BeautifulSoup(page)

col1 = soup.find('div', attrs={'class': 'span-240'})
#print col1

image = col1.find('div', attrs={'class': 'span7'}).img['src']

summary = col1.find('div', attrs={'class': 'span5'})
print summary
print "\n\n\n"
lines = summary.find('ul', attrs={'class': 'unstyled'}).findAll('li')
print lines[0].span.text
print lines[1].span.text
print lines[2].span.text
print int(lines[3].span.text.split()[0])

