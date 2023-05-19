from operator import le
from routine.models import *

def input_lst(lst):
    newlist = []
    for word in lst:
        word = word.split(",")
        newlist.extend(word)  
    
    return newlist


def pdf_code(batch,lecCodeLst,lectId):
    if batch == 375:
        c = Computer_Third.objects.all()
        Lecturer_Sub = []
        lab = []
        
        lab_lecturer_code = []
        for code in c:
            lab_lec = []
            lab_leccode = []
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Subject)
                lab_leccode.append(code.Lab_Lec_Period)
                lab_leccode = input_lst(lab_leccode)
                lab_leccode = list(map(int,lab_leccode))
                
                for i in lab_leccode:
                    index = lectId.index(i)
                    lab_lec.append(lecCodeLst[index])
                lab_lecturer_code.append(lab_lec)
                

        
        lab_lecturer_code = ['+ '.join([str(c) for c in lst]) for lst in lab_lecturer_code]
        
        

        return Lecturer_Sub, lab, lab_lecturer_code

    if batch == 376:
        c = Computer_Second.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_lecturer_code = []
        for code in c:
            lab_lec = []
            lab_leccode = []
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Subject)
                lab_leccode.append(code.Lab_Lec_Period)
                lab_leccode = input_lst(lab_leccode)
                lab_leccode = list(map(int,lab_leccode))
                
                for i in lab_leccode:
                    index = lectId.index(i)
                    lab_lec.append(lecCodeLst[index])
                lab_lecturer_code.append(lab_lec)
                

        lab_lecturer_code = ['+ '.join([str(c) for c in lst]) for lst in lab_lecturer_code]

        return Lecturer_Sub, lab, lab_lecturer_code
    
    if batch == 377:
        c = Computer_First.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_lecturer_code = []
        for code in c:
            lab_lec = []
            lab_leccode = []
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Subject)
                lab_leccode.append(code.Lab_Lec_Period)
                lab_leccode = input_lst(lab_leccode)
                lab_leccode = list(map(int,lab_leccode))
               
                for i in lab_leccode:
                    index = lectId.index(i)
                    lab_lec.append(lecCodeLst[index])
                lab_lecturer_code.append(lab_lec)
                

        
        lab_lecturer_code = ['+ '.join([str(c) for c in lst]) for lst in lab_lecturer_code]
        
        return Lecturer_Sub, lab, lab_lecturer_code
    
    if batch == 374:
        c = Computer_Fourth.objects.all()
        Lecturer_Sub = []
        lab = []
        lab_lecturer_code = []
        for code in c:
            lab_lec = []
            lab_leccode = []
            Lecturer_Sub.append(code.Lecturer_Subject)
            if code.Lab_Class != '':
                lab.append(code.Lab_Subject)
                lab_leccode.append(code.Lab_Lec_Period)
                lab_leccode = input_lst(lab_leccode)
                lab_leccode = list(map(int,lab_leccode))
               
                for i in lab_leccode:
                    index = lectId.index(i)
                    lab_lec.append(lecCodeLst[index])
                lab_lecturer_code.append(lab_lec)
                

        
        lab_lecturer_code = ['+ '.join([str(c) for c in lst]) for lst in lab_lecturer_code]
        
        return Lecturer_Sub, lab, lab_lecturer_code
    
    
    

