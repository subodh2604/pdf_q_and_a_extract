import PyPDF2 as p2 
import re
import json

qa=[]
pdffile=open("July-English2.pdf",'rb')
pdfread=p2.PdfFileReader(pdffile)

for i in range(73,100):
    dict1={}
    x=pdfread.getPage(i)
    x1=x.extractText()
    x1=x1.replace("\n"," ")
    x2=x1.split(" ) ")
    x2.pop(0)
    for j in range(len(x2)):
        question=x2[j]

        question=question[:-3]
        q_and_a=re.split(r'[?]|[:]',question)
        dict1["page"]=i
        dict1["question%s"%j]=q_and_a

    qa.append(dict1)
    dict1={}

with open('qa2.json','w') as f:
    json.dump(qa,f)