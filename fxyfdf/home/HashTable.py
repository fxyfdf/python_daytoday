
'''
散列表是一种数据结构，其中数据元素的地址或索引值是由散列函数生成的。这使得访问数据的速度更快，
因为索引值是数据值的关键字。换句话说，哈希表存储键值对，但密钥是通过哈希函数生成的。
因此，数据元素的搜索和插入函数变得更快，因为键值本身成为存储数据的数组的索引。
在Python中，Dictionary数据类型表示哈希表的实现。字典中的密钥满足以下要求。
    字典的键是可散列的，即通过散列函数生成，该散列函数为提供给散列函数的每个唯一值生成唯一的结果。
    字典中数据元素的顺序不固定。
所以我们通过使用下面的字典数据类型来看到哈希表的实现。

'''


'''
在词典中访问值

要访问字典元素，可以使用熟悉的方括号和密钥来获取它的值。
'''
# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

'''
更新字典
'''

# Declare a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


'''
删除字典元素

您可以删除单个字典元素，也可以清除字典的全部内容。您也可以在一个操作中删除整个字典。要显式删除整个字典，只需使用del语句。 -
'''
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])