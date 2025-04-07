# make_regression 用于生成回归问题的数据集，可以控制特征数量、噪声
from sklearn.datasets import make_regression, make_classification, make_blobs
import matplotlib.pyplot as plt 

# X, y = make_regression(n_samples=100, # 样本数量
#                        n_features=1, # 特征数量
#                        noise=10, # 噪声水平
#                        random_state=42) # 随机种子

# # 可视化
# plt.scatter(X,y)
# plt.title('Simple Regression Dataset')
# plt.xlabel('Feature')
# plt.ylabel('Target')
# plt.show()

# X, y = make_classification(n_samples=50, # 样本数量
#                            n_features=2, # 特征数量 
#                            n_informative=2, # 有信息量的特征
#                            n_redundant=0, # 冗余特征
#                            n_clusters_per_class=1, # 每个类别的簇数
#                            random_state=42)
# print(X)
# print(y)
# # 可视化
# plt.scatter(X[:,0], X[:,1], c=y, cmap='viridis', edgecolors='k')
# plt.title('Binary Classification Dataset')
# plt.xlabel('Feature 1')
# plt.ylabel('Feature 2')
# plt.colorbar(label='Class')
# plt.show()

X, y = make_blobs(n_samples=100,
                  n_features=2,
                  centers=4,  # 簇的数量
                  cluster_std=1.0, # 簇的标准差
                  center_box=(-10,10), # 簇中心的边界框
                  random_state=42)

# 可视化
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.title('Blob Dataset with 4 clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.show()