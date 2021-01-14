import os
import sys
import os.path
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import MD5
import shutil
from shutil import copy



#实现加密
def encryptFile(fileDir,pdw):
    filepaths=[]
    for filename in os.listdir(fileDir):
        filepaths.append(fileDir+'/'+filename)
    for filepath in filepaths:
        with open(filepath,'rb') as f:
            with open((os.path.splitext(filepath)[0]+".crp"), 'wb') as fw:
                fw.write(AES.new(b'Sixteen byte key', AES.MODE_CFB, password).encrypt(f.read()))




# 实现分组存储
def copyFile(fileDir,saveDir,group):
    for root, dirs, files in os.walk(fileDir):
        filenum = len(files)
        print(filenum)
        imgnum = int(filenum / group)
        print(imgnum)
        for i in range(group):
            for j in range(i,filenum,group):
                newSave_Dir = saveDir + '/' + 'result' + str(i)
                if not os.path.exists(newSave_Dir):
                    os.mkdir(newSave_Dir)
                new_file_path = newSave_Dir + "/" + files[j]
                if ((files[i][-3:]).lower() in ['jpg', 'png', 'bmp', 'jpeg','crp']):
                    file_path = fileDir + '/' + files[j]
                    shutil.copy(file_path, new_file_path)




if __name__ == '__main__':
    fileDir = "G:/TrainProject/img"  # 源图片文件夹路径
    saveDir = "G:/TrainProject/result"  # 保存图片
    group = 2
    pwd = input("Password:")
    passwordGen = MD5.new()
    passwordGen.digest_size = 16
    passwordGen.update(pwd.encode('utf-8'))
    password = passwordGen.digest()
    encryptFile(fileDir, pwd)
    copyFile(fileDir, saveDir,group)


