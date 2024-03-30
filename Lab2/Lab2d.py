import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load the dataset
relative_data_path = Path('Lab2_Datasets') / 'Lab2d_power.csv'
data_driver_bin = str(relative_data_path.resolve())
data = pd.read_csv(data_driver_bin)

# 1. 简单的探索性数据分析
print("数据集的前几行:") 
print(data.head())

print("\n数据集的基本信息:")
print(data.info())

print("\n数据集的统计摘要:")
print(data.describe())

# 2. 检查和清理数据集
# 检查缺失值
print("\n检查缺失值:")
print(data.isnull().sum())

# 如果有缺失值，可以根据情况进行处理，例如删除包含缺失值的行或使用插值法填充缺失值

# 3. 进行有意义的探索性数据分析和绘图
# 对每一列数据进行分析和可视化
for column in data.columns:
    if data[column].dtype in ['int64', 'float64']:  # 只处理数值型数据
        # 绘制直方图
        plt.figure(figsize=(10, 6))
        plt.hist(data[column], bins=20, color='skyblue')
        plt.title(f'Histogram of {column}')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.show()

        # 绘制箱线图
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=data[column])
        plt.title(f'Boxplot of {column}')
        plt.xlabel('Values')
        plt.show()

        # 绘制密度图
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data[column], fill=True, color='skyblue')
        plt.title(f'Density Plot of {column}')
        plt.xlabel('Values')
        plt.ylabel('Density')
        plt.show()

    else:
        # 对非数值型数据进行其他处理，例如计算频数统计等
        pass
