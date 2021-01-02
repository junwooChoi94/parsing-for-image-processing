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
from collections import Counter #list 중복값 카운팅 하기


# sys.stdout = open('output.txt','a')  #print 로 출력된 내용을 텍스트로 저장함


car_array = []
person_array = []

obj_counter = 0
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
p_a = []
c_a = []
key_path ={}
c_height_list = []
c_width_list = []
c_box_len_list = []
p_height_list = []
p_width_list = []
p_box_len_list = []
path_list = []
file_list = []
name_list = []
value=[]
dir_len = len(path_list)


root_path = "D:/backup/DataSet"
target_path = "D:/backup/DataSet"
parser = ET.XMLParser(encoding="utf-8")  # XMLParser는 xml에서 원하는 구문을 출력할수있게 해준다

save_path = ""

xmlRootpath = r'D:\backup\DataSet'

xmlList = []
coun=0


f = open(f"D:/backup/DataSet/dic_v4_test.txt", "w")

for (path, dir, files) in os.walk(xmlRootpath):
    for file in files:
        # print(file)
        if file.endswith(".xml"):
            empty = os.path.join(root_path,path)
            path_list.append(empty)

            total_xml += 1
            tree = ET.parse(os.path.join(empty, file))  # x에 대한정보를 가져온다
            root = tree.getroot()  # 문서의 최상단을 가리킴 여기서는 annotations

            for child in root.findall('filename'):
                filename = root.find("filename").text
                for child in root.findall("object"): #root(annotations) 아래 자식image 의 객수만큼 반복한다)

                    bndbox=child.find('bndbox')
                    name = child.find('name').text
                    total_box_count += 1

                    xml_root_path = (empty+"\\"+file)


                    xmin = int(float(bndbox.find("xmin").text))
                    ymin = int(float(bndbox.find("ymin").text))
                    xmax = int(float(bndbox.find("xmax").text))
                    ymax = int(float(bndbox.find("ymax").text))

                    # print(name+'  %s  %s  %s  %s' %(xmin, ymin, xmax, ymax))  #5


                    if name == "person":
                        obj_counter += 1
                        p_w = abs(float(xmin)-float(xmax))
                        p_h = abs(float(ymin)-float(ymax))
                        p_a = abs(float(p_w*p_h))
                        # printdp("person width=" + str(p_w), "person height" + str(p_h))
                        # print("label:person"+"  xmin:"+str(xmin)+"  ymin:"+str(ymin)+"  xmax:"+str(xmax)+"  ymax:"+str(ymax)+"   width=" + str(p_w), "   height" + str(p_h))
                        value = [xml_root_path,'person',str(obj_counter),  str(p_w), str(p_h), str(p_a), filename]
                        print(value)
                        f.write(value[0]+" "+value[1]+ " " +value[2]+" "+value[3] + " " + value[4] + " " + value[5] + " " + value[6] + " " +"\n")
                    elif name == "car":
                        obj_counter += 1
                        c_w = abs(float(xmin)-float(xmax))
                        c_h = abs(float(ymin)-float(ymax))
                        c_a = abs(float(c_w * c_h))
                        # print("car width=" + str(c_w), "car height=" + str(c_h))
                        #print("label:car" + "     xmin:" + str(xmin) + "  ymin:" + str(ymin) + "  xmax:" + str(xmax) + "  ymax:" + str(ymax) + "   width=" + str(c_w), "   height" + str(c_h))
                        value = [xml_root_path,'car',str(obj_counter), str(c_w), str(c_h), str(c_a), filename]

                        f.write(value[0]+" "+value[1]+ " " +value[2]+" "+value[3] + " " + value[4] + " " + value[5] + " " + value[6] + " " + "\n")
                    else:
                        other += 1
                obj_counter = 0



                person_array.append(person_count)
                car_array.append(car_count)
                car_count=0
                person_count=0

f.close()

