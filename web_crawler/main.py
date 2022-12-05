import requests
from bs4 import BeautifulSoup
import csv

if __name__ == '__main__':
    url = 'https://www.4icu.org/cn/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('tbody')
    review_links = container.find_all('a')
    rev_url_list = []
    for link in review_links:
        link_url = link['href']
        rev_url_list.append(link_url)
    print(rev_url_list)
    print(len(rev_url_list))

    uni_web_list = []
    uni_domain_list = []
    for i in range(0, len(rev_url_list) - 1):
        rev_url = "https://www.4icu.org" + rev_url_list[i]
        response = requests.get(rev_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        a_tag = soup.find('a', {'itemprop': 'url'})
        href = a_tag['href']
        uni_web_list.append(href)
        domain = href.replace("https://www.", "")
        domain = domain.replace("http://www.", "")
        uni_domain_list.append(domain)
        print(i)

    with open('uni-rank.csv', 'r') as f:
        reader = csv.reader(f)
        uni_rank_oricsv_list = list(reader)

    new_csv_list = []
    for i in range(0, len(uni_rank_oricsv_list) - 1):
        tmpList = [uni_rank_oricsv_list[i + 1][0], uni_rank_oricsv_list[i + 1][1], uni_domain_list[i]]
        new_csv_list.append(tmpList)
    header = ['Rank', 'name', 'domain']

    with open('rank-uni-domain.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_csv_list)
