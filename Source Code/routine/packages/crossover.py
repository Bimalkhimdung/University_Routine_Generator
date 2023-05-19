import numpy as np
import itertools
import random
from .fitness import calcFitness
import sys
from copy import deepcopy
import pickle
from .teacherconflict import lec_checkconflict
from .teacher_code import LecturerCode


def oneDArray(x):
    return list(itertools.chain(*x))


# for crossover                                              

def partial_crossover(lst1, lst2, lab_len,batch):
    lst1_1 = deepcopy(lst1)
    lst2_2=deepcopy(lst2)
    x=0
    i = j = 0
    lst1off=[]
    lst2off=[]
    offspring = []
    routine_two_offspring = []  
    score_offspring_lst = []  
    x=random.randint(0,5)
    lst1off.append(lst2_2[x])
    lst2_2.pop(x)
    lst2off.append(lst1_1[x])
    lst1_1.pop(x)


    for i in range(5):
        lst1off.append(lst1_1[0])
        lst1_1.pop(0)

    for i in range(5):
        lst2off.append(lst2_2[0])
        lst2_2.pop(0)
    offspring.append(lst1off)
    offspring.append(lst2off)

    for i in range(2):
        routine = []
        routine = offspring[i]
        routinecheck=[]
        routinecheck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                        29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 100, 100, 100, 100, 100, 100]

        for i in range(6):
            for j in range(8):
                if routine[i][j] in routinecheck:
                    index = routinecheck.index(routine[i][j])
                    routinecheck.pop(index)
                else:
                    routine[i][j] = '*'

        not_present = routinecheck[:]
        arr = [[0 for q in range(10)] for p in range(6)]
        for i in range(6):
            for j in range(8):
                arr[i][j] = routine[i][j]
        present = arr[:]

        codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)



       
        mylist1 = np.array(mylist1)
        mylist1 = mylist1.flatten()
        mylist2 = np.array(mylist2)  
        mylist2 = mylist2.flatten()
        mylist3 = np.array(mylist3)
        mylist3 = mylist3.flatten()
        mis_prac = []
        mis_lec = []
        mis_tut = []
        for i in range(len(not_present)):
            if not_present[i] in mylist1:
                mis_lec.append(not_present[i])
            if not_present[i] in mylist2:
                mis_prac.append(not_present[i])
            if not_present[i] in mylist3:
                mis_tut.append(not_present[i])

        mis_prac_smp=mis_prac[:]
        mis_lec_smp=mis_lec[:]
        mis_tut_smp=mis_tut[:]

        if lab_len == 3:
            for i in range(6):
                for j in range(8):
                    if len(mis_prac_smp) != 0 and present[i][j] == '*' and present[i][j + 1] == '*' and present[i][j + 2] == '*':
                        present[i][j] = 'prac'
                        mis_prac_smp.pop(0)
                        present[i][j + 1] = 'prac'
                        mis_prac_smp.pop(0)
                        present[i][j + 2] = 'prac'
                        mis_prac_smp.pop(0)
                    elif len(mis_lec_smp) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                        present[i][j] = 'Lec'
                        mis_lec_smp.pop(0)
                        present[i][j + 1] = 'Lec'
                        mis_lec_smp.pop(0)
                    elif len(mis_tut_smp) != 0 and present[i][j] == '*':
                        present[i][j] = 'Tut'
                        mis_tut_smp.pop(0)

        if lab_len == 2:
            for i in range(6):
                for j in range(8):
                    if len(mis_prac_smp) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                        present[i][j] = 'prac'
                        mis_prac_smp.pop(0)
                        present[i][j + 1] = 'prac'
                        mis_prac_smp.pop(0)
                        

                    elif len(mis_lec_smp) != 0 and present[i][j] == '*' and present[i][j + 1] == '*':
                        present[i][j] = 'Lec'
                        mis_lec_smp.pop(0)
                        present[i][j + 1] = 'Lec'
                        mis_lec_smp.pop(0)
                        
                    elif len(mis_tut_smp) != 0 and present[i][j] == '*':
                        present[i][j] = 'Tut'
                        mis_tut_smp.pop(0)
        
        present1 = present
        present1 = np.array(present1)
        present1.flatten()
        if '*' in present1:
            return [],[]
    
    
        if lab_len == 3:
            for i in range(6):
                for j in range(8):
                    if present[i][j] == 'prac' and present[i][j + 1] == 'prac' and present[i][j + 2] == 'prac':
                        present[i][j] = mis_prac[0]
                        mis_prac.pop(0)
                        present[i][j + 1] = mis_prac[0]
                        mis_prac.pop(0)
                        present[i][j + 2] = mis_prac[0]
                        mis_prac.pop(0)
                    elif present[i][j] == 'Lec' and present[i][j + 1] == 'Lec':
                        present[i][j] = mis_lec[0]
                        mis_lec.pop(0)
                        present[i][j + 1] = mis_lec[0]
                        mis_lec.pop(0)
                    elif present[i][j] == 'Tut':
                        present[i][j] = mis_tut[0]
                        mis_tut.pop(0)

        if lab_len == 2:
            for i in range(6):
                for j in range(8):
                    if present[i][j] == 'prac' and present[i][j + 1] == 'prac':
                        present[i][j] = mis_prac[0]
                        mis_prac.pop(0)
                        present[i][j + 1] = mis_prac[0]
                        mis_prac.pop(0)
                    elif present[i][j] == 'Lec' and present[i][j + 1] == 'Lec':
                        present[i][j] = mis_lec[0]
                        mis_lec.pop(0)
                        present[i][j + 1] = mis_lec[0]
                        mis_lec.pop(0)
                    elif present[i][j] == 'Tut':
                        present[i][j] = mis_tut[0]
                        mis_tut.pop(0)

        routine_offspring = []
        for i in range(6):
            routine_offspring.append(present[i][:8])
        routine_two_offspring.append(routine_offspring)
        
        overal_score =480
        for i in range(6): 
            chk=routine_offspring[i]
            score = calcFitness(chk,batch) 
            overal_score += score

      
        scoreconflict=lec_checkconflict(routine_offspring, batch,overal_score)
        overal_score=overal_score+scoreconflict

        if overal_score==480:
            score_offspring_lst.append(overal_score)  
            return routine_two_offspring,score_offspring_lst
        score_offspring_lst.append(overal_score)

    return routine_two_offspring, score_offspring_lst
    



