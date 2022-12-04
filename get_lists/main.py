from urllib.request import urlretrieve, urlopen
import json
import csv
import urllib

if __name__ == '__main__':
    # China
    url = 'http://universities.hipolabs.com/search?country=China'
    urlretrieve(url, 'file.txt')
    # txt = urlopen(url).read()
    # print(txt)
    with open('file.txt') as f:
        data = f.read()
    oriList = json.loads(data)

    # To domains-uni-List.csv:
    newList = []
    for i in range(len(oriList)):
        domainList = oriList[i]['domains']
        domains = domainList[0]
        for j in range(1, len(domainList)):
            domains += " & " + domainList[j]
        myList = [domains, oriList[i]['name']]
        if myList not in newList:
            newList.append(myList)

    csvList = []
    for i in range(len(newList)):
        tmpList = [i + 1, newList[i][0], newList[i][1]]
        csvList.append(tmpList)

    header = ['No.', 'domain', 'name']
    print(csvList)

    with open('domainList.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(csvList)

    # To domains.txt
    with open(r'domains.txt', 'w') as fp:
        for item in csvList:
            # write each item on a new line
            fp.write("%s\n" % item[1])
        print('Done')


# # All countries:
    # url0 = 'http://universities.hipolabs.com/search'
    # urlretrieve(url0, 'whole_file.txt')
    # with open('whole_file.txt') as f:
    #     data = f.read()
    # oriDic = json.loads(data)
    # countrySet = set()
    # countryDic = {}
    # for i in range(len(oriDic)):
    #     country = oriDic[i]['country']
    #     countrySet.add(country)
    #     if country in countryDic.keys():
    #         countryDic.update({country: countryDic[country] + 1})
    #     else:
    #         countryDic.update({country: 1})
    # countrySet = sorted(countrySet)
    # print(countrySet)
    # print(len(countrySet))
    # print(countryDic)
    # print(len(countryDic))
    # for country in countrySet:
    #     x = countryDic[country]
    #     if countryDic[country] < 100:
    #         del countryDic[country]
    # print(countrySet)
    # print(len(countrySet))
    # print(countryDic)
    # print(len(countryDic))
    #
    # with open(r'countryList.txt', 'w') as fp:
    #     for country in countryDic.keys():
    #         fp.write("%s\n" % country)
    #     print('Done')

    # # store the list of every country to respective file
    # urlList = []
    # for country in countrySet:
    #     countryformat = country.replace(" ", "%20")
    #     url = 'http://universities.hipolabs.com/search?country=' + countryformat
    #     urlList.append(url)
    #     urlretrieve(url, country + ' file.txt')
    # print(urlList)