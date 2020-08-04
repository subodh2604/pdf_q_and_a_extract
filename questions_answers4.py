import PyPDF2 as p2 
import re
import json

qa=[]

pdffile=open("July-English2.pdf",'rb')

pdfread=p2.PdfFileReader(pdffile)
p=0
list1=[]
for i in range(72,100):
    dict1={}
    x=pdfread.getPage(i)
    x1=x.extractText()

    x1=x1.replace("\n"," ")
    x2=x1.split(" ) ")
    patt=re.compile(r'MAY  -   2019|APRIL  -   2019|MARCH  -   2019|FEBRUARY  -   2019|JANUARY  -   2019|DECEMBER  -   2018')
    #print(x1)
    matches=patt.finditer(x1)
    if matches:
        for match in matches:
            print(match)
            print(x1[match.start():match.end()])
            m=x1[match.start():match.end()]
            if p==0:
                pass
            else:
                with open(fname,'w') as f:
                    json.dump(list1,f)
                list1=[]
            p=1
    else:
        pass
    x2.pop(0)
    for j in range(len(x2)):
        question=x2[j]

        question=question[:-3]
        q_and_a=re.split(r'[?]|[:]',question)
        dict1["page"]=i
        dict1["month"]= m
        dict1["question %s"%j]=q_and_a
        #dict1["answer%s"%j]=q_and_a[1]
    qa.append(dict1)
    list1.append(dict1)
    fname=m+".json"

    #with open(fname,'w+') as f:
        #json.dump(dict1,f)

with open('qa2.json','w') as f:
    json.dump(qa,f)