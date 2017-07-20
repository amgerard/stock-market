import urllib2

def get_data(sym):
	# read historical data for symbol
	url = "http://real-chart.finance.yahoo.com/table.csv?s={0}&d=3&e=16&f=2016&g=d&a=11&b=12&c=1980&ignore=.csv".format(sym)
	response = urllib2.urlopen(url)
	html = response.read()

	# write data to csv
	with open('data2/{0}.csv'.format(sym), 'wb') as f:
    		f.write(html)

def get_symbols():
	# read and return all symbols in S&P500
	with open("symbols.csv") as f:
    		return [x.rstrip() for x in f.readlines()]

if __name__ == "__main__":
	# save all data
	for s in get_symbols():
		try:
			get_data(s)
		except:
			print "Error " + s # 404
