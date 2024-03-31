import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os


# Load the dataset
relative_data_path = Path('..') / 'Lab2_Datasets' / 'Lab2d_power.csv'
data_driver_bin = str(relative_data_path.resolve())
data = pd.read_csv(data_driver_bin)


# 设置选项以显示所有列
pd.set_option('display.max_columns', None)


# # 1. Simple exploratory data analysis  # 1. 简单的探索性数据分析
# print("First few rows of the dataset:")  # 数据集的前几行
# print(data.head())
#
# print("\nBasic information about the data set:")  # 数据集的基本信息
# print(data.info())
#
# print("\nStatistical summary of the dataset:")  # 数据集的统计摘要
# print(data.describe())


# # 2. Check and clean the data set  # 2. 检查和清理数据集
# # Check for missing values  # 检查缺失值
# print("\nCheck for missing values:")  # 检查缺失值
# print(data.isnull().sum())
#
# # If there are missing values,
# # handle them according to the situation,
# # such as deleting rows containing missing values or using interpolation to fill in missing values.
# # 如果有缺失值，可以根据情况进行处理，例如删除包含缺失值的行或使用插值法填充缺失值


# 3. Conduct meaningful exploratory data analysis and plotting  # 3. 进行有意义的探索性数据分析和绘图

# 创建保存图像的文件夹
if not os.path.exists('PNG'):
    os.makedirs('PNG')

# 选择数值型的列
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# # 计算统计指标
# mean_value = numeric_data.mean()
# median_value = numeric_data.median()
# std_deviation = numeric_data.std()
#
# # 创建统计指标的DataFrame
# stats_df = pd.DataFrame({
#     'Mean': mean_value,
#     'Median': median_value,
#     'Standard Deviation': std_deviation
# })
#
# # 输出统计指标
# print(stats_df)


# # 计算相关系数
# correlation_matrix = numeric_data.corr()
#
# # 输出相关系数矩阵
# print(correlation_matrix)
#
# # # 可视化相关性矩阵
# # plt.figure(figsize=(10, 8))
# # sns.heatmap(correlation_matrix, annot=True)
# # plt.title('Correlation Matrix')
# # plt.savefig(f'PNG/Correlation_Matrix.png')  # 保存直方图
# # plt.show()
# # 绘制相关系数矩阵图
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True)
# plt.title('Correlation Matrix')
#
# # 保存图像
# plt.savefig('PNG/Correlation_Matrix.png')
# plt.show()

# # 对每一列数据进行分析和可视化
# for column in numeric_data.columns:
#     # Draw histogram  # 绘制直方图
#     plt.figure(figsize=(10, 6))
#     plt.hist(data[column], bins=20, color='skyblue')
#     plt.title(f'Histogram of {column}')
#     plt.xlabel('Values')
#     plt.ylabel('Frequency')
#     plt.savefig(f'PNG/Histogram__{column}.png')  # 保存直方图
#     plt.close()
#
#     # Draw box plot  # 绘制箱线图
#     plt.figure(figsize=(10, 6))
#     sns.boxplot(x=data[column])
#     plt.title(f'Boxplot of {column}')
#     plt.xlabel('Values')
#     plt.savefig(f'PNG/Box_Plot__{column}.png')  # 保存箱线图
#     plt.close()
#
#     # Draw density plot  # 绘制密度图
#     plt.figure(figsize=(10, 6))
#     sns.kdeplot(data[column], fill=True, color='skyblue')
#     plt.title(f'Density Plot of {column}')
#     plt.xlabel('Values')
#     plt.ylabel('Density')
#     plt.savefig(f'PNG/Density_Plot__{column}.png')  # 保存密度图
#     plt.close()

# # 确定相关系数大于0.5的变量组
# highly_correlated_vars = []
# for var1 in correlation_matrix.columns:
#     for var2 in correlation_matrix.index:
#         if var1 != var2 and abs(correlation_matrix.loc[var1, var2]) > 0.5:
#             highly_correlated_vars.append((var1, var2))
#
# # 绘制折线图
# for var1, var2 in highly_correlated_vars:
#     plt.figure(figsize=(8, 6))
#     plt.plot(data[var1], data[var2])
#     plt.title(f'Line Plot of {var1} and {var2}')
#     plt.xlabel(var1)
#     plt.ylabel(var2)
#     plt.savefig(f'PNG/Line_Plot_of_{var1}_and_{var2}.png')  # 保存折线图
#     plt.show()

# # 获取时间列
# time_column = pd.to_datetime(data['Datetime'])
#
# # 绘制折线图
# for column in numeric_data.columns:
#     plt.figure(figsize=(10, 6))
#     plt.plot(time_column, numeric_data[column])
#     plt.title(f'Line Plot of {column} over Time')
#     plt.xlabel('Time')
#     plt.ylabel(column)
#     plt.xticks(rotation=45)  # 旋转x轴刻度标签，以便更好地显示时间信息
#     plt.savefig(f'PNG/Line_Plot_of_{column}_over_Time.png')  # 保存折线图
#     plt.show()


# 将时间列设置为索引
data['Datetime'] = pd.to_datetime(data['Datetime'])
data.set_index('Datetime', inplace=True)

# 计算日均、月均、年均值
daily_mean = data.resample('D').mean()
monthly_mean = data.resample('ME').mean()


# 绘制折线图
for column in data.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(daily_mean.index, daily_mean[column], label='Daily Mean')
    plt.title(f'Daily Mean Values of {column}')
    plt.xlabel('Time')
    plt.ylabel('Daily Mean Value')
    plt.xticks(rotation=45)  # 旋转x轴刻度标签，以便更好地显示时间信息
    plt.savefig(f'PNG/Daily_Mean_Values_of_{column}.png')  # 保存折线图
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_mean.index, monthly_mean[column], label='Monthly Mean')
    plt.title(f'Monthly Mean Values of {column}')
    plt.xlabel('Time')
    plt.ylabel('Monthly Mean Value')
    plt.xticks(rotation=45)  # 旋转x轴刻度标签，以便更好地显示时间信息
    plt.savefig(f'PNG/Monthly_Mean_Values_of_{column}.png')  # 保存折线图
    plt.show()

