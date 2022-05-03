#!/usr/bin/python3
import os
import pysnooper


#@pysnooper.snoop()
def check_os():
    os_list = ["debian","centos"]
    result = os.popen("uname -a").read()[:-1]
    result = str(result).lower()
    for os_name in os_list:
        if os_name in result:
            return os_name

def check_setup_status(os_name):
    flag = False
    soft_manager_list = [{"debian":"apt list --installed |grep docker |wc -l"},{"centos":"rpm -q "}]
    for soft in soft_manager_list:
        for key,value in soft.items():
            if key == os_name:
                if int(os.popen(value).read()[:-1]) > 0:
                    flag = True
    return flag


# 检查是否有脆弱项配置
def has_safe_config(os_name):
    open_log_status = os.popen("cat /etc/docker/daemon.json |grep '\"log-level\": \"debug\"' |echo $?").read()[:-1]
    if int(open_log_status) == 0:
        print("未开启docker日志！")
    # 检查特定版本配置
    os.system("bash docker-bench-security.sh")


if __name__ == "__main__":
    # 获取系统型号
    os_name = check_os()
    # 检查是否安装
    flag = check_setup_status(os_name)
    if flag is False:
        print("没找到docker！请安装后再使用本程序！")
    else:
        # 脆弱项检查
        has_safe_config("")
