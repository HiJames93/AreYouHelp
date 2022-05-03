#!/usr/bin/python3
import os


def check_config(check_list):
    # 指定目录
    for key,val in check_list.items():
        res_count = 0
        resp = os.popen(val).read()[:-1]
        if resp != "":
            res_count = len(resp)
        if res_count == 0:
                print(f"没有配置【{key}】")


if __name__ == "__main__":
    root_path = input("请输入php安装目录:\n")
    if len(root_path) > 0:
        check_list = {
                "控制php脚本能访问的目录": f"cat {root_path}/cli/php.ini |grep '^open_basedir ='|grep -E '\/(\w+\/?)+'",
                "关闭危险函数": f"cat {root_path}/cli/php.ini |grep '^disable_functions =' |"+"awk -F '=' '{print $2}'",
                "关闭php版本信息在http头中的泄露": f"cat /{root_path}/cli/php.ini|grep '^expose_php = Off'",
                "SQL注入防护": f"cat /{root_path}/cli/php.ini|grep '^magic_quotes_gpc = on'",
                "错误信息控制": f"cat /{root_path}/cli/php.ini|grep '^display_errors = On'",
                "错误日志": f"cat /{root_path}/cli/php.ini|grep '^log_errors = On'"
        }
        check_config(check_list)
    else:
        print("参数不能为空！")
