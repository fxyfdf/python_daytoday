
import  csv

# 打开一个csv 文件 用于存放输出内容
f = open('text-csv.csv', 'w', encoding='utf-8')
# 2 基于文件对象构建 csv 写入对象
csv_w = csv.writer(f)
# 3 构建列表头
csv_w.writerow(["Lb_ip", "port", "project_name"])
# 每个服务分别创建LB
for i in range(20):

    csv_w.writerow([LoadBalancerPublicIp, ListenerPort, LoadBalancerName])

f.close()
