## parsing data for deeplearning


original data form



1. xml to text


---------------------------------------------------------------------------------------------------------------------------
코드 내용
1. dataRead_makeText.py는 target_path 내부의 xml 파일의 정보를 파싱하여  car, person의 w,h w*h 에 따른 값들을 text형태로 저장한다.

2. textRead_makeGraph는 text 형태로 저장된 데이터를 읽어 크기별 갯수를 정렬하여 xlsx형태로 저장하고 bar graph를 저장한다.

3. whole_dataRead_makeText는 전체 데이터셋이 있는 리렉토리에 하위 폴더까지 검색하여 xml 파일을 txt 형태로 저장한다

4. whole_textRead_makeGraph는 wholedataRead에서 저장한 txt파일을 열고 크기별로 갯수를 정렬하여 xlsx 형태로 저장하고  bar graph를 저장한다.

**data 형태는 반드시 object와 xmin xmax 가 있는 xml로 사용해야한다


코드활용
1. dataRead_makeText.py 파일의 58번째 줄에 target_path를 개별 xml 경로에 맞게 수정하고 run 한다. 결과물로 car_w, car_h, car_area, person_w, person_h, person_area와 output txt파일들이 폴더 내부에 저장된다.

2. textRead_makeGraph파일의 65번째 줄에 있는 target_path를  생성된 txt이 있는 경로에 맞게 수정하고 run 한다. 결과물로
객체 크기별로 갯수 정렬하여 car_w, car_h, car_area, person_w, person_h, person_area의  xlsx 파일과 그래프가 폴더 내부에 저장된다. 

3. whole_dataRead_makeText의 59, 60번째줄 target_path와 root_path를 전체 데이터셋이 있는 폴더위치로 수정한후 run 한다. 전체 데이터셋에 대한 car_w, car_h, car_area, person_w, person_h, person_area와 output 텍스트 파일을 저장한다.
(전체데이터라서 시간이 오래걸린다)

4.whole_textRead_makeGraph의 65와 66번쨰줄의 target_path와 root_path를 데이터셋 전체에 대한 txt가 있는 디렉토리로 수정하고 run 한다. 전체 데이터셋을 크기별 갯수를 정렬하여 xlsxs과 그래프를 폴더 내부에 저장한다.(전체데이터라서 시간이 오래걸린다)


