list1 = ['gopi', 'krishna', 'salt', 100, 'ampashayya Naveen']

# for x in list1:
#   print(x)


dict1 = {"Name": "Kumar", "Age": 25, "guage": 56, "kisthi": "100 cm"}
# #x = dict1["Name"]
for k,v in dict1.iteritems():
    if k == 'Name':
        if v == 'Kumar':
            print(dict1['kisthi'])