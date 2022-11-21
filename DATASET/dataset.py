import cv2
import time
import random
import os
import shutil
import glob
import math

def make_folder():

    patha = "./image"
    if not os.path.isdir(patha):
            os.mkdir(patha)

    pathb = "./train"
    if not os.path.isdir(pathb):
        os.mkdir(pathb)

    pathc = "./valid"
    if not os.path.isdir(pathc):
        os.mkdir(pathc)

def read_cam():
    
    cap = cv2.VideoCapture(cv2.CAP_DSHOW+0)
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    cap.set(28, 1)
    cap.set(cv2.CAP_PROP_EXPOSURE, -4.5)
    

    print("=============================================================")
    c = input("페트병 구분 입력[(입력시): BNP, SNP, BLP, SLP, NRP]: ")
    n = input("시료 넘버 입력(001~999): ")
    print("=============================================================")

    a = int(input("촬영할 이미지 갯수는? : "))
    for x in range(1, a+1):
    	ret, frame = cap.read()
    	cv2.imwrite(f'./image\\image{x}.jpg', frame)
    	#time.sleep(0.5)
    print(a, "장 촬영 완료")
    print("=============================================================")
    
    path = "./image"
    files = glob.glob(path + '/*')
    for f in files:
    	os.rename(f, os.path.join(path, n + c + os.path.basename(f)))
    cap.release()

    
    #random_image
    source = "./image"
    dest = "./train"

    b = a * 0.7
    no_of_files=int(b)
    bf = math.floor(b)

    for i in range(no_of_files):
    	random_file=random.choice(os.listdir(source))
    	source_file="%s/%s"%(source,random_file)
    	dest_file=dest
    	shutil.move(source_file,dest_file)
    	
    print(bf, "장 Training 폴더 이동 완료")
    
    source = "./image"
    dest = "./valid"

    c = a * 0.3
    no_of_files=int(c)
    cf = math.floor(c)
    
    for i in range(no_of_files):
    	random_file=random.choice(os.listdir(source))
    	source_file="%s/%s"%(source,random_file)
    	dest_file=dest
    	shutil.move(source_file,dest_file)
    	
    print(cf, "장 Validation 폴더 이동 완료")
    print("=============================================================")

    
def main():
    print("페트병 구분 \n BNP = big_nolabel_pets \n SNP = small_nolabel_pets \n BLP = big_label_pets \n SLP = small_label_pets \n NRP = no_recycle_pets")
    make_folder()
    print("분류 폴더 생성")
    read_cam()
    #random_image()

    while(1):
        print("촬영을 계속 하겠습니까? (Y or N): ", end='')
        answer = input()
        if answer == "y" or answer == "Y" or answer == 'o' or answer == 'O':
            read_cam()
            #random_image()

        elif answer == "n" or answer == "N" or answer == 'x' or answer == 'X':
            print("=============================================================")
            print("촬영 끝")
            time.sleep(3)
            break

    
if __name__ == '__main__':
    main()
