from .generator import generator
import sys
from .pdf_gen import make_pdf
def call():
    score=[]
    routine=[]
    

    x=0
    batch=377
    score,routine=generator(batch)
    while 480 not in score:
        if x<120:
            print(x,batch)
            x=x+1
            score,routine=generator(batch)
            
        else:
            call()
    if len(score)==1:
        print("This is right routine for Computer First Year:",routine,score)
        make_pdf(routine,batch)
    else:
        print("This is right routine for Computer First Year:",routine[0],score)
        make_pdf(routine[0],batch)

    x=0
    batch=376
    score,routine=generator(batch)
    while 480 not in score:
        if x<30:
            x=x+1
            print(x,batch)
            score,routine=generator(batch)
        else:
            call()
    if len(score)==1:
        print("This is right routine for Computer Second Year:",routine,score)
        make_pdf(routine,batch)
    else:
        print("This is right routine for Computer Second Year:",routine[0],score)
        make_pdf(routine[0],batch)

    x=0
    batch=375
    score,routine=generator(batch)
    while 480 not in score :
        if x<10:
            print(x ,batch)
            x=x+1
            score,routine=generator(batch)
        else:
            call()
    if len(score)==1:
        print("This is right routine for Computer Third Year:",routine,score)
        make_pdf(routine,batch)
    else:
        print("This is right routine for Computer Third Year:",routine[0],score)
        make_pdf(routine[0],batch)
    x=0
    batch=374
    score,routine=generator(batch)
    while 480 not in score :
        if x<50:
            print(x ,batch)
            x=x+1
            score,routine=generator(batch)
        else:
            call()
  
    if len(score)==1:
        print("This is right routine for Computer Fourth Year:",routine,score)
        make_pdf(routine,batch)
    else:
        print("This is right routine for Computer Fourth Year:",routine[0],score)
        make_pdf(routine[0],batch)




    




