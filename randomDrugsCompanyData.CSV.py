#!/usr/bin/env python

import sys
import os
import random
import json
import pickle

v_companyNum = 500
v_drugNum = 20000
v_sparse_parentDrugId1 = 100
v_sparse_parentDrugId2 = 300

myString = ""

fileOut = open('DONTBACKUP/drugs.csv', 'wb')
for drugId in range(1,v_drugNum):
  #myString=myString+str(drugId)+';'+str(drugId)+';'+str(drugId%v_companyNum)+';'+str(random.randint(1, v_sparse_parentDrugId1))+';'+str(random.randint(1, v_sparse_parentDrugId2))+'\n'
  myString=str(drugId)+',Drg_'+str(drugId)+','+str(drugId%v_companyNum)+','+str(random.randint(1, v_sparse_parentDrugId1))+'\n'#+','+str(random.randint(1, v_sparse_parentDrugId2))+'\n'
  fileOut.write(myString)
fileOut.close()

fileOut = open('DONTBACKUP/company.csv', 'wb')
myString=""
for companyId in range(1,v_companyNum):
  #myString=myString+str(companyId)+';'+str(companyId)+'\n'
  myString=str(companyId)+',Cmp_'+str(companyId)+'\n'
  fileOut.write(myString)
fileOut.close()
