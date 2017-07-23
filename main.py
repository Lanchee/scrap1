#coding=utf-8

from interface import interface1, interface2
from datatype import datatype1

if __name__=='__main__':
    ipaddr = interface1.Get_IPinfo("www.baidu.com", datatype1.NSLOOKUP_TIMEOUT)
    info = "---------------------------------------\nScanning " + str(ipaddr)
    interface2.write_log(datatype1.INTERFACE_LOG, info)
    interface1.IP_port(ipaddr)

