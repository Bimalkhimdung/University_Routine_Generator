from .labmatrix import lab_matrix
from .teacher_code import LecturerCode
from copy import deepcopy
import pickle

def lab_checkconflict(routine1,batch,overal_score):
    if batch==2075:
        allLabMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(10)]
        with open('file7.txt','wb') as f:
            pickle.dump(allLabMatrix,f)
        f.close()
    with open('file7.txt','rb') as f:
        allLabMatrix=pickle.load(f)
    ##print(allLabMatrix)
    routine1=deepcopy(routine1)
    lab_routine1 = lab_matrix(routine1,batch)
    #print(lab_routine1)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer,lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
  

    for u in range(len(lab_room_lst)):
        for i in range(6):
            for j in range(8):
                allLabMatrix[u][i][j] += lab_routine1[u][i][j]
    #print(allLabMatrix)


    score=0
    b=0
    for u in range(len(allLabMatrix)):
        for i in range(6):
            for j in range(8):
                a=allLabMatrix[u][i][j]
                if a >4:
                    b=a-2
                    score=score-(10*b)


    return score,allLabMatrix
