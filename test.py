#导入 requests模块
import requests
import json
import sys

Cookie = sys.argv[1]
CSRFToken = sys.argv[2]
start_time = sys.argv[3]
end_time = sys.argv[4]

#设置请求头,填写认证信息
headers = {
'Cookie': Cookie,
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
'X-CSRFToken': CSRFToken
}

r = requests.get('https://apm.cf.eu10.hana.ondemand.com/e/c1485af5-25bc-4773-a0e3-ca5a534dc784/rest/customfilters/customchartdata/f2272b97-6a2d-47b2-9460-ad5953bb7389?'
                 'tz=%2B00%3A00&gtf=c_' + start_time+ '_' + end_time + '&gf=all',headers=headers)
#转换json
jsonobj = json.loads(r.text)
#print(jsonobj)
state = jsonobj['customChartingTimeseries']['data']['builtin:host.cpu.usage|AVG|TOTAL|LINE|HOST']
#print(state)
#print(state.keys())
value_list= []
for key in state.keys():
    #print(state[key])
    for list in state[key]['dataPoints']:
        #print(list.get('value'))
        value = list.get('value')
        if value > 0:
            value_list.append(value)
#print(value_list)
sum = 0
for list in value_list:
    sum = sum+list
avg = sum/len(value_list)

print("the avg of Bizx app CPU usage is ",avg,"%")



'''
#获取当前编码 当前编码有utf-8 ISO-8859-1

print(r.encoding)
# 新建一个文件名 例如：TencentHtml 设置文件格式编码为 utf-8
# 注意文件格式的编码和 获取的编码 要一致，不然出现乱码问题


f = open("dynatrace.txt", "w",encoding="utf-8")
for i in r.text:
    #将数据写入文件
    f.write(i)
#关闭文件
f.close()
'''