#Ma sinh vien: B20DCCN497
#Ho ten: Pham Hong Phong
#Nhom: 01

import csv
def Average(country, year):
    with open('DP_LIVE_16102022143222532.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        count=0
        sum=0
        for row in csv_reader:
            if row[0]==country and row[5]==year:
                sum+=float(row[6])
                count+=1
    return float(sum/count)

country = input()
year = input()
print(Average(country, year))    