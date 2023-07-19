#!/usr/bin/python3


# coding=utf-8
"""
filename:snmp_test.py

說明：
使用系統的 snmpwalk 來查詢裝置資訊，需要先安裝 snmp
程式碼 Windows 和 Linux 通用

Windows cmd 呼叫示例：snmpwalk -v 2c -c public 127.0.0.1 1.3.6.1.2.1.1.1

Windows cmd 下檢視某主機（192.168.132.130）資訊示例：
snmpwalk -v 2c -c public 192.168.132.130 1.3.6.1.2.1.1.1
"""

import re
import os
import time
import platform

if 'Linux' == platform.system():
    hosts = ['192.168.1.18']
else:
    # 在虛擬機器執行時則檢視本地
    hosts = ['127.0.0.1']

def snmpWalk(host, oid):
    result = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
    return result

# ------------------------------------------------------------
# 獲取負載資訊
# ------------------------------------------------------------


def getSystem(host):
    system = ':'.join(snmpWalk(host, 'system')[0].split(':')[3:]).strip()
    return system

# ------------------------------------------------------------

# ------------------------------------------------------------
# 獲取負載資訊
# ------------------------------------------------------------


def getLoad(host, loid):
    """系統負載"""
    load_oids = '1.3.6.1.4.1.2021.10.1.3.' + str(loid)
    return snmpWalk(host, load_oids)[0].split(':')[3]


def getLoads(host):
    load1 = getLoad(host, 1)
    load10 = getLoad(host, 2)
    load15 = getLoad(host, 3)
    return load1, load10, load15

# ------------------------------------------------------------

# ------------------------------------------------------------
# 獲取網絡卡流量
# ------------------------------------------------------------


def getNetworkDevices(host):
    """獲取網路裝置資訊"""
    device_mib = snmpWalk(host, 'RFC1213-MIB::ifDescr')
    device_list = []
    for item in device_mib:
        device_list.append(item.split(':')[3].strip())
    return device_list


def getNetworkData(host, oid):
    """獲取網路流量"""
    data_mib = snmpWalk(host, oid)
    data = []
    for item in data_mib:
        byte = float(item.split(':')[3].strip())
        data.append(str(round(byte / 1024, 2)) + ' KB')
    return data


def getNetworkInfo(host):
    device_list = getNetworkDevices(host)
    # 流入流量
    inside = getNetworkData(host, 'IF-MIB::ifInOctets')
    # 流出流量
    outside = getNetworkData(host, 'IF-MIB::ifOutOctets')
    return device_list, inside, outside

# ------------------------------------------------------------


# ------------------------------------------------------------
# 記憶體使用率
# ------------------------------------------------------------

def getSwapTotal(host):
    swap_total = snmpWalk(host, 'UCD-SNMP-MIB::memTotalSwap.0')[0].split(' ')[3]
    return swap_total


def getSwapUsed(host):
    swap_avail = snmpWalk(host, 'UCD-SNMP-MIB::memAvailSwap.0')[0].split(' ')[3]
    swap_total = getSwapTotal(host)
    swap_used = str(round(((float(swap_total) - float(swap_avail)) / float(swap_total)) * 100, 2)) + '%'
    return swap_used


def getMemTotal(host):
    mem_total = snmpWalk(host, 'UCD-SNMP-MIB::memTotalReal.0')[0].split(' ')[3]
    return mem_total


def getMemUsed(host):
    mem_total = getMemTotal(host)
    mem_avail = snmpWalk(host, 'UCD-SNMP-MIB::memAvailReal.0')[0].split(' ')[3]
    mem_used = str(round(((float(mem_total) - float(mem_avail)) / float(mem_total)) * 100, 2)) + '%'
    return mem_used


def getMemInfo(host):
    mem_used = getMemUsed(host)
    swap_used = getSwapUsed(host)
    return mem_used, swap_used

# ------------------------------------------------------------

def main():
    for host in hosts:

        print('=' * 10 + host + '=' * 10)
        start = time.time()
        #print("系統資訊")
        #system = getSystem(host)
        #print(system)

        print("系統負載")
        load1, load10, load15 = getLoads(host)
        print('load(5min): %s ,load(10min): %s ,load(15min): %s' % (load1, load10, load15))

        print("網絡卡流量")
        device_list, inside, outside = getNetworkInfo(host)
        for i, item in enumerate(device_list):
            print('%s : RX: %-15s   TX: %s ' % (device_list[i], inside[i], outside[i]))

        mem_used, swap_used = getMemInfo(host)
        print("記憶體使用率")
        print('Mem_Used = %-15s   Swap_Used = %-15s' % (mem_used, swap_used))

        end = time.time()
        print('run time:', round(end - start, 2), 's')

if __name__ == '__main__':
    main()

    
