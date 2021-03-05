import csv 

with open('sample.csv','w') as f:
	x = csv.writer(f)
	rows_i = [[1,'ok'],[2,'ok2'],[3,'ok3']]
	x.writerows(rows_i)
	print('done')

with open('sample.csv','r') as f:
	x = csv.reader(f)
	for rows in x:
		print(rows)

with open('sample2.csv','r') as f:
	x = csv.reader(f,delimiter='\t')
	for rows in x:
		print(rows)


with open('sample3.csv','w') as f:
	x = csv.writer(f,delimiter="*")
	x.writerow([1,'ray'])

