# coding=utf-8
import  csv
import xlrd
import  csv
from kscore.session import get_session
# 读取非表头数据，以每行为一个数组元素返回一个数组
def read_xlrd(excelFile,tableName):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_name(tableName)
    dataFile = []
    # print(table.nrows)
    for rowNum in range(table.nrows):
        # 去掉表头
        if rowNum > 0 :  # =0 时 为表头
            dataFile.append(table.row_values(rowNum))
    return  dataFile

# 数据加工： 输入 ServerName Port Ip  输出： ServerName Port [ip1,ip2]
def dataFileProces(dataFile):
    dataProces = []
    serverData = dataFile
    # 对项目去重存放至dataProces
    for sNume in range(len(serverData)):
        if str(dataProces).find(serverData[sNume][0]) != -1:
            pass
        else:
            # 如果项目不在dataProces 写入
            dataProces.append(serverData[sNume])
    # 端口转换成正整型， ip 转换成列表
    for i in range(len(dataProces)):
        dataProces[i][2] = [dataProces[i][2]]
        dataProces[i][1] = int(dataProces[i][1])
    # print(dataProces)
    for i in range(len(serverData)):
        for t in range (len(dataProces)):
            if serverData[i][0] == dataProces[t][0] and serverData[i][1] == dataProces[t][1] and serverData[i][2] != dataProces[t][2]:
                    # pass
                    dataProces[t][2].append(serverData[i][2])
            else:
                pass
    return dataProces

if __name__ == '__main__':
    # a = read_xlrd('lb.xls','kong')
    # slbClient = CrcateSlbClient()
    # # 2 创建负载均衡实例
    # LoadBalancerID = CreateSlbBalancer(slbClient,'qwecheck-test1')
    # # 3 创建监听
    # ListenerId = CreateSlbListener(slbClient,LoadBalancerID,'LName9040',9040)
    # # 4 挂载实例
    # cswl = CreateSlbWithListener(slbClient,ListenerId,'10.1.0.79',9898)

    # 创建两个LB，读取的额表中已经区分端口不同，程序不做判断
    # serverL = ['配置管理服务', 8082, ['10.1.0.205', '10.1.0.35']]

    # lb.xls server1 server2 两部分，如果
    # serverData = read_xlrd('lb.xls','server')
    serverData = read_xlrd('test.xls','nginx')
    dfp = dataFileProces(serverData)
    print(dfp)
    # 创建一个 Lb.


    # 打开一个csv 文件 用于存放输出内容
    f = open('text.csv', 'w', encoding='utf-8')
    # 2 基于文件对象构建 csv 写入对象
    csv_w = csv.writer(f)
    # 3 构建列表头
    csv_w.writerow(["Lb_ip", "port", "project_name"])
    # 每个服务分别创建LB
    slbClient = CrcateSlbClient()
    for dfpList in dfp:
        # print (dfpList)
        LoadBalancerName = str('ccb-check-qweqqwwee')+str(dfpList[0]) + str(dfpList[1])
        ListenerPort = dfpList[1]
        LoadBalancer = CreateSlbBalancer(slbClient, LoadBalancerName)
        LoadBalancerId = LoadBalancer['LoadBalancerId']
        LoadBalancerPublicIp = LoadBalancer['PublicIp']
        # print("创建LB,返回信息",LoadBalancer)
        serverL = dfpList
        ListenerName = str(str(serverL[0]) + str(serverL[1]))
        Listener = CreateSlbListener(slbClient, LoadBalancerId, ListenerName, ListenerPort)
        ListenerId = Listener['ListenerId']
        print(LoadBalancerName,LoadBalancerPublicIp,ListenerPort)
        csv_w.writerow([LoadBalancerPublicIp, ListenerPort, LoadBalancerName])
        # print("创建监听返回信息：",Listener)
        for RelServerIp in serverL[2]:
            print(ListenerId, RelServerIp, ListenerPort)
            cswl = CreateSlbWithListener(slbClient, ListenerId, RelServerIp, ListenerPort)
            # print("挂载实例返回信息：",cswl)
        # print(LoadBalancerName)
        # print(ListenerPort)
    f.close()




