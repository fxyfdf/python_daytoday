
import  yaml
import  os

# 先找到 yaml 文件的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(cur_path,"prometheus.yml")

# 打开文件
f = open(yaml_path, 'r', encoding='utf-8')
# y = yaml.load(f,Loader=yaml.FlowEntryToken)
# 读取文件
yaml_content = f.read()
print(type(yaml_path)) # <class 'str'>
print (yaml_path) # 注释也读出来

# 有没有什么地方转化为其他类型
yaml_content_dict = yaml.load(yaml_content)
# print(type(yaml_content_dict))
print("yaml_concent_dict",yaml_content_dict)
print(yaml_content_dict)

f.close()




