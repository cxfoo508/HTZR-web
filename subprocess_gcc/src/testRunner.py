import os
import subprocess
from lib.fileUtil import FileWrite

# 获取当前工作目录绝对路径
dir_path = os.getcwd()
# 获取当前py代码文件目录的绝对路径
# os.path.dirname(os.path.abspath(__file__))

def CompileProject(dir_name: str):
    destPath = os.path.join(dir_path,dir_name)
    os.chdir(destPath)
    #mingw32-make.exe
    ret = subprocess.run(["gcc", "-o", "maintest.exe", "maintest.c"], shell=False, capture_output=True)
    #print(ret)
    FileWrite(destPath+"/compile.log", "returncode: {}\nstdout: {}\nstderr: {}\n".format(ret.returncode, ret.stdout, ret.stderr))
    os.chdir(dir_path)

def RunProject(dir_name: str):
    destPath = os.path.join(dir_path,dir_name)
    os.chdir(destPath)
    try:
        ret = subprocess.run([".\maintest.exe"], shell=False, capture_output=True)
        FileWrite(destPath+"/run.log", "returncode: {}\nstdout: {}\nstderr: {}\n".format(ret.returncode, ret.stdout, ret.stderr))
    except Exception as e:
        FileWrite(destPath+"/run.log", "FileNotFoundError! 请检查是否编译成功")

    #print(ret)
    os.chdir(dir_path)

if __name__ == '__main__':
    CompileProject("rsc/c_proj_demo")
    RunProject("rsc/c_proj_demo")