# Praveen Lama
# IS 211
# Assignment 9
# Fall 2017

from bs4 import BeautifulSoup
import urllib2


def searchCol(soupParam, header):
    table = soupParam.find_all('th')
    date_column = None
    header_row = None

    for entry in table:
        if entry.string.lower() == header.lower():
            for i in range(0, len(entry.parent.contents)):
                if entry.parent.contents[i] == entry:
                    date_column = i
                    header_row = entry.parent
    return date_column, header_row


def main():
    print "Apple Stocks Prices: \n"
    req = urllib2.Request("http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices")
    res = urllib2.urlopen(req)
    html_doc = res.read()
    soup = BeautifulSoup(html_doc, 'html5lib')
    date_col_loc = searchCol(soup, "Date")[0]
    close_col_loc = searchCol(soup, "Close")[0]
    header_row = searchCol(soup, "Date")[1]
    num_of_rows = len(header_row.parent.contents)

    for i in range(1, num_of_rows):
        cells = header_row.parent.contents[i].contents
        if len(cells) > close_col_loc:
            date = header_row.parent.contents[i].contents[date_col_loc]\
                .string
            close = header_row.parent.contents[i].contents[close_col_loc]\
                .string

            print date
            print "Closing Price: %s\n" % close


if __name__ == "__main__":
    main()