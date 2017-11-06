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
        if entry.string is not None and \
                        entry.string.lower() == header.lower():
            for i in range(0, len(entry.parent.contents)):
                if entry.parent.contents[i] == entry:
                    date_column = i
    return date_column


def main():
    req = urllib2.Request("http://www.cbssports.com/nfl/stats/playersort/nfl/year-2017-season-regular-category-touchdowns/")
    res = urllib2.urlopen(req)
    html_doc = res.read()
    soup = BeautifulSoup(html_doc, 'html5lib')
    table = soup.find_all('a')
    name_column = searchCol(soup, "player")
    position_column = searchCol(soup, "pos")
    team_column = searchCol(soup, "team")
    td_column = searchCol(soup, "td")

    print "Here are the 2017 Top 20 NFL Player by Touchdowns:\n"

    counter = 1
    for entry in table:
        if entry['href'][:24] == "/nfl/players/playerpage/":
            player_record = entry.parent.parent
            player_name = player_record.contents[name_column].string
            player_position = player_record.contents[position_column].string
            player_team = player_record.contents[team_column].string
            player_touchdowns = player_record.contents[td_column].string

            print "Name: %s\n Position: %s\n Team: %s\n Touchdowns: %s\n" % \
                  (player_name, player_position, player_team,
                   player_touchdowns)

            counter += 1

        if counter > 20:
            break


if __name__ == "__main__":
    main()