import os
import platform
import re


# 检查数据库放在系统分区
def check_data_path(username, password):
    # 不要将数据库放在系统分区
    data_path = ""
    if mysql_pwd == "":
        data_path = os.popen(
            f"mysql -u{username} -e \"show variables where variable_name = 'datadir'\"" + " |awk 'NR==2''{print $2}'").read()[
                    :-1]
    else:
        data_path = os.popen(
            f"mysql -u{username} -p{password} -e \"show variables where variable_name = 'datadir'\"" + " |awk 'NR==2''{print $2}'").read()[
                    :-1]
    root_path = data_path
    if len(root_path) > 0:
        if re.findall("/|/usr|/var", root_path):
            print("不要将数据库放在系统分区!!")


def check_other_config():
    global mysql_user, mysql_pwd
    cmd_list = {
        "请使用专用的最小权限账号运行mysql数据库进程!!": "ps -ef | grep mysql |grep -v 'auto mysql'|grep root",
                "未禁用mysql命令行历史记录": "find / -name \".mysql_history\"",
        "确保MYSQL_PWD环境变量未设置敏感信息":"grep MYSQL_PWD /proc/*/environ",
        "未控制数据目录的访问权限": f"dataval=`mysql -u{mysql_user} -e 'show variables where variable_name = \"datadir\"'"+"|awk 'NR==2{print $2}'"+"` && ls -l $dataval | egrep \"^d[r|w|x]{3}------\s*.\s*mysql\s*mysql\s*\d*.*mysql\"" if mysql_pwd == "" else f"dataval=`mysql -u{mysql_user} -p{mysql_pwd} -e 'show variables where variable_name = \"datadir\"'"+"|awk 'NR==2{print $2}'"+"` && ls -l $dataval | egrep \"^d[r|w|x]{3}------\s*.\s*mysql\s*mysql\s*\d*.*mysql\"",
        "未控制二进制日志文件的权限": f"dataval=`mysql -u{mysql_user} -e \"show variables like 'log_bin_basename'\"`"+"|awk 'NR==2{print $2}'"+" &&ls -l $dataval | egrep \"^-[r|w]{2}-[r|w]{2}----\s*.*$\"" if mysql_pwd == "" else f"dataval=`mysql -u{mysql_user} -p{mysql_pwd} -e \"show variables like 'log_bin_basename'\" +"+"|awk 'NR==2{print $2}'"+"+` &&ls -l $dataval | egrep \"^-[r|w]{2}-[r|w]{2}----\s*.*$\"",
        "未删除test数据库": f"mysql -u{mysql_user} -e \"show databases\"|grep test" if mysql_pwd == "" else f"mysql -u{mysql_user} -p{mysql_pwd} -e \"show databases\"|grep test",
        "请确保读取本地文件的参数设置为失效": f"mysql -u{mysql_user} -e \"SHOW VARIABLES WHERE Variable_name = 'local_infile'\""+"|awk 'NR==2{print $2}'|grep ON" if mysql_pwd == "" else f"mysql -u{mysql_user} -p{mysql_pwd} -e \"SHOW VARIABLES WHERE Variable_name = 'local_infile'\""+"|awk 'NR==2{print $2}'|grep ON",
        "请确保日志存放在非系统区域": f"mysql -u{mysql_user} -e \"SELECT @@global.log_bin_basename\""+"|awk 'NR==2{print $2}'|grep -v NULL" if mysql_pwd == "" else f"mysql -u{mysql_user} -p{mysql_pwd} -e \"SELECT @@global.log_bin_basename\""+"|awk 'NR==2{print $2}'|grep -v NULL",
    }
    for key, val in cmd_list.items():
        resp = os.popen(val).read()
        if len(resp) > 0:
            print(key)


# 获取操作系统类型
def sys_info():
    return platform.system()


if __name__ == '__main__':
    mysql_user = "root"
    mysql_pwd = ""
    check_data_path(mysql_user, mysql_pwd)
    check_other_config()