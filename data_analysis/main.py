import csv

if __name__ == '__main__':
    with open('final-result.csv', 'r') as f:
        reader = csv.reader(f)
        ori_list = list(reader)

    new_list = [ori_list[0]]
    for item in ori_list:
        if len(item[3]) != 2:
            new_list.append(item)

    with open('final-result-1.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(new_list)
