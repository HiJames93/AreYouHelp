# -*- coding: utf-8 -*-
import os


# 是否存在空口令账号
def hasPwd():
    cmd = "cat /etc/shadow | awk -F: '$2 == \"\"'"
    resp_info = os.popen(cmd).readline()
    flag = False
    if len(resp_info) == 0:
        flag = True
    out_msg = "存在空口令账号？"
    print(f"{out_msg} 否" if flag is True else f"{out_msg} 是")


# 检查口令过期前警告天数
def has_wdbpe():
    resp_info = os.popen("cat /etc/login.defs | grep '^PASS_WARN_AGE'").readline()
    flag = False
    if len(resp_info) > 0:
        date_score = resp_info.split()[1]
        flag = int(date_score) >= 30
    out_msg = "口令过期前警告天数"
    print(f"{out_msg}符合标准" if flag is True else f"{out_msg}不符合标准")


# 检查口令最小长度
def pwd_len():
    resp_info = os.popen("cat /etc/login.defs | grep '^PASS_MAX_LEN'").readline()
    flag = False
    if len(resp_info) > 0:
        date_score = resp_info.split()[1]
        flag = int(date_score) >= 8
    out_msg = "口令最小长度"
    print(f"{out_msg}符合标准" if flag is True else f"{out_msg}不符合标准")


# 检查口令生存周期
def pwd_lifetime():
    resp_info = os.popen("cat /etc/login.defs | grep '^PASS_MAX_DAYS'").readline()
    date_score = resp_info.split()[1]
    flag = int(date_score) <= 90
    out_msg = "口令生存周期"
    print(f"{out_msg}符合标准" if flag is True else f"{out_msg}口令生存周期不符合标准")


# 检查是否设置除root之外UID为0的用户
def like_root_user():
    cmd = "cat /etc/passwd | awk -F: '($3 == 0){print $1 }'|grep -v root"
    resp_info = os.popen(cmd).readline()
    flag = True
    if len(resp_info) > 0:
        flag = False
    out_msg = "除root之外UID为0的用户"
    print(f"{out_msg} 不存在" if flag is True else f"{out_msg} 存在：{resp_info}")


if __name__ == '__main__':
    # 检查口令生存周期
    pwd_lifetime()
    # 检查口令最小长度
    pwd_len()
    # 检查口令过期前警告天数
    has_wdbpe()
    # 检查是否存在空用户
    hasPwd()
    # 检查是否设置除root之外UID为0的用户
    like_root_user()
