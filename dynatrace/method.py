#导入 requests模块
import requests
import json
import sys

def getBizxCpu(json):

    state = json['customChartingTimeseries']['data']['builtin:host.cpu.usage|AVG|TOTAL|LINE|HOST']
    # print(state)
    # print(state.keys())
    value_list = []
    for key in state.keys():
        # print(state[key])
        for list in state[key]['dataPoints']:
            # print(list.get('value'))
            value = list.get('value')
            if value > 0:
                value_list.append(value)
    # print(value_list)
    sum = 0
    for list in value_list:
        sum = sum + list
    avg = sum / len(value_list)
    return avg

def getDBCpu(json):
    state = json['customChartingList']['items']['HOST']
    # print(state)
    # print(state.keys())
    value_list = []
    for host in state:
        # print(host['name'])
        if host['name'] == 'qa13hanac02n31.lab.od.sap.biz':
            MasterCpu = host['customChartingTimeseriesColumnValues']['data'][
                'builtin:host.cpu.usage|AVG|TOTAL|LINE|HOST']
            value_list.append(MasterCpu)
        elif host['name'] == 'qa13hanac02n32.lab.od.sap.biz':
            SlaveCpu = host['customChartingTimeseriesColumnValues']['data'][
                'builtin:host.cpu.usage|AVG|TOTAL|LINE|HOST']
            value_list.append(SlaveCpu)
        else:
            print("pleae have a manual check on dynatrace")
    return value_list

def getOemCpu(json):
    state = json['customChartingList']['items']['HOST']
    # print(state)
    # print(state.keys())
    value_list = []
    for host in state:
        # print(host['name'])
        value = host['customChartingTimeseriesColumnValues']['data']['builtin:host.cpu.usage|AVG|TOTAL|LINE|HOST']
        value_list.append(value)
    sum = 0
    for list in value_list:
        sum = sum + list
    avg = sum / len(value_list)
    return avg

def getOemMem(json):
    state = json['customChartingList']['items']['PROCESS_GROUP_INSTANCE']
    # print(state)
    # print(state.keys())
    value_list = []
    for host in state:
        # print(host['name'])
        value = host['customChartingTimeseriesColumnValues']['data'][
            'builtin:tech.jvm.memory.pool.used|AVG|TOTAL|LINE|PROCESS_GROUP_INSTANCE']
        # print(value/1024/1024/1024)
        value_list.append(value)

    sum = 0
    for list in value_list:
        sum = sum + list
    avg = sum * 2 / len(value_list)/1024/1024/1024
    return avg
def getBizxMem(json):
    state = json['customChartingList']['items']['PROCESS_GROUP_INSTANCE']
    # print(state)
    # print(state.keys())
    value_list = []
    for host in state:
        # print(host['name'])
        value = host['customChartingTimeseriesColumnValues']['data'][
            'builtin:tech.jvm.memory.pool.used|AVG|TOTAL|LINE|PROCESS_GROUP_INSTANCE']
        # print(value/1024/1024/1024)
        value_list.append(value)

    sum = 0
    for list in value_list:
        sum = sum + list
    avg = sum / len(value_list)/1024/1024/1024
    return avg
def getOemGC(json):
    state = json['customChartingList']['items']['PROCESS_GROUP_INSTANCE']
    # print(state)
    # print(state.keys())
    value_list = []
    for host in state:
        # print(host['name'])
        value = host['customChartingTimeseriesColumnValues']['data'][
            'builtin:tech.jvm.memory.gc.suspensionTime|AVG|TOTAL|AREA|PROCESS_GROUP_INSTANCE']
        value_list.append(value)

    sum = 0
    for list in value_list:
        sum = sum + list
    avg = sum / len(value_list)
    return avg
def getBizxGC(json):
    state = json['customChartingList']['items']['PROCESS_GROUP_INSTANCE']
    # print(state)
    # print(state.keys())
    value_list = []
    for host in state:
        # print(host['name'])
        value = host['customChartingTimeseriesColumnValues']['data'][
            'builtin:tech.jvm.memory.gc.suspensionTime|AVG|TOTAL|LINE|PROCESS_GROUP_INSTANCE']
        # print(value/1024/1024/1024)
        value_list.append(value)

    sum = 0
    for list in value_list:
        sum = sum + list
    avg = sum / len(value_list)
    return avg








