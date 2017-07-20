import urllib2
import re

def write_symbols():
	# parse wiki html for S&P500 symbols
	url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
	response = urllib2.urlopen(url)
	html = response.read()
	
	# NYSE regex
	symbols = re.findall('XNYS:([A-Z]+)"', html)

	# Nasdaq regex
	symbols.extend([x.upper() for x in re.findall('www.nasdaq.com/symbol/([a-z]+)"', html)])

	# write symbols to file
	with open('sp500_symbols.csv', 'wb') as f:
    		f.write('\n'.join(symbols))


if __name__ == "__main__":
	write_symbols()
