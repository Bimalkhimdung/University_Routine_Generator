from routine.models import Computer_First,Computer_Second,Computer_Third,Computer_Fourth
from .db_code import code_db_calc, input_lst




def LecturerCode(batch):
    if batch == 375:
        c = Computer_Third.objects.all()
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics''Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
 
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0



    elif batch == 376:
        c = Computer_Second.objects.all()
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0
        

    elif batch == 374:
        c = Computer_Fourth.objects.all()

        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']

        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)

        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0


    elif batch == 377:
        c = Computer_First.objects.all()
        codeLst, lecCodeLst, lectId, lab_lst, lab_room, lab_lecturer,mylist1,mylist2, mylist3 = code_db_calc(c)
        lab_room_lst = ['Computer', 'Electrical', 'Instrumentation', 'Drawing', 'Chemistry', 'Physics','Thermodynamics','Electronics','Workshop','Project','Hydropower', 'Switchgear', 'Class1', 'Class2']
        if mylist2 != []:
            lab_len = len(mylist2[0])
        else:
            lab_len = 0


    return codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len


def allLecturerCode():
    lec_name = ['MKS', 'EN', 'SS', 'RN', 'LM', 'SP', 'ABT', 'SA','BS','MSM', 'KM', 'NRB', 'SK', 'GBJ','RKS','ST', 'SB', 'BS1','MBD','AA','SR','NRS','HR','AS','RA', 'DA', 'SG',  'SRB', 'PP','E2', 'E3','TBG','RK', 'Teacher_A', 'Teacher_B', 'Teacher_C','SP1']
    lec_Id =  [  1,    2,    3,     4,     5,     6,    7,    8,   9,   10,   11,   12,    13,    14,   15,  16,   17,   18,   19,   20,  21,  22,   23,  24,  25,   26,   27,    28,    29,  30,   31,  32,   33,   34, 35, 36, 37]

    return lec_name, lec_Id

