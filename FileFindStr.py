import os
import sys

def findStr(path,targets):
    dirlist = os.walk(path)
    output = open("E:/out46.txt",'w') #输出结果文件
    for root,dir,files in dirlist:  #遍历文件夹
        if not os.path.isdir(path): #如果本是文件直接结束
            return
        for file in files:
            #print(file)
            with open(os.path.join(root,file),'r') as fp: #读取文件内容
                bigstr = fp.read()
                #print(file)
                for tar in targets: #查找匹配项
                    if bigstr.find(tar)!= -1:
                        print(tar+"\t"+os.path.join(root,file))
                        print(tar + "\t" + os.path.join(root, file),file = output)
    output.close()




if __name__ == '__main__':
    def_dir = 'E:/temp\\'
    path = def_dir+'46\\smali'  #文件路径
    #path_in = sys[1]
    aim = {"getNetworkOperator","getDeviceId","getPhoneType"
        ,"getSubscriberId","getLine1Number","getCellLocation"
        ,"listen","getSimOperator","getRunningAppProcesses","getRunningTasks"
        ,"getInstalledPackages"}  #敏感API标识数组
    findStr(path,aim)


