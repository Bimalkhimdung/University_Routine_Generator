from .initial_population import *
from .teacher_code import LecturerCode
import numpy as np
from copy import deepcopy
chk=[]

def calcFitness(chk,batch):
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
    maxm = max(codeLst)
    lecCount = [0 for i in range(len(lectId))]
    a = 0
    b = 0
    j = 0
    while(j <= (len(lectId)-1)):
        if(a>7):
            break
        elif codeLst[j] != 0:
            if(chk[a] <= codeLst[j]):
                lecCount[j] += 1
                j=0
                a=a+1
            elif chk[a] >=(maxm+1):
                b += 1
                a += 1
                j=0
                pass
        
            else: 
                j += 1
                pass
        else:
            j += 1
            pass

    score=0
    for j in range(len(lecCount)):
        if lecCount[j]>2:
            conflict = 0
            conflict=(lecCount[j]-2)
            score=score-(10*conflict) 

    lab_count = 0
    mylist2_2 = deepcopy(mylist2)
    mylist2_2 = np.array(mylist2_2)
    mylist2_2 = mylist2_2.flatten()
    score_lab=0
    for i in range(8):
        if chk[i] in mylist2_2:
            lab_count+=1
    if lab_count>lab_len:
        b=lab_count-lab_len
        score_lab=score_lab-(b*10)
    score=score+score_lab

    return score
     
