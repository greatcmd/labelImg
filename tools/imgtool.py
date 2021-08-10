# -*- coding:utf-8 -*-
import os
import os.path
import cv2
import hashlib
from tqdm import tqdm

def convertImageToJpg(rootdir):
    '''
    1.遍历文件夹中非空的文件  2.修改文件名字  3.统计文件内同行数  4.记录信息到文件中
    :param rootdir: 文件根目录
    :return: 
    '''
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        print ("parent is "+parent)
        print('count of files:',len(filenames))
        for filename in tqdm(filenames):
            imgname = ''
            if ('.jpeg' in filename or '.png' in filename or '.jfif' in filename ):
                imgname = os.path.join(parent,filename)
            if imgname :
                print('read:' + imgname)
                imgf = cv2.imread(imgname)    
                # new image name
                nimgname = os.path.join(parent+'\\tst\\',hashlib.md5(filename.encode()).hexdigest() + '.jpg')
                cv2.imwrite(nimgname,imgf)
                print("save image: " + nimgname)
                os.remove(imgname)
                print("delete image: " + imgname)
            #if filename == '20170317.ind':
            #    os.rename(os.path.join(parent, filename), os.path.join(parent, "20170320.ind"))
    #f.close()


def renameImagefile(rootdir):
    '''
    1.遍历文件夹中非空的文件  2.修改文件名字  3.统计文件内同行数  4.记录信息到文件中
    :param rootdir: 文件根目录
    :return: 
    '''
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        print ("parent is "+parent)
        #print(filenames)
        for filename in filenames:
            imgname = os.path.join(parent,filename)
            if imgname :
                print('read:' + imgname)
                imgf = cv2.imread(imgname)    
                # new image name
                nimgname = os.path.join(parent+'\\tst\\',hashlib.md5(filename.encode()).hexdigest() + '.jpg')
                cv2.imwrite(nimgname,imgf)
                print("save image: " + nimgname)
                os.remove(imgname)
                print("delete image: " + imgname)
            #if filename == '20170317.ind':
            #    os.rename(os.path.join(parent, filename), os.path.join(parent, "20170320.ind"))
    #f.close()

if __name__ == '__main__':
    convertImageToJpg('C:\\Users\\jason\\Desktop\\temp\\yoloTools\\MLPic\\helmet\\imageSet\\')