from .teacher_code import LecturerCode, allLecturerCode
from copy import deepcopy 



def teacher_matrix(routine,batch):
    routine1=[]
    routine1=deepcopy(routine)
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
    teacher_routine = [[[0 for j in range(8)]for i in range(6)]for k in range(len(lectId))]


    # for theory and tutorial class
    for u in range(len(codeLst)):
        for i in range(6):
            for j in range(8):
                if routine1[i][j] <= codeLst[u]:
                    teacher_routine[u][i][j] = 1
                    routine1[i][j] = 105
                else:
                    pass


    # for lab class
    for id in range(len(lectId)):
        for u in range(len(lab_lst)):
            for i in range(6):
                for j in range(8):
                    if routine1[i][j] <= lab_lst[u]:
                        for k in lab_lecturer[u]:
                            if k in lectId:
                                index = lectId.index(k)
                                teacher_routine[index] [i][j] = 1
                        routine1[i][j] = 105        
                    else:
                        pass  

    return teacher_routine
