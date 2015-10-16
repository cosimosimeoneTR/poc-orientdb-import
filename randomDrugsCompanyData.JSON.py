#!/usr/bin/env python

import sys
import os
import random
import json
import pickle

v_companyNum = 100
v_drugNum = 20000
v_sparse_parentDrugId1 = 10
v_sparse_parentDrugId2 = 3

fileOut = open('DONTBACKUP/drugs.json', 'wb')
fileOut.write('[')
for drugId in range(1,v_drugNum):
  #myString='{'+'"drugId":"'+str(drugId)+'", "drugName":"'+'Drug '+str(drugId)+'", "companyid":"'+str(drugId%v_companyNum)+'", "relatedDrugId":["'+str(random.randint(1, v_sparse_parentDrugId1))+'", "'+str(random.randint(1, v_sparse_parentDrugId2))+'"] }\n'
  myString='{'+'"drugId":"'+str(drugId)+'", "drugName":"'+'Drug '+str(drugId)+'", "companyid":"'+str(drugId%v_companyNum)+'", "relatedDrugId":"'+str(random.randint(1, v_sparse_parentDrugId1))+'" }\n'
  if drugId != v_drugNum-1:
     myString=myString+','
  fileOut.write(myString)
fileOut.write(']')
fileOut.close()

fileOut = open('DONTBACKUP/company.json', 'wb')
fileOut.write('[')
for companyId in range(1,v_companyNum):
  myString='{"companyId":"'+str(companyId)+'", "companyName":"Company '+str(companyId)+'"}\n'
  if companyId != v_companyNum-1:
     myString=myString+','
  fileOut.write(myString)

fileOut.write(']')
fileOut.close()
