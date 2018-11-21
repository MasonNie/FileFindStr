import os
import sys

def findStr(path,targets):
    dirlist = os.walk(path)
    output = open("E:/out46.txt",'w')
    for root,dir,files in dirlist:
        # if not os.path.isdir(path):
        #     return
        for file in files:
            #print(file)
            with open(os.path.join(root,file),'r') as fp:
                bigstr = fp.read()
                #print(file)
                for tar in targets:
                    if bigstr.find(tar)!= -1:
                        print(tar+"\t"+os.path.join(root,file))
                        print(tar + "\t" + os.path.join(root, file),file = output)
    output.close()




if __name__ == '__main__':
    def_dir = 'E:/temp\\'
    path = def_dir+'46\\smali'
    #path_in = sys[1]
    aim = {"getNetworkOperator","getDeviceId","getPhoneType"
        ,"getSubscriberId","getLine1Number","getCellLocation"
        ,"listen","getSimOperator","getRunningAppProcesses","getRunningTasks"
        ,"getInstalledPackages"}
    findStr(path,aim)


