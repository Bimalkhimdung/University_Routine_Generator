from .teachermatrix import teacher_matrix
from .teacher_code import LecturerCode
from copy import deepcopy
from .teacher_code import allLecturerCode
import pickle
import os
from .lab_conflict import lab_checkconflict
from .labmatrix import lab_matrix
import itertools

# to change nested list into a one dimensional list

def oneDArray(x):
    return list(itertools.chain(*x))
def lec_checkconflict(routine1, batch,overal_score):

    lec_name, lec_Id = allLecturerCode()
    #score_from_lab,allLabMatrix=lab_checkconflict(routine1, batch,overal_score)
    if batch==276:
        allLecturerMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(len(lec_Id))]
        allTeacherMatrix= [[[0 for j in range(8)]for i in range(6)]for k in range(len(lec_Id))]
        with open('file6.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)
        f.close()
        with open('file8.txt','wb') as f:
            pickle.dump(allTeacherMatrix,f)
        f.close()
    with open('file6.txt','rb') as f:
        allLecturerMatrix=pickle.load(f)
    
    # for i in range(len(lec_Id)):
    #     print(lec_name[i])
    #     # index = lec_name.index(lec_name[i])
    #     # print(lec_Id[i])
    #     for j in range(6):
    #         print(allLecturerMatrix[i][j])

    routine=deepcopy(routine1)
    # print(routine)
    teacher_routine1 = teacher_matrix(routine,batch)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)


    # print('After calling teaacher routine')
    # for u in range(len(teacher_routine1)):
    #     name  =  lecCodeLst[u]
    #     print(name)
    #     for j in range(6):
    #         print(teacher_routine1[u][j])

    for id in lectId:
       for i in range(6):
            for j in range(8):
                index = lectId.index(id)
                allLecturerMatrix[id-1][i][j] += teacher_routine1[index][i][j]

    # print('After Addition')

    # for i in range(len(lec_Id)):
    #     print(lec_name[i])
    #     # index = lec_name.index(lec_name[i])
    #     # print(lec_Id[i])
    #     for j in range(6):
    #         print(allLecturerMatrix[i][j])


    

   
    score=0
    b=0
    for u in range(len(allLecturerMatrix)):
     for i in range(6):
            for j in range(8):
                a=allLecturerMatrix[u][i][j]
                if a>1:
                    b=a-1
                    score=score-(10*b)
                    
    # print('Hi I am a score', score)
    


    if batch==276:
        allLabMatrix = [[[0 for j in range(8)]for i in range(6)]for k in range(len(lab_room_lst))]
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


    scorelab=0
    b=0
    for u in range(len(allLabMatrix)):
        for i in range(6):
            for j in range(8):
                a=allLabMatrix[u][i][j]
                if a >4:
                    b=a-4
                    scorelab=scorelab-(10*b)

    
    if score==0 and scorelab==0 and overal_score==480:
        allTest=[]
        with open('file6.txt','wb') as f:
            pickle.dump(allLecturerMatrix,f)
        f.close()

        with open('file6.txt','rb') as f:
            allTest=pickle.load(f)

        with open('file8.txt','rb') as f:
            allTeacherMatrix=pickle.load(f)
        for u in range(len(allLecturerMatrix)):
            oneDmylist2=deepcopy(mylist2)
            oneDmylist2=oneDArray(oneDmylist2)
            for i in range(6):
                for j in range(8):
                    a=allTest[u][i][j]
                    b=allTeacherMatrix[u][i][j]
                    if a==1 and b==0:
                        if batch<300 :
                            var=str(batch-200)
                            if routine[i][j] in oneDmylist2:
                                allTeacherMatrix[u][i][j]="BEL_LAB_0"+var
                            else:
                                 allTeacherMatrix[u][i][j]="BEL_LEC_0"+var
                        else:
                            var=str(batch-300)
                            if routine[i][j] in oneDmylist2:
                                allTeacherMatrix[u][i][j]="BCT_LAB_0"+var
                            else:
                                allTeacherMatrix[u][i][j]="BCT_LEC_0"+var
                                        
        with open('file8.txt','wb') as f:
            pickle.dump(allTeacherMatrix,f)
        f.close()
        with open('file7.txt','wb') as f:
            pickle.dump(allLabMatrix,f)
        f.close()

        lec_name, lec_Id = allLecturerCode()

        if batch==277:
            #for i in range(len(lec_Id)):
            for i in range(len(lec_Id)):
                print(lec_name[i])
                index = lec_name.index(lec_name[i])
                print(lec_Id[i])
                for j in range(6):
                    print(allTeacherMatrix[i][j])
            
            print("Routine of lab classes:")

            for i in range(len(lab_room_lst)):
                print(lab_room_lst[i])
                for j in range(len(allLabMatrix[i])):
                    print(allLabMatrix[i][j])
    return score+scorelab



    
   