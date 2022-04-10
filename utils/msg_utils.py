# -*- coding: utf-8 -*-
import logging


class sys_utils:

    def __init__(self, log_filename="../core/dev_ops.log"):
        # Define a Handler and set a format which output to file
        logging.basicConfig(
            level=logging.DEBUG,  # 定义输出到文件的log级别，
            format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
            datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
            filename=log_filename,  # log文件名
            filemode='w')  # 写入模式“w”或“a”
        # Define a Handler and set a format which output to console
        console = logging.StreamHandler()  # 定义console handler
        console.setLevel(logging.INFO)  # 定义该handler级别
        formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
        console.setFormatter(formatter)
        # Create an instance
        logging.getLogger().addHandler(console)  # 实例化添加handler

    def out_msg(self, msg, type="info"):
        if type == "debug":
            logging.debug(msg)
        elif type == "info":
            logging.info(msg)
        elif type == "warn":
            logging.warning(msg)
        elif type == "err":
            logging.error(msg)
        elif type == "critical":
            logging.critical(msg)