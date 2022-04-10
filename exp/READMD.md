# 前言
这是框架的内核，一个中间调度框架。用于整合这些工具，对于系统工程师来说工具的意义相当于第三只手，但是谁能说清我们到底需要多少功能呢？

# 插件添加规范
1. 在exp目录下新建插件目录
2. 在新建的插件目录下放置插件的执行程序
3. 在新建的插件目录下填写好配置文件exp.ini

# 框架结构
1. 加载目录：
```text
menu_list:
    menu_item1:
        item_info_list: 功能菜单简介和配置
        item_equipment_list: 脚本列表
            name1 path1
            name2 path2
            name3 path3
            name4 path4
            ...
    menu_item2
    menu_item3
    menu_item4
    ...
```
2. 配置文件Demo:
```ini
[base]
name=插件目录标题
desc=插件目录简介
version=插件目录版本

[script_info]
desc=文件简介1,文件简介2

[script_path]
path_list=文件路径1,文件路径2

```
