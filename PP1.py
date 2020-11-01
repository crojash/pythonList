import csv

f = open('spi_global_rankings.csv', 'r')
reader = csv.reader(f)

data = []
league = []
next(reader)

for row in reader:
    data.append([int (row[0]), row[2], row[3]])
    league.append(row[3])

league = list(set(league))

#DATA LOADED

print("Global Club Soccer Rankings •By League• SPI global rankings table")
print("https://projects.fivethirtyeight.com/global-club-soccer-rankings/?ex_cid=irpromo")
print("Please enter the number corresponding to a league; 99 to quit \n \n")

for item in league:
    index = league.index(item)
    print(index, "  ", item)
#Ask user for a number
index = int(input())


while (index < 36):
    for item in data:
        if item.__contains__(league[index]):
            print(item)
    print("Please enter the number corresponding to a league; 99 to quit \n \n")
    index = int(input())
print("Program Terminated")


