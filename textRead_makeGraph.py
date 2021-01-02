# -*- coding: utf-8 -*-
import os  # 운영체제와 상호 작용하기 위한 라이브 러리
import sys
import xml.etree.ElementTree as ET  # xml을 tree 형태로 읽어오는 라이브러리, as ET는 라이브러리를 단축시키기 위한 명령어
import shutil  # 파일 및 디렉터리 작업을 수행하는 데 사용할 모듈 (파일 복사 이동 )
import random  # 난수 형성 함수
from xml.dom import minidom  # xml 에 접근하기 위한 함수
import operator  # list의 차를 구하기 위한 라이브 러리
import math  # 표준편차를 구하기위한 수학계산 라이브러리
import numpy as np  # 표준편차를 구하기위한 수학계산 라이브러리
from matplotlib import pyplot as plt
import pandas as pd
from math import sqrt
from collections import Counter
import csv
from openpyxl import workbook
from IPython.core.interactiveshell import InteractiveShell
from collections import  Counter
from os import listdir
from os import walk


InteractiveShell.ast_node_interactivity = "all"

# sys.stdout = open('output.txt','a')  #print 로 출력된 내용을 텍스트로 저장함

answer = ['car', 'person']
attr = ['width', 'height', 'box']
car_array = []
person_array = []

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
other = 0
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
person_area=[]
car_area=[]

# root_path = r"D:\backup\DataSet"
target_path = r"D:\backup\DataSet\UniTrain10"
_path= os.listdir(root_path)

parser = ET.XMLParser(encoding="utf-8")  # XMLParser는 xml에서 원하는 구문을 출력할수있게 해준다



def convert_string_to_float(n):
    return float(n)

def convert_string_to_int(n):
    return int(n)

for x in os.listdir(target_path):

    if x.endswith('txt'):

        zom = os.path.join(target_path ,x)

        if x.startswith("person_w"):
            with open(zom) as f:
                for line in f:
                    line = line.strip("[")
                    line = line.strip("]")
                    numbers_float = list(map(convert_string_to_float, line.split(',')))
                    # print(type(numbers_float[0]))
                    person_w=numbers_float
                    # print(type(person_w[0]))
        elif x.startswith("person_h"):
            with open(zom) as f:
                for line in f:
                    line = line.strip("[")
                    line = line.strip("]")
                    numbers_float = list(map(convert_string_to_float, line.split(',')))
                    # print(type(numbers_float[0]))
                    person_h = numbers_float
                    # print(person_h)
        elif x.startswith("person_area"):
            with open(zom) as f:
                for line in f:
                    line = line.strip("[")
                    line = line.strip("]")
                    numbers_float = list(map(convert_string_to_float, line.split(',')))
                    # print(type(numbers_float[0]))
                    p_box_len_list = numbers_float
                    # print(person_area)
        elif x.startswith("car_w"):
            with open(zom) as f:
                for line in f:
                    line = line.strip("[")
                    line = line.strip("]")
                    numbers_float = list(map(convert_string_to_float, line.split(',')))
                    # print(type(numbers_float[0]))
                    car_w = numbers_float
                    # print(car_w)
        elif x.startswith("car_h"):
            with open(zom) as f:
                for line in f:
                    line = line.strip("[")
                    line = line.strip("]")
                    numbers_float = list(map(convert_string_to_float, line.split(',')))
                    # print(type(numbers_float[0]))
                    car_h = numbers_float
                    # print(car_h)
        elif x.startswith("car_area"):
            with open(zom) as f:
                for line in f:
                    line = line.strip("[")
                    line = line.strip("]")
                    numbers_float = list(map(convert_string_to_float, line.split(',')))
                    # print(type(numbers_float[0]))
                    c_box_len_list = numbers_float
                    #print(car_area)

                    # person_w = list(map(float, person_w))
                    # person_w=[float (i) for i in person_w]






#sort
person_w.sort()
person_h.sort()
p_box_len_list.sort()

car_w.sort()
car_h.sort()
c_box_len_list.sort()

p_w_max_list = []
p_h_max_list = []
p_b_max_list = []
file_count = 0


print("그래프 생성")

#answer = ['car','person']
#attr = ['width', 'height', 'box']

for label_type in answer:
    for attr_type in attr:
        w_label = []
        w_count = []
        h_label = []
        h_count = []
        b_label = []
        b_count = []
        if attr_type == 'width':
            if label_type == 'car':
                for x in car_w:
                    if not(x in w_label): #width 값을 더해준다
                        w_label.append(x)
                for x in range(0, len(w_label)):
                    w_count.append(0)
                for x in car_w:
                    if x in w_label:
                        index = w_label.index(x)
                        w_count[index] += 1
            if label_type == 'person':
                for x in person_w:
                    if not(x in w_label):
                        w_label.append(x)
                for x in range(0, len(w_label)):
                    w_count.append(0)
                for x in person_w:
                    if x in w_label:
                        index = w_label.index(x)
                        w_count[index] += 1
            file_count += 1
            # x = w_label / y = w_count
            plt.figure(figsize=(10, 10)) #figsize=(10, 10)
            plt.xlabel('Width len')
            plt.ylabel('Count')

            plt.bar(w_label, w_count, color='r', alpha=0.5) #################################alpha=0.5////plt.plot(w_label, w_count, c='r', alpha=0.5)
            plt.grid()
            if label_type == 'car':
                plt.bar(w_label, w_count, color='r', alpha=0.5)###################################, alpha=0.5
                plt.ylim(-100, max(w_count))
                plt.title('%s %s' % (label_type, attr_type))
                c_std_w = np.std(car_w)
                c_w_m = np.mean(car_w)
                min_index = w_count.index(min(w_count))
                c_w_min_count = w_count[min_index]
                c_w_min_label = w_label[min_index]
                max_index = w_count.index(max(w_count))
                c_w_max_count = w_count[max_index]
                c_w_max_label = w_label[max_index]
                c_w_x_max = max(w_label)
                c_w_x_min = min(w_label)
                df = pd.DataFrame(
                    {
                        "Count" : w_count
                    }, index = w_label
                )
                xlsx_file = os.path.join(target_path, 'Dataset_%s_%s.xlsx' % (label_type, attr_type))
                df.to_excel(xlsx_file)
            if label_type == 'person':
                plt.title('%s %s' % (label_type, attr_type))
                p_std_w = np.std(person_w)
                p_w_m = np.mean(person_w)
                min_index = w_count.index(min(w_count))
                p_w_min_count = w_count[min_index]
                p_w_min_label = w_label[min_index]
                max_index = w_count.index(max(w_count))
                p_w_max_count = w_count[max_index]
                p_w_max_label = w_label[max_index]
                p_w_x_max = (max(w_label))
                p_w_x_min = min(w_label)
                count = 0
                for x in w_count:
                    if p_w_max_count == x:
                        p_w_max_list.append(w_label[count])
                    count += 1
                df = pd.DataFrame(
                    {
                        "Count" : w_count
                    }, index = w_label
                )
                xlsx_file = os.path.join(target_path, 'Dataset_%s_%s.xlsx' % (label_type, attr_type))
                df.to_excel(xlsx_file)
            file_path = os.path.join(target_path,'Dataset_%s_%s.jpg' % (label_type, attr_type))
            plt.savefig(file_path)

        if attr_type == 'height':
            if label_type == 'car':
                for x in car_h:
                    if not (x in h_label):
                        h_label.append(x)
                for x in range(0, len(h_label)):
                    h_count.append(0)
                for x in car_h:
                    if x in h_label:
                        index = h_label.index(x)
                        h_count[index] += 1
            if label_type == 'person':
                for x in person_h:
                    if not (x in h_label):
                        h_label.append(x)
                for x in range(0, len(h_label)):
                    h_count.append(0)
                for x in person_h:
                    if x in h_label:
                        index = h_label.index(x)
                        h_count[index] += 1
            file_count += 1
            plt.figure(figsize=(10, 10))  ##figsize=(10, 10)
            plt.xlabel('Height len')
            plt.ylabel('Count')

            plt.bar(h_label, h_count, color='r', alpha=0.5)############################
            plt.grid()
            if label_type == 'car':
                plt.title('%s %s' % (label_type, attr_type))
                plt.ylim(-100, max(h_count))
                c_std_h = np.std(car_h)
                c_h_m = np.mean(car_h)
                min_index = h_count.index(min(h_count))
                c_h_min_count = h_count[min_index]
                c_h_min_label = h_label[min_index]
                max_index = h_count.index(max(h_count))
                c_h_max_count = h_count[max_index]
                c_h_max_label = h_label[max_index]
                c_h_x_max = max(h_label)
                c_h_x_min = min(h_label)
                df = pd.DataFrame(
                    {
                        "Count" : h_count
                    }, index = h_label
                )
                xlsx_file = os.path.join(target_path, 'Dataset_%s_%s.xlsx' % (label_type, attr_type))
                df.to_excel(xlsx_file)
            else:
                plt.title('%s %s' % (label_type, attr_type))
                p_std_h = np.std(person_h)
                p_h_m = np.mean(person_h)
                min_index = h_count.index(min(h_count))
                p_h_min_count = h_count[min_index]
                p_h_min_label = h_label[min_index]
                max_index = h_count.index(max(h_count))
                p_h_max_count = h_count[max_index]
                p_h_max_label = h_label[max_index]
                p_h_x_max = max(h_label)
                p_h_x_min = min(h_label)
                count = 0
                for x in h_count:
                    if p_h_max_count == x:
                        p_h_max_list.append(h_label[count])
                    count += 1
                df = pd.DataFrame(
                    {
                        "Count" : h_count
                    }, index = h_label
                )
                xlsx_file = os.path.join(target_path, 'Dataset_%s_%s.xlsx' % (label_type, attr_type))
                df.to_excel(xlsx_file)
            file_path = os.path.join(target_path,'Dataset_%s_%s.jpg' % (label_type, attr_type))
            plt.savefig(file_path)
        if attr_type == 'box':
            if label_type == 'car':
                for x in c_box_len_list:
                    if not (x in b_label):
                        b_label.append(x)
                for x in range(0, len(b_label)):
                    b_count.append(0)
                for x in c_box_len_list:
                    if x in b_label:
                        index = b_label.index(x)
                        b_count[index] += 1
            if label_type == 'person':
                for x in p_box_len_list:
                    if not (x in b_label):
                        b_label.append(x)
                for x in range(0, len(b_label)):
                    b_count.append(0)
                for x in p_box_len_list:
                    if x in b_label:
                        index = b_label.index(x)
                        b_count[index] += 1
            count = 0
            # for x in b_count:
            #     if x <= 2:
            #         b_count.pop(count)
            #         b_label.pop(count)
            #     count += 1
            file_count += 1
            plt.figure(figsize=(20, 10)) #figsize=(20, 10)
            plt.xlabel('Box len')
            plt.ylabel('Count')
            plt.bar(b_label, b_count, width=300, color='r', alpha=0.5)  ############ 박스라인
            plt.ylim(-10, max(b_count))

            # plt.xlim(-15000, max(b_label))
            if label_type == 'car':
                plt.title('%s %s' % (label_type, attr_type))
                plt.xticks(np.arange(0, max(b_label), step=100000))
                c_std_b = np.std(c_box_len_list)
                c_b_m = np.mean(c_box_len_list)
                min_index = b_count.index(min(b_count))
                c_b_min_count = b_count[min_index]
                c_b_min_label = b_label[min_index]
                max_index = b_count.index(max(b_count))
                c_b_max_count = b_count[max_index]
                c_b_max_label = b_label[max_index]
                c_b_x_max = max(b_label)
                c_b_x_min = min(b_label)
                df = pd.DataFrame(
                    {
                        "Count" : b_count
                    }, index = b_label
                )
                xlsx_file = os.path.join(target_path, 'Dataset_%s_%s.xlsx' % (label_type, attr_type))
                df.to_excel(xlsx_file)
            else:
                plt.title('%s %s' % (label_type, attr_type))
                plt.xticks(np.arange(0, max(b_label), step=10000))
                p_std_b = np.std(p_box_len_list)
                p_b_m = np.mean(p_box_len_list)
                min_index = b_count.index(min(b_count))
                p_b_min_count = b_count[min_index]
                p_b_min_label = b_label[min_index]
                max_index = b_count.index(max(b_count))
                p_b_max_count = b_count[max_index]
                p_b_max_label = b_label[max_index]
                p_b_x_max = max(b_label)
                p_b_x_min = min(b_label)
                count = 0
                for x in b_count:
                    if p_b_max_count == x:
                        p_b_max_list.append(b_label[count])
                    count += 1
                df = pd.DataFrame(
                    {
                        "Count" : b_count
                    }, index = b_label
                )
                xlsx_file = os.path.join(target_path, 'Dataset_%s_%s.xlsx' % (label_type, attr_type))
                df.to_excel(xlsx_file)
            file_path = os.path.join(target_path, 'Dataset_%s_%s.jpg' % (label_type, attr_type))
            plt.savefig(file_path)
        print("그래프 생성 완료")