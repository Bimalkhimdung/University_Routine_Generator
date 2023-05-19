from fpdf import FPDF
# from test import create_table
from copy import deepcopy
from PyPDF2 import PdfFileReader, PdfFileWriter
from .teacher_code import LecturerCode
from .pdf_code import pdf_code
import sys
import numpy as np




def make_pdf(routine1,batch):
    codeLst, lecCodeLst, lectId, lab_lst, lab_lecturer, lab_room, lab_room_lst, mylist1, mylist2, mylist3, lab_len = LecturerCode(batch)
    Lecturer_Sub, lab, lab_lecturer_code = pdf_code(batch,lecCodeLst,lectId)
    routine_str = []
    routine =deepcopy(routine1)
    
    

    for u in range(len(codeLst)):
        for i in range(6):
            for j in range(8):
                if type(routine[i][j]) != str:
                    if routine[i][j] == 100:
                        routine[i][j] = 'Break'
                    elif routine[i][j] <= codeLst[u]:

                        routine[i][j] = '\n' + lecCodeLst[u] + '(THR)' + '\n ' + Lecturer_Sub[u] + '\n'
                    else:
                        pass

    for u in range(len(lab_lst)):
        for i in range(6):
            for j in range(8):
                if type(routine[i][j]) != str:
                    if routine[i][j] <= lab_lst[u]:
                        routine[i][j] =  '\n' + lab[u]  + ' (PRC)' + '\n' + lab_lecturer_code[u] + '\n' 
                        #routine[i][j] =  '\n' + lab[u]  + '\n' + lab_lecturer_code[u] + '\n'      
                    else:
                        pass

    for i in routine:
        routine_str.append(list(map(str,i)))

    routine = routine_str[:]
    
    
    if batch == 377:
        title = 'Routine for Computer First Year'
    elif batch == 376:
        title = 'Routine for Computer Second Year'
    elif batch == 375:
        title = 'Routine for Computer Third Year'
    elif batch == 374:
        title = 'Routine for Computer Fourth Year'
    elif batch == 277:
        title = 'Routine for Electrical First Year'
    elif batch == 276:
        title = 'Routine for Electrical Second Year'
    elif batch == 275:
        title = 'Routine for Electrical Third Year'
    else:
        title = 'Routine for Electrical Fourth Year'

    
    # if batch == 377:
    #     title = 'Routine for Computer First Year'
    # elif batch == 376:
    #     title = 'Routine for Computer Second Year'
    # elif batch == 375:
    #     title = 'Routine for Computer Third Year'
    # else:
    #     title = 'Routine for Computer Fourth Year'
    

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    time = ['7:00-7:50','7:50-8:40','8:40-9:30','9:30-10:20','10:20-11:10','11:10-12:00','12:00-12:50','12:50-1:40']
    data =[]
    j = 0
    two = ['Days/Period',str(time[j]),str(time[j+1]),str(time[j+2]),str(time[j+3]),str(time[j+4]),str(time[j+5]),str(time[j+6]),str(time[j+7])]
    data.append(two)
    for i in range(6):
        j = 0
        one = [days[i],routine[i][j],routine[i][j+1],routine[i][j+2],routine[i][j+3],routine[i][j+4],routine[i][j+5],routine[i][j+6],routine[i][j+7]]
        data.append(one) 

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=10)
#create table
    table_data = data
    cell_width='even'
    data_size = 6
    title_size=12 
    align_data='L'
    align_header='L' 
    cell_width='even' 
    x_start='x_default'
    emphasize_data=[]
    emphasize_style=None
    emphasize_color=(0,0,0)
    default_style = pdf.font_style
    if emphasize_style == None:
        emphasize_style = default_style

    def get_col_widths():
        epw=pdf.w-2*pdf.l_margin
        col_width = cell_width
        if col_width == 'even':
            col_width = pdf.epw / len(data[0]) - 1  # distribute content evenly   # epw = effective page width (width of page not including margins)
            #updated by bimal
            #col_width = [col_width] * len(data[0])
        elif col_width == 'uneven':
            col_widths = []

            # searching through columns for largest sized cell (not rows but cols)
            for col in range(len(table_data[0])): # for every row
                longest = 0 
                for row in range(len(table_data)):
                    cell_value = str(table_data[row][col])
                    value_length = pdf.get_string_width(cell_value)
                    if value_length > longest:
                        longest = value_length
                col_widths.append(longest + 10) # add 4 for padding 4 Changed here
            col_width = col_widths


        elif isinstance(cell_width, list):
            col_width = cell_width  # TODO: convert all items in list to int        
        else:
            # TODO: Add try catch
            
            col_width = int(col_width)
            
        return col_width
    if isinstance(table_data, dict):
        header = [key for key in table_data]
        data = []
        for key in table_data:
            value = table_data[key]
            data.append(value)
        data = [list(a) for a in zip(*data)]

    else:
        header = table_data[0]
        data = table_data[1:]

    line_height = pdf.font_size * 2.5

    col_width = get_col_widths()
    pdf.set_font(size=title_size)
    if x_start == 'C':
        table_width = 0
        if isinstance(col_width, list):
            for width in col_width:
                table_width += width
        else: # need to multiply cell width by number of cells to get table width 
            table_width = col_width * len(table_data[0])
        # Get x start by subtracting table width from pdf width and divide by 2 (margins)
        margin_width = pdf.w - table_width
        # TODO: Check if table_width is larger than pdf width

        center_table = margin_width / 2 # only want width of left margin not both
        x_start = center_table
        pdf.set_x(x_start)
    elif isinstance(x_start, int):
        pdf.set_x(x_start)
    elif x_start == 'x_default':
        x_start = pdf.set_x(pdf.l_margin)


    # TABLE CREATION #

    # add title
    if title != '':
        pdf.multi_cell(0, line_height, title, border=0, align='j', ln=3, max_line_height=pdf.font_size)
        pdf.ln(line_height) # move cursor back to the left margin

    pdf.set_font(size=data_size)
    # add header
    y1 = pdf.get_y()
    if x_start:
        x_left = x_start
    else:
        x_left = pdf.get_x()
    x_right = pdf.epw + x_left
    if  not isinstance(col_width, list):
        if x_start:
            pdf.set_x(x_start)
        for datum in header:
            pdf.multi_cell(col_width, line_height, datum, border=0, align=align_header, ln=3, max_line_height=pdf.font_size)
            x_right = pdf.get_x()
        pdf.ln(line_height) # move cursor back to the left margin
        y2 = pdf.get_y()
        pdf.line(x_left,y1,x_right,y1)
        pdf.line(x_left,y2,x_right,y2)

        for row in data:
            if x_start: # not sure if I need this
                pdf.set_x(x_start)
            for datum in row:
                if datum in emphasize_data:
                    pdf.set_text_color(*emphasize_color)
                    pdf.set_font(style=emphasize_style)
                    pdf.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font(style=default_style)
                else:
                    pdf.multi_cell(col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named pdf
            pdf.ln(line_height) # move cursor back to the left margin
    
    else:
        if x_start:
            pdf.set_x(x_start)
        for i in range(len(header)):
            datum = header[i]
            pdf.multi_cell(col_width[i], line_height, datum, border=0, align=align_header, ln=3, max_line_height=pdf.font_size)
            x_right = pdf.get_x()
        pdf.ln(line_height) # move cursor back to the left margin
        y2 = pdf.get_y()
        pdf.line(x_left,y1,x_right,y1)
        pdf.line(x_left,y2,x_right,y2)


        for i in range(len(data)):
            if x_start:
                pdf.set_x(x_start)
            row = data[i]
            for i in range(len(row)):
                datum = row[i]
                if not isinstance(datum, str):
                    datum = str(datum)
                adjusted_col_width = col_width[i]
                if datum in emphasize_data:
                    pdf.set_text_color(*emphasize_color)
                    pdf.set_font(style=emphasize_style)
                    pdf.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font(style=default_style)
                else:
                    pdf.multi_cell(adjusted_col_width, line_height, datum, border=0, align=align_data, ln=3, max_line_height=pdf.font_size) # ln = 3 - move cursor to right with same vertical offset # this uses an object named pdf
            pdf.ln(line_height) # move cursor back to the left margin
    y3 = pdf.get_y()
    pdf.line(x_left,y3,x_right,y3)
    pdf.ln()
    
    #Verical Line
    pdf.line(x1=10, y1=19,x2=10,y2=80.5)
    pdf.line(x1=25, y1=19,x2=25,y2=80.5)
    pdf.line(x1=49, y1=19,x2=49,y2=80.5)
    
    pdf.line(x1=70, y1=19,x2=70,y2=80.5)
    pdf.line(x1=90, y1=19,x2=90,y2=80.5)
    
    pdf.line(x1=110, y1=19,x2=110,y2=80.5)
    pdf.line(x1=128, y1=19,x2=128,y2=80.5)
    
    pdf.line(x1=150, y1=19,x2=150,y2=80.5)
    pdf.line(x1=170, y1=19,x2=170,y2=80.5)
    pdf.line(x1=191, y1=19,x2=191,y2=80.5)
    
    #horizontal
    pdf.line(x1=10, y1=37,x2=191,y2=37)
    pdf.line(x1=10, y1=47,x2=191,y2=47)
    pdf.line(x1=10, y1=55,x2=191,y2=55)
    pdf.line(x1=10, y1=64,x2=191,y2=64)
    pdf.line(x1=10, y1=73,x2=191,y2=73)
    
   
    # def horizontal(pdf,x1,y1,x2,y2):
    #     pdf.line(x1=x1, y1=y1, x2=x2, y2=y2)
    #     pdf.line(x1=x1+15,y1=y1, x2=x2+15, y2=y2+62)
    #     return(x1+15,y1,x2+15,y2+62)

    

 
    if batch==276:
        pdf.output('output1_fun.pdf')
    elif batch==376:
        pdf.output('output2_fun.pdf')
    elif batch==374:
        pdf.output('output3_fun.pdf')
    elif batch==375:
        pdf.output('output4_fun.pdf')
    elif batch==377:
        pdf.output('output5_fun.pdf')
    elif batch==274:
        pdf.output('output6_fun.pdf')
    elif batch==275:
        pdf.output('output7_fun.pdf')
    elif batch==277:
        pdf.output('output8_fun.pdf')
        output = PdfFileWriter()
        pdf1 = PdfFileReader(open(r"D:\NCE_Project\output1_fun.pdf", "rb"))
        pdf2 = PdfFileReader(open(r"D:\NCE_Project\output2_fun.pdf", "rb"))
        pdf3 = PdfFileReader(open(r"D:\NCE_Project\output3_fun.pdf", "rb"))
        pdf4 = PdfFileReader(open(r"D:\NCE_Project\output4_fun.pdf", "rb"))
        pdf5 = PdfFileReader(open(r"D:\NCE_Project\output5_fun.pdf", "rb"))
        pdf6 = PdfFileReader(open(r"D:\NCE_Project\output6_fun.pdf", "rb"))
        pdf7 = PdfFileReader(open(r"D:\NCE_Project\output7_fun.pdf", "rb"))
        pdf8 = PdfFileReader(open(r"D:\NCE_Project\output8_fun.pdf", "rb"))
        
        
        output.addPage(pdf1.getPage(0))
        output.addPage(pdf2.getPage(0))
        output.addPage(pdf3.getPage(0))
        output.addPage(pdf4.getPage(0))
        output.addPage(pdf5.getPage(0))
        output.addPage(pdf6.getPage(0))
        output.addPage(pdf7.getPage(0))
        output.addPage(pdf8.getPage(0))

        outputStream = open(r"output.pdf", "wb")
        output.write(outputStream)
        outputStream.close()