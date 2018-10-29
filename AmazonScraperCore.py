import IncludesCore
def CreateAmazonProductUrl(id):
	baseUrl = 'https://www.amazon.com/gp/offer-listing/'
	return baseUrl + id
def HasMultiplePages():
	hasPagination = False
	try:
		pagination = browser.find_element_by_class_name('a-pagination')
		hasPagination = True
	except:
		hasPagination = False
	return hasPagination	
def ScrapePrices():
	priceList = list()
	prices = browser.find_elements_by_xpath('/html/body/div[1]/div[4]/div/div[1]/div[1]/div/div/div/div[1]/span')	
	for elems in prices:
		#remove non numerical chars from string
		temp = re.sub(r'[^\d.]+','', str(elems.text))	
		priceList.append(temp)
	return priceList
def ScrapeAllPages():
	if HasMultiplePages():
		nextPageButton = ['']
		allPricesList = list()
		pages = browser.find_elements_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[2]/ul/li/a')
		for p in range(len(pages) - 1):
			allPricesList.extend(ScrapePrices())
			nextPageButton = browser.find_elements_by_class_name('a-last')
			nextPageButton[0].click() 
	allPricesListFloat = list()
	#remove empty list entries
	allPricesList = list(filter(None, allPricesList))
	for price in allPricesList:
		allPricesListFloat.append(Decimal(price))
	return allPricesListFloat 
