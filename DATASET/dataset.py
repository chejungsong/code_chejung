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

    pathb_r = "./train/images"
    if not os.path.isdir(pathb_r):
        os.mkdir(pathb_r)

    pathc = "./valid"
    if not os.path.isdir(pathc):
        os.mkdir(pathc)

    pathc_r = "./valid/images"
    if not os.path.isdir(pathc_r):
        os.mkdir(pathc_r)

        
def delete_image_folder():
    filePath = "./image"
    fileExtension = '.jpg'
    print("이미지 파일 삭제")
    if os.path.exists(filePath):
        for file in os.scandir(filePath):
            if file.name.endswith(fileExtension):
                os.remove(file.path)
        return 'Remove File: ' + fileExtension 
    else:
        return 'Directory Not Found'
    print(removeExtensionFile('./image', '.jpg'))
    print("이미지 폴더 파일 삭제")

def read_cam():
    
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)
    
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
    #time.sleep(5)
    print("촬영 시작")
    #첫번째 파일이 문제가 생기니 첫번째 파일을 자동으로 삭제가 가능한가?
    for x in range(0, a+1):
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
    time.sleep(2)

    #여기서 파일 명 찾아서 삭제
    pick_files = ["image0"]
    org_directory_ = r"./image"

    org_directory = org_directory_.replace("\\", "/", 20)
    for i in range(0, len(pick_files)):
        FileList = os.listdir(org_directory)
        delete_num = [n for n in range(len(FileList)) if pick_files[i] in FileList[n]]
        for j in delete_num:
            os.remove("{}/{}".format(org_directory, FileList[j]))
    print("파일 삭제")
    time.sleep(2)

    
    #random_image
    source = "./image"
    dest = "./train\\images"

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
    dest = "./valid\\images"

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
    time.sleep(2)
    delete_image_folder()
    #random_image()

    while(1):
        print("촬영을 계속 하겠습니까? (Y or N): ", end='')
        answer = input()
        if answer == "y" or answer == "Y" or answer == 'o' or answer == 'O':
            time.sleep(5)
            read_cam()
            time.sleep(2)
            delete_image_folder()
            #random_image()

        elif answer == "n" or answer == "N" or answer == 'x' or answer == 'X':
            print("=============================================================")
            print("촬영 끝")
            time.sleep(3)
            break

    
if __name__ == '__main__':
    main()
