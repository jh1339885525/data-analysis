#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 导入包
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[17]:


# 选取相应字段
select_columns = [
    'user_id', 'register_time', 'stone_reduce_value', 'ivory_reduce_value', 
    'meat_reduce_value', 'magic_reduce_value', 'infantry_add_value', 'infantry_reduce_value', 
    'wound_infantry_add_value', 'wound_infantry_reduce_value', 'general_acceleration_reduce_value', 
    'building_acceleration_reduce_value', 'reaserch_acceleration_reduce_value', 'training_acceleration_reduce_value', 
    'treatment_acceleration_reduce_value', 'pvp_battle_count', 'pvp_lanch_count', 'pve_battle_count', 
    'pvp_win_count', 'pve_win_count', 'avg_online_minutes', 'pay_price', 'pay_count',
    'wood_add_value', 'wood_reduce_value', 'stone_add_value', 'ivory_add_value', 'meat_add_value',
    'magic_add_value', 'cavalry_add_value', 'cavalry_reduce_value', 'shaman_add_value', 'shaman_reduce_value',
    'bd_training_hut_level', 'bd_stronghold_level', 'sr_training_speed_level', 'sr_infantry_atk_level'
]

# 使用原始字符串前缀r避免路径转义问题
file_path = r"D:\数据分析文件夹\300 万条《野蛮时代》的玩家数据分析\tap4fun竞赛数据\tap_fun_train.csv"

# 读取数据
original_data = pd.read_csv(file_path, usecols=select_columns)


# In[19]:


import pandas as pd

# 假设 original_data 是你的原始数据集
original_data.rename(columns={
    'user_id': '用户ID',
    'register_time': '注册时间',
    'stone_reduce_value': '石头消耗值',
    'ivory_reduce_value': '象牙消耗值',
    'meat_reduce_value': '肉消耗值',
    'magic_reduce_value': '魔法消耗值',
    'infantry_add_value': '步兵增加值',
    'infantry_reduce_value': '步兵消耗值',
    'wound_infantry_add_value': '受伤步兵增加值',
    'wound_infantry_reduce_value': '受伤步兵消耗值',
    'general_acceleration_reduce_value': '通用加速消耗值',
    'building_acceleration_reduce_value': '建筑加速消耗值',
    'reaserch_acceleration_reduce_value': '研究加速消耗值',
    'training_acceleration_reduce_value': '训练加速消耗值',
    'treatment_acceleration_reduce_value': '治疗加速消耗值',
    'pvp_battle_count': 'PVP战斗次数',
    'pvp_lanch_count': 'PVP发起次数',
    'pve_battle_count': 'PVE战斗次数',
    'pvp_win_count': 'PVP胜利次数',
    'pve_win_count': 'PVE胜利次数',
    'avg_online_minutes': '平均在线分钟数',
    'pay_price': '付费金额',
    'pay_count': '付费次数',
    'wood_add_value': '木材增加值',
    'wood_reduce_value': '木材消耗值',
    'stone_add_value': '石头增加值',
    'ivory_add_value': '象牙增加值',
    'meat_add_value': '肉增加值',
    'magic_add_value': '魔法增加值',
    'cavalry_add_value': '骑兵增加值',
    'cavalry_reduce_value': '骑兵消耗值',
    'shaman_add_value': '萨满增加值',
    'shaman_reduce_value': '萨满消耗值',
    'bd_training_hut_level': '训练小屋等级',
    'bd_stronghold_level': '要塞等级',
    'sr_training_speed_level': '训练速度等级',
    'sr_infantry_atk_level': '步兵攻击等级'
}, inplace=True)


# In[20]:


# 查看数据集的描述性统计信息
original_data.describe()


# In[21]:


original_data.head()


# In[22]:


# 1. 处理缺失值
# 检查数据集中是否有缺失值
missing_values = original_data.isnull().sum()
print("缺失值数量：\n", missing_values)


# In[23]:


#2 检查数据中是否存在重复值
duplicate_values = original_data.duplicated().sum()

# 输出重复值的数量
print("重复值数量：", duplicate_values)


# In[24]:


# 设置中文显示
sns.set(font='SimHei')  # 设置字体为中文黑体


# In[25]:


#3 查看是否有异常值
import matplotlib.pyplot as plt
import seaborn as sns

# 绘制箱线图
plt.figure(figsize=(8, 6))
sns.boxplot(data=original_data)
plt.title('箱型图')
plt.xticks(rotation=90)  # 旋转 x 轴标签，以便更好地显示
plt.show()


# In[11]:


# 将 'register_time' 列转换为 datetime 类型，并提取日期部分
original_data['register_time'] = pd.to_datetime(original_data['register_time']).dt.date


# In[27]:


# 确保 'register_time' 列已经转换为日期类型，并提取日期部分
original_data['注册时间'] = pd.to_datetime(original_data['注册时间']).dt.date

# 按照注册日期进行分组，并计算每个日期的玩家数量
daily_registration = original_data.groupby('注册时间').size()

# 创建绘图
plt.figure(figsize=(12, 6))
plt.plot(daily_registration.index, daily_registration.values, marker='o')

# 设置图形标题和轴标签
plt.title('每日用户注册')
plt.xlabel('注册时间')
plt.ylabel('注册人数')

# 设置x轴显示每一天
plt.xticks(daily_registration.index, rotation=45) # 可以根据需要调整日期显示的间隔，如每周显示一次日期

# 添加网格线
plt.grid(True)

# 显示图形
plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域
plt.show()


# In[28]:


# 计算总用户数
total_users = original_data['用户ID'].nunique()

# 计算付费用户数
paying_users = original_data[original_data['付费金额'] > 0]['用户ID'].nunique()

# 计算付费率
pay_rate = paying_users / total_users

# 计算未付费用户数
non_paying_users = total_users - paying_users

# 创建饼图数据
labels = ['付费用户', '未付费用户']
sizes = [paying_users, non_paying_users]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # 突出显示付费用户

# 绘制饼图
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title('用户付费率')
plt.axis('equal')  # 使饼图为正圆形
plt.show()

# 输出付费率
print(f"付费率（Pay Rate）: {pay_rate:.2%}")


# In[29]:


# 计算总收入
total_revenue = original_data['付费金额'].sum()

# 计算ARPU
arpu = total_revenue / total_users

# 计算ARPPU
arppu = total_revenue / paying_users

# 打印ARPU和ARPPU
print(f"每用户平均收入（ARPU）: {arpu:.2f}")
print(f"付费用户平均收入（ARPPU）: {arppu:.2f}")

# 绘制ARPU和ARPPU的柱状图
labels = ['ARPU', 'ARPPU']
values = [arpu, arppu]
colors = ['#66b3ff','#ff9999']

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=colors)
plt.title('每用户平均收入（ARPU）和付费用户平均收入（ARPPU）')
plt.ylabel('收入（单位：元）')
plt.show()


# In[30]:


# 计算每日新增付费用户数
daily_new_paying_users = original_data[original_data['付费金额'] > 0].groupby('注册时间')['用户ID'].nunique()

# 打印每日新增付费用户数
print("每日新增付费用户数:\n", daily_new_paying_users)

# 绘制每日新增付费用户数的折线图
plt.figure(figsize=(12, 6))
plt.plot(daily_new_paying_users.index, daily_new_paying_users.values, marker='o', linestyle='-', color='b', label='新增付费用户数')
plt.title('每日新增付费用户数')
plt.xlabel('日期')
plt.ylabel('用户数')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[31]:


# 按要塞等级分组
grouped_data = original_data.groupby('要塞等级')

# 计算不同要塞等级的ARPU
arpu_by_level = grouped_data['付费金额'].sum() / grouped_data['用户ID'].nunique()

# 计算不同要塞等级的ARPPU
arppu_by_level = grouped_data['付费金额'].sum() / grouped_data.apply(lambda x: x[x['付费金额'] > 0]['用户ID'].nunique())

# 绘制不同要塞等级的ARPU和ARPPU的柱状图
labels = arpu_by_level.index
x = range(len(labels))

plt.figure(figsize=(12, 6))
plt.bar(x, arpu_by_level.values, width=0.4, label='ARPU', color='#66b3ff', align='center')
plt.bar(x, arppu_by_level.values, width=0.4, label='ARPPU', color='#ff9999', align='edge')
plt.xlabel('要塞等级')
plt.ylabel('收入（单位：元）')
plt.title('不同要塞等级的ARPU和ARPPU')
plt.xticks(x, labels, rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[37]:


# 创建付费标签
original_data['是否付费'] = original_data['付费金额'] > 0

# 按要塞等级和付费情况分组
grouped_data_behavior = original_data.groupby(['要塞等级', '是否付费'])['平均在线分钟数'].mean().unstack()

# 绘制平均在线时长的分组柱状图
plt.figure(figsize=(12, 6))
grouped_data_behavior.plot(kind='bar', stacked=False, figsize=(12, 6), color=['lightcoral', 'lightblue'])
plt.title('按要塞等级和付费情况分组的平均在线时长')
plt.xlabel('要塞等级')
plt.ylabel('平均在线时长（分钟）')
plt.legend(['非付费用户', '付费用户'], title='付费情况')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[38]:


# 按要塞等级和付费情况分组
grouped_data_resources = original_data.groupby(['要塞等级', '是否付费'])['木材消耗值'].mean().unstack()

# 绘制木材消耗值的分组柱状图
plt.figure(figsize=(12, 6))
grouped_data_resources.plot(kind='bar', stacked=False, figsize=(12, 6), color=['lightgreen', 'darkgreen'])
plt.title('按要塞等级和付费情况分组的木材消耗值')
plt.xlabel('要塞等级')
plt.ylabel('平均木材消耗值')
plt.legend(['非付费用户', '付费用户'], title='付费情况')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[39]:


# 按要塞等级和付费情况分组计算训练小屋等级的平均值
grouped_data_building = original_data.groupby(['要塞等级', '是否付费'])['训练小屋等级'].mean().unstack()

# 绘制训练小屋等级的分组柱状图
plt.figure(figsize=(12, 6))
grouped_data_building.plot(kind='bar', stacked=False, figsize=(12, 6), color=['lightblue', 'darkblue'])
plt.title('按要塞等级和付费情况分组的训练小屋等级')
plt.xlabel('要塞等级')
plt.ylabel('平均训练小屋等级')
plt.legend(['非付费用户', '付费用户'], title='付费情况')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[43]:


import pandas as pd

# 创建付费标签
original_data['是否付费'] = original_data['付费金额'] > 0

# 计算每个分组的统计数据
pve_stats = original_data.groupby('是否付费').agg({
    'PVE战斗次数': ['mean', 'median', 'std'],
    'PVE胜利次数': ['mean', 'median', 'std'],
    'PVE胜率': ['mean', 'median', 'std']
}).reset_index()

# 重命名列
pve_stats.columns = ['是否付费', 'PVE战斗次数均值', 'PVE战斗次数中位数', 'PVE战斗次数标准差', 
                     'PVE胜利次数均值', 'PVE胜利次数中位数', 'PVE胜利次数标准差', 
                     'PVE胜率均值', 'PVE胜率中位数', 'PVE胜率标准差']


# In[44]:


import matplotlib.pyplot as plt
import seaborn as sns

# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 付费情况映射
pay_labels = {False: '非氪金玩家', True: '氪金玩家'}

# 替换是否付费字段为中文标签
pve_stats['是否付费'] = pve_stats['是否付费'].map(pay_labels)

# 绘制PVE战斗次数均值的条形图
plt.figure(figsize=(10, 6))
sns.barplot(x='是否付费', y='PVE战斗次数均值', data=pve_stats, palette=['lightblue', 'lightgreen'])
plt.title('PVE战斗次数均值')
plt.xlabel('玩家类型')
plt.ylabel('平均PVE战斗次数')
plt.grid(True)
plt.show()

# 绘制PVE胜利次数均值的条形图
plt.figure(figsize=(10, 6))
sns.barplot(x='是否付费', y='PVE胜利次数均值', data=pve_stats, palette=['lightblue', 'lightgreen'])
plt.title('PVE胜利次数均值')
plt.xlabel('玩家类型')
plt.ylabel('平均PVE胜利次数')
plt.grid(True)
plt.show()

# 绘制PVE胜率均值的条形图
plt.figure(figsize=(10, 6))
sns.barplot(x='是否付费', y='PVE胜率均值', data=pve_stats, palette=['lightblue', 'lightgreen'])
plt.title('PVE胜率均值')
plt.xlabel('玩家类型')
plt.ylabel('平均PVE胜率')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




