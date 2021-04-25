import os
import shutil
import time
import sys

time_now = time.strftime("%Y%m%d", time.localtime())
path = "D:"+'\send\k1297\中国民生银行股份有限公司\\'+time_now

def copy_and_rename(fpath_input, fpath_output):
    for file in os.listdir(fpath_input):
        #if os.path.splitext(file)[1] == ".jpg":
        oldname = os.path.join(fpath_input, file)
        newname_1 = os.path.join(fpath_output,
                                 os.path.splitext(file)[0] + ".ok")
        #os.rename(oldname, newname)
        shutil.copyfile(oldname, newname_1)

if __name__ == '__main__':
    print('start ...')
    t1 = time.time() * 1000
    #time.sleep(1) #1s
    fpath_input = path
    fpath_output = path
    copy_and_rename(fpath_input, fpath_output)
    t2 = time.time() * 1000
    print('take time:' + str(t2 - t1) + 'ms')
    print('end.')