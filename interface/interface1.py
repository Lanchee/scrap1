# coding=utf-8
import socket
import time
import _thread
import subprocess
import re
from datatype import datatype1
from interface import interface2

socket.setdefaulttimeout(3) #设置全局超时时间为3S

def scaf_port(ipaddr, portid):
    '''
    扫描指定IP地址的端口
    :param ipaddr: IP地址
    :param portid: 端口号
    :return:
    '''
    try:
        if portid > 65535 or portid < 0:
            print("Portid is to big, portid=%d"% portid)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connet_ex(ipaddr, portid)
        if result == 0:
            interface2.write_log(datatype1.INTERFACE_LOG,
                                 " Scanning " + str(ipaddr) + ":" + str(portid) + " success!")
        else:
            interface2.write_log(datatype1.INTERFACE_LOG,
                                 " Scanning " + str(ipaddr) + ":" + str(portid) + " failed!")
        sock.close()
    except:
        interface2.write_log(datatype1.INTERFACE_LOG,
                             " Scanning " + str(ipaddr) + ":" + str(portid) + " error!")

def IP_port(ipaddr):
    '''
    获得ip开放端口列表
    :param ipaddr: 网站IP地址
    :return:
    '''
    try:
        t = time.time()
        for portid in range(0, datatype1.MAX_PORT):
            _thread.start_new_thread(scaf_port, (ipaddr, int(portid)))
            time.sleep(0.003) #确保先运行socket中的方法
    except:
        print("Get Error")


def Get_IPinfo(web, timeout):
    '''
    获得网站服务器ip地址
    :param web: 网站域名
    :param timeout: nslookup命令延时
    :return: 返回IP地址string
    '''
    cmd = ['nslookup', web]
    try:
        std = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)
        t_beginning = time.time()
        seconds_pass = 0
        while True:
            if subprocess.Popen.poll(std) is not None:
                break
            if timeout and seconds_pass > timeout:
                std.terminate()
                raise TimeoutError(cmd, timeout)
            time.sleep(0.5)
            seconds_pass = time.time() - t_beginning

        outinfo = subprocess.Popen.communicate(std)
        p = re.compile(r'.*Address:\s+(\d+\.\d+\.\d+\.\d+).*')
        m = p.match(str(outinfo[0]))
        ipaddr = m.group(1)
        return ipaddr
    except:
        raise TimeoutError(cmd, timeout)
