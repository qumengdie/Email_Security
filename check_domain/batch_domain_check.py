from check_domain_dds import check_dds
import csv

if __name__ == "__main__":
    with open('rank-uni-domain.csv', 'r') as f:
        reader = csv.reader(f)
        ori_list = list(reader)

    new_csv_list = []
    for i in range(1, len(ori_list)):
        domain = ori_list[i][2]
        res = check_dds(domain)
        tmpList = [ori_list[i][0], ori_list[i][1], ori_list[i][2], res[0], res[1], res[2], res[3]]
        new_csv_list.append(tmpList)
        print(i)

    header = ['Rank', 'University Name', 'Domain', 'MX', 'SPF', 'DKIM', 'DMARC']

    with open('final-result.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_csv_list)