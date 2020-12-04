import csv 
headers=['ID','UserName','Password','Age','Country']
# rows=[(1001,"qiye","qiye_pass",24,"China"),
# (1002,"Mary","Mary_pass",20,"USA"),(1003,"Jack","Jack_pass",20,"USA")]

rows=[{'ID':1001,'UserName':"giye",'Password':"giye_pass",'Age':24,'Country':"China"},
{'ID':1002,'UserName':"Mary",'Password':"Mary_pass",'Age':20,'Country':"USA"},
{'ID':1003,'UserName':"Jack",'Password':"Jack_pass",'Age':20,'Country':"USA"}]
# with open('qiye.csv','w') as f:
    # f_csv=csv.writer(f)
    # f_csv.writerow(headers)
    # f_csv.writerows(rows)

    # f_csv=csv.DictWriter(f,headers)
    # f_csv.writeheader()
    # f_csv.writerows(rows)
with open('qiye.csv') as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)

with open('qiye.csv') as f:
    f_csv=csv.DictReader(f)
    for row in f_csv: 
        print(row.get('UserName'), row.get('Password'))
        