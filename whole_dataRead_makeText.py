import os #운영체제와 상호 작용하기 위한 라이브 러리
import sys
import xml.etree.ElementTree as ET #xml을 tree 형태로 읽어오는 라이브러리, as ET는 라이브러리를 단축시키기 위한 명령어
import shutil # 파일 및 디렉터리 작업을 수행하는 데 사용할 모듈 (파일 복사 이동 )
import random  # 난수 형성 함수
from xml.dom import minidom #xml 에 접근하기 위한 함수
import operator # list의 차를 구하기 위한 라이브 러리
import math # 표준편차를 구하기위한 수학계산 라이브러리
import numpy as np # 표준편차를 구하기위한 수학계산 라이브러리
from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
import csv
import pickle
from collections import Counter #list 중복값 카운팅 하기
import time
start = time.time()
# sys.stdout = open('output.txt','a')  #print 로 출력된 내용을 텍스트로 저장함

answer = ['car','person']
attr = ['width', 'height', 'box']
car_array = []
person_array = []
# zz=[]
# zz1=[]
car_count = 0
person_count = 0
total_box = 0
total_xml = 0
total_box_count = 0
total_car = 0
total_person = 0
person_w = []
person_h = []
car_w = []
car_h = []
other =0
c_w = []
c_h = []
p_w = []
p_h = []
p_b = []
c_b = []

c_height_list = []
c_width_list = []
c_box_len_list = []
p_height_list = []
p_width_list = []
p_box_len_list = []
path_list = []
file_list = []
name_list = []


dir_len = len(path_list)


root_path = "D:/backup/DataSet"
target_path = "D:/backup/DataSet"
parser = ET.XMLParser(encoding="utf-8")  # XMLParser는 xml에서 원하는 구문을 출력할수있게 해준다




rootpath = r"D:\backup\DataSet"

xmlRootpath = r'D:\backup\DataSet'

xmlList = []
coun=0


for (path, dir, files) in os.walk(xmlRootpath):
    for file in files:

        if file.endswith(".xml"):
        # for x in os.listdir(root_path):
        #     if x.endswith('xml'):
            empty = os.path.join(root_path,path)
            path_list.append(empty)

            total_xml += 1
            tree = ET.parse(os.path.join(empty, file))  # x에 대한정보를 가져온다
            root = tree.getroot()  # 문서의 최상단을 가리킴 여기서는 annotations
            #print(os.path.join(empty, file))
            for child in root.findall("object"): #root(annotations) 아래 자식image 의 객수만큼 반복한다)
                bndbox=child.find('bndbox')
                name = child.find('name').text
                total_box_count += 1

                xmin = int(float(bndbox.find("xmin").text))
                ymin = int(float(bndbox.find("ymin").text))
                xmax = int(float(bndbox.find("xmax").text))
                ymax = int(float(bndbox.find("ymax").text))

                # print(name+'  %s  %s  %s  %s' %(xmin, ymin, xmax, ymax))  #5


                if name == "person":

                    person_count += 1
                    total_person += 1

                    p_w = abs(float(xmin)-float(xmax))
                    p_h = abs(float(ymin)-float(ymax))
                    p_b = abs(float(p_w*p_h))
                    # print("person width=" + str(p_w), "person height" + str(p_h))
                    # print("label:person"+"  xmin:"+str(xmin)+"  ymin:"+str(ymin)+"  xmax:"+str(xmax)+"  ymax:"+str(ymax)+"   width=" + str(p_w), "   height" + str(p_h))
                    person_w.append(p_w)
                    person_h.append(p_h)
                    p_box_len_list.append(p_b)

                elif name == "car":
                    car_count += 1
                    total_car += 1
                    c_w = abs(float(xmin)-float(xmax))
                    c_h = abs(float(ymin)-float(ymax))
                    c_b = abs(float(c_w * c_h))
                    # print("car width=" + str(c_w), "car height=" + str(c_h))
                    #print("label:car" + "     xmin:" + str(xmin) + "  ymin:" + str(ymin) + "  xmax:" + str(xmax) + "  ymax:" + str(ymax) + "   width=" + str(c_w), "   height" + str(c_h))
                    car_w.append(c_w)
                    car_h.append(c_h)
                    c_box_len_list.append(c_b)
                else:
                    other += 1



            # print("car num:"+str(car_count)+"  person num:"+str(person_count))




            person_array.append(person_count)
            car_array.append(car_count)
            car_count=0
            person_count=0




person_np = np.array(person_array)
car_np = np.array(car_array)

# np.max(arr) max 값 구하기

x = np.array(person_w)#person_width
y = np.array(person_h)#person_height
z = x*y #person _w*h

zz = list(z)

# print(z)
x1 = np.array(car_w) #car width
y1 = np.array(car_h) #car height
z1 = x1*y1 #car_w*h

zz1 = list(z1)

a = round(np.average(x),2)
b = round(np.average(y),2)
c = round(np.average(z),2)
a1 = round(np.average(x1),2)
b1 = round(np.average(y1),2)
c1 = round(np.average(z1),2)

d = round(np.std(x),2)
e = round(np.std(y),2)
f = round(np.std(z),2)
d1 = round(np.std(x1),2)
e1 = round(np.std(y1),2)
f1 = round(np.std(z1),2)




#origin file 을 txt 저장
with open(target_path+'/person_w.txt', 'w') as f:
    f.writelines(str(person_w))
with open(target_path+'/person_h.txt', 'w') as f:
    f.writelines(str(person_h))
with open(target_path+'/person_area.txt', 'w') as f:
    f.writelines(str(zz))
with open(target_path+'/car_w.txt', 'w') as f:
    f.writelines(str(car_w))
with open(target_path+'/car_h.txt', 'w') as f:
    f.writelines(str(car_h))
with open(target_path+'/car_area.txt', 'w') as f:
    f.writelines(str(zz1))








sys.stdout = open(target_path+'/output.txt','a',encoding='utf8')
print(target_path)
print("total xmls:"+str(total_xml))
print("total boxes:"+str(total_box_count))
print("total person count:"+str(total_person))
print("total car count:"+str(total_car))
print("other object:"+str(other))

####################

print("person width  "+" average:"+str(a) + "  standard deviation:"+str(d)+"  min:"+str(np.min(x))+"  max:"+str(np.max(x)))
print("person height  "+" average:"+str(b) +"  standard deviation:"+str(e)+ "  min:"+str(np.min(y))+"  max:"+str(np.max(y)))
print("person width*height  "+" average:"+str(c) +"  standard deviation:"+str(f)+ "  min:"+str(np.min(z))+"  max:"+str(np.max(z)))

print("car width  "+" average:"+str(a1) +"  standard deviation:"+str(d1)+"  min:"+str(np.min(x1))+"  max:"+str(np.max(x1)))
print("car height  "+" average:"+str(b1) +"  standard deviation:"+str(e1)+ "  min:"+str(np.min(y1))+"  max:"+str(np.max(y1)))
print("car width*height  "+" average:"+str(c1) +"  standard deviation:"+str(f1)+ "  min:"+str(np.min(z1))+"  max:"+str(np.max(z1)))


