from PIL import Image
import sys
import codecs
import pyocr
import pyocr.builders
from bs4 import BeautifulSoup

tool = pyocr.get_available_tools()[0]
langs = tool.get_available_languages()
lang = langs[24]
#영어 24 한글 57
builder = pyocr.builders.LineBoxBuilder()
line_boxes = tool.image_to_string(
    Image.open('final_test.png'),
    lang=lang,
    builder=builder
)
print("Will use lang '%s'" % (lang))


with codecs.open("toto4_test.html", 'w', encoding='utf-8') as file_descriptor:
    builder.write_file(file_descriptor, line_boxes)
print("complete hocr")

#soup = BeautifulSoup(open("./toto4_test.html").decode('utf-8'),"html.parser")
with open("./toto4_test.html",'rb') as html:
    soup = BeautifulSoup(html)
print("open hocr completed")
mr = soup.find_all(class_="ocr_line")
sizeLine = len(mr)
i = 0
result=0
sum=0
print("begining detect")
tempSize = 0

while i<sizeLine:
    table_temp=mr[i].find_all(class_="ocrx_word")
    tempSize = len(table_temp)
    x=0
    before=0
    after=0
    flag = False
    while x<tempSize:
        tempStr = str(table_temp[x])
        if(tempStr[36]==' '):
            after = 0
        elif(tempStr[37]==' '):
            after=int(tempStr[36:37])
        elif(tempStr[38] == ' '):
            after=int(tempStr[36:38])
        else:
            after=int(tempStr[36:39])
        if(tempSize<1 and after<100):
            flag=True
            break
        sum+=1
        if(x==tempSize-1 and after<before):
            result+=1
            print("this line is upsidedown")
        before=after
        x+=1
    i+=1
    print("end of line")
    del table_temp[:]

finalResult = (result/sum)*100
print("finalResult %d",finalResult)

if(finalResult>50):
    print("it is upside down!!")
else:
    print("it is alright!!")