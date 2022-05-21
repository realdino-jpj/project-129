import csv

dataset1 = []
dataset2 = []


with open("final.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open("archive_dataset_sorted.csv","r")as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

headers1 = dataset1[0]
star_data1 = dataset1[1:]

headers2 = dataset2[0]
star_data2 = dataset2[1:]

headers = headers1+headers2
planet_data = []
for index,data_row in enumerate(star_data1):
    planet_data.append(star_data1[index]+star_data2[index])

with open("merge_dataset.csv","a+")as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
    