# 编码名义分类特征
import numpy as np
from sklearn.preprocessing import LabelBinarizer, MultiLabelBinarizer
import pandas as pd

# one-hot encoding 将每个类别变量转换为一个二进制向量，向量的长度等于类别的数量。每个类别对应于向量中的一个1，其他为0.
feature = np.array([["Texas"],["California"],["Texas"],["Delaware"],["Texas"]])
one_hot = LabelBinarizer()
print(one_hot.fit_transform(feature))
print(one_hot.classes_)
print(pd.get_dummies(feature[:,0]))

# 编码有序分类特征
dataframe = pd.DataFrame({"Score":["Low","High","Medium","Low","High"]})
print(pd.get_dummies(dataframe["Score"]))
scale_mapper = {"Low":1,"Medium":2,"High":3}
print(dataframe["Score"].replace(scale_mapper))

# 编码特征字典
from sklearn.feature_extraction import DictVectorizer
data = [{"Red":2,"Blue":4},{"Red":4,"Blue":3},{"Red":1,"Yellow":2,"Blue":3},{"Red":2,"Yellow":2}]
dictvectorizer = DictVectorizer(sparse=False)
# dictvectorizer = DictVectorizer()
features = dictvectorizer.fit_transform(data)
print(features)
# machine learning algorithms expect the data to be in the form of matrix.

# 输入缺失类值
from sklearn.neighbors import KNeighborsClassifier
X = np.array([[0, 2.10, 1.45],
              [1, 1.18, 1.33],
              [0, 1.22, 1.27],
              [1, -0.21, -1.19]])
X_with_nan = np.array([[np.nan, 0.87, 1.31],
                       [np.nan, -0.67, -0.22]])

clf = KNeighborsClassifier(3, weights='distance')
trained_model = clf.fit(X[:,1:], X[:,0])
imputed_values = trained_model.predict(X_with_nan[:,1:])
print(imputed_values)
X_with_imputed = np.hstack((imputed_values.reshape(-1,1), X_with_nan[:,1:]))
print(np.vstack((X_with_imputed, X)))

# 处理不平衡类
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris 
iris = load_iris()
features = iris.data
target = iris.target 
features = features[40:,:]
target = target[40:]
target = np.where((target==0), 0, 1)
print(target)