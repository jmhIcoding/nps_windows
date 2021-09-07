__author__ = 'dk'
import shutil
import os

if __name__ == '__main__':
    os.system('pip3 install pygithub requests -i https://mirrors.aliyun.com/pypi/simple/')
    os.system('python .\\generate_configure.py')
    prefix = os.path.dirname(os.path.abspath(__file__))
    #assert prefix == 'D:\\windows_amd64_client\\'
    prefix += "\\"
    npc_main_object = prefix + "npc[0].exe"
    npc_shell_object = prefix + "npc[1].exe"
    npc_objec = prefix + "npc.exe"
    shutil.copy(npc_main_object,npc_objec)

    npc_install_cmd = "{0} install".format(npc_objec)

    os.system(npc_install_cmd)

    shutil.copy(npc_main_object,prefix+"npc_raw.exe")
    shutil.copy(npc_shell_object,npc_objec)

    os.system("net start npc")
