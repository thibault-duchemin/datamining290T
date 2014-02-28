#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
from collections import Counter, defaultdict
import csv

(
    CMTE_ID, AMNDT_IND, RPT_TP, TRANSACTION_PGI, IMAGE_NUM, TRANSACTION_TP,
    ENTITY_TP, NAME, CITY, STATE, ZIP_CODE, EMPLOYER, OCCUPATION,
    TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID, CAND_ID, TRAN_ID, FILE_NUM,
    MEMO_CD, MEMO_TEXT, SUB_ID
) = range(22)

CANDIDATES = {
    'P80003338': 'Obama',
    'P80003353': 'Romney',
}

############### Set up variables
# TODO: declare datastructures
Obama = 1.0   
Romney = 1.0
BigList = []
Gini_Zipcode = []
ratioDict = {}
############### Read through files
for row in csv.reader(fileinput.input(), delimiter='|'):
    candidate_id = row[CAND_ID]
    if candidate_id not in CANDIDATES:
        continue
    candidate_name = CANDIDATES[candidate_id]
    zip_code = row[ZIP_CODE][:5]
    if candidate_name == 'Obama':
        Obama += 1
    else:
        Romney += 1
    BigList.append((zip_code,candidate_name))

#Creating the dictionnary list
orderedDict = defaultdict(list)
for i,j in BigList:
    orderedDict[i].append(j)
del orderedDict['']

for i in orderedDict.items():
    cnt = Counter()
    for candidate in i[1]:
        cnt[candidate] += 1
    D = dict(cnt)
    orderedDict[i[0]] = D #replace the spread out list [obama, romney, obama, obama] by {'obama' = 3, 'romney' = 1}

#Calculating gini by zipcode
for zipcode in orderedDict.items():
    oc = 0.0
    rc = 0.0
    if 'Obama' in zipcode[1].keys():
        oc = (zipcode[1]['Obama'])*1.0   
    if 'Romney' in zipcode[1].keys():
        rc = (zipcode[1]['Romney'])*1.0
    gini_zip = 1.00 - pow((oc/(rc+oc)),2) - pow((rc/(rc+oc)),2)
    ratio = (oc+rc)/(Obama + Romney)
    ratioDict[zipcode[0]] = ratio
    Gini_Zipcode.append([zipcode[0],gini_zip])
# current Gini Index using candidate name as the class

gini_std = 1 - (Obama/(Obama*Romney))**2 - (Romney/(Obama+Romney))**2  
# weighted average of the Gini Indexes using candidate names, split up by zip code
split_gini = 0 
for zipcode in Gini_Zipcode:
    split_gini += ratioDict[zipcode[0]]*zipcode[1]

#print "List %s" % orderedDict.items()
print "Gini Index: %s" % gini_std
print "Gini Index after split, zip_gini*zip_weight: %s" % split_gini
print "Obama: %s" % int(Obama)
print "Romney: %s" % int(Romney)
