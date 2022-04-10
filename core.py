# -*- coding: utf-8 -*-
import os
import sys
from utils.msg_utils import sys_utils

sysUtils = sys_utils()
menu_list = []


def check_conf():
    global sysUtils

    # 检测系统环境是否为kali 如果不是则警告用户可能程序无法运行
    info = os.popen("uname -n").read()
    if info[:-1] != "kali":
        sysUtils.out_msg(msg="系统非kali 程序可能无法运行！", type="warn")

    # 检查运行环境 必须是root权限
    if os.getuid() != 0:
        sysUtils.out_msg(msg=f"You need to be root to run {sys.argv[0]}", type="warn")
        sys.exit(-1)


# 把exp目录下面的文件
def get_exp_to_cache():
    import configparser
    # 把该目录下的文件夹读取到缓存
    root_path = r'exp'
    global menu_list
    global sysUtils

    for dirpath, dirnames, filenames in os.walk(r'./exp'):
        # 获取每个菜单下的功能
        for dir in dirnames:
            # 找到目录下的所有文件
            script_dir = os.path.join(root_path, dir)
            for file in os.listdir(script_dir):
                # 先读配置文件
                if file[-3:] == "ini":
                    menu_item_list = {"item_info": [], "item_equipment_list": []}

                    config = configparser.ConfigParser()
                    config.read(os.path.join(script_dir, file))
                    base = config.items('base')
                    script_info = config.items('script_info')
                    script_path = config.items('script_path')
                    # 写了配置就读
                    if len(base) > 0:
                        item_info = {}
                        for key, value in base:
                            item_info[key] = value
                        menu_item_list["item_info"] = item_info
                        # 只检查有没有写脚本简介 因为根据约定写了配置简介那么就有配置文件路径
                        if len(script_info) > 0 :
                            scriptInfo = script_info[0][1].split(",")
                            scriptPath = script_path[0][1].split(",")
                            for index in range(0, len(scriptInfo)):
                                menu_item_list["item_equipment_list"].append({"name": scriptInfo[index], "path": scriptPath[index]})
                            menu_list.append(menu_item_list)
    sysUtils.out_msg(msg="插件加载完成！")


# 生成目录并运行程序
def running_tools():
    global menu_list
    global sysUtils
    sysUtils.out_msg(msg="启动前加载完毕！开始运行程序！")
    while True:
        print("~"*40)
        print("\tAre You Help ?\t".center(20, "~"))
        for index in range(len(menu_list)):
            base = menu_list[index]["item_info"]
            print(f'{index}.{base["name"]}\t\t\t【{base["desc"]} - {base["version"]}】')
        choice = input(">>q/d ")
        if choice == "q":
            sysUtils.out_msg(msg="退出程序")
            break
        # 选择具体服务
        item_menu = menu_list[int(choice)]["item_equipment_list"]
        # 打印二级目录
        while True:
            for index in range(len(item_menu)):
                print(f'【{index}】{item_menu[index]["name"]}')
            sec_choice = input(">>q/d ")
            if sec_choice == "q":
                sysUtils.out_msg(msg=f'返回一级目录')
                break
            script_path = item_menu[int(sec_choice)]["path"]
            os.system(f"python3 {script_path}")


if __name__ == '__main__':
    # 检查配置
    check_conf()
    # 读插件到内存
    get_exp_to_cache()
    # 生成插件目录
    running_tools()
