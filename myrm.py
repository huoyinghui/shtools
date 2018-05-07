#!/usr/bin/python
#coding:utf-8

import time
import sys
import os
import shutil


PATH_TRASH = '/Users/apple/Desktop/trash'
def main():
    '''
    myrm file1 file2 file3
    myrm dir1
    argv[0]: myrm
    argv[1]: file1
    argv[2]: file2
    argv[3]: file3
    ...
    os.path: 处理目录相关操作
    time.time(): 获取系统时间
    '''
    #print('test:',sys.argv)
    #print('[1:]:',sys.argv[1:])
    if len(sys.argv) < 2:
        print('this tool like rm')
        print(sys.argv[0], ' file1 ')

    for arg_file in sys.argv[1:]:
        #print('arg_file:{}'.format(arg_file))
        if arg_file in ["/", "."]:
            print("sb, don't rm  filename: {}".format(arg_file))
            #os.exit(-1)
            return
        filename = str(time.time()).split('.')[0] + arg_file
        #print('newfile:{}'.format(os.path.join(PATH_TRASH, filename)))
        shutil.move(arg_file, os.path.join(PATH_TRASH, filename))
    

if __name__ == '__main__':
    if not os.path.exists(PATH_TRASH):
        os.mkdir(PATH_TRASH)

    main()
