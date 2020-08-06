# by xianqiang.li@sap.com
import requests
import json
import sys

from config import *
from method import *


Cookie = sys.argv[1]
CSRFToken = sys.argv[2]
start_time = sys.argv[3]
end_time = sys.argv[4]

'''
Cookie = 'apmroute=2dabbf26d2f34e9b33de720f7030dda8; apmsessionid=node0trz5heiufssn12u2p633tabr3472509.node0'
CSRFToken = '7d36e420-cf32-4ec5-8a96-f720dfce5df8|3|c1a7b26a-a2ca-11e7-9c34-02a366d33462'
start_time = '1596098929359'
end_time = '1596106769321'
'''
#add header
headers = {
'Cookie': Cookie,
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
'X-CSRFToken': CSRFToken
}


#BizxApp
r2 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + BizxAppID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)
json2 = json.loads(r2.text)
BizxCpu = getBizxCpu(json2)

#DB
r1 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + DbID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json1 = json.loads(r1.text)
DBcpu = getDBCpu(json1)

#OEM cpu
r3 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + OemAppID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json3 = json.loads(r3.text)
OemCpu = getOemCpu(json3)

#OEM Mem
r4 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + OemMemID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json4 = json.loads(r4.text)
OemMem = getOemMem(json4)

#Bizx Mem
r5 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + BizxMemID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json5 = json.loads(r5.text)
BizxMem = getBizxMem(json5)

#Oem GC
r6 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + OemGcID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json6 = json.loads(r6.text)
OemGC = getOemGC(json6)

#Bizx GC
r7 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + BizxGcID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json7 = json.loads(r7.text)
BizxGC = getBizxGC(json7)

#BizxTomcatThreads
r8 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + BizxTomcatThreadsID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json8 = json.loads(r8.text)
BizxTomcatThreads = getBizxTomcatThreads(json8)

#OemTomcatThreads
r9 = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/'
                 + OemTomcatThreadsID +
                 '?tz=%2B00%3A00&gtf=c_' + start_time + '_' + end_time + '&gf=all',headers=headers)

json9 = json.loads(r9.text)
OemTomcatThreads = getOemTomcatThreads(json9)



print("the avg of Bizx app CPU usage is ",round(BizxCpu,2),"%")
print("the avg of OEM app CPU usage is ", round(OemCpu,2), "%")

print("the avg of DB master node CPU usage is ", round(DBcpu[0],2), "%")
print("the avg of DB slave node CPU usage is ", round(DBcpu[1],2), "%")

print("the avg of OEM MEM usage is ", round(OemMem,2), "GB")

print("the avg of Bizx MEM usage is ", round(BizxMem,2) , "GB")

print("the avg of OEM GC Suspention is ", round(OemGC,2), "%")

print("the avg of OEM GC Suspention is ", round(BizxGC, 2), "%")

print("the avg of Bizx tomcat threads is ", round(BizxTomcatThreads, 2))

print("the avg of OEM tomcat threads is ", round(OemTomcatThreads, 2))


