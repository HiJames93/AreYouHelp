# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    host_list = input("请输入主机：").split(",")
    for host in host_list:
        cmd = f"nmap -sS {host} | awk 'NR>4'|grep -v 'Nmap done*'"
        scanner_resp = os.popen(cmd).readlines()[1:]
        if len(scanner_resp) > 0:
            print(f"主机：{host}，发现如下端口暴露")
            for info in scanner_resp:
                info2 = info[:-1]
                if info == "":
                    continue
                print(info2)
        else:
            print(f"主机：{host}，没有发现任何端口")