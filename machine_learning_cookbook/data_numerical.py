import numpy as np 
import matplotlib.pyplot as plt
from sklearn import preprocessing 

feature = np.array([[-500.5],
                    [-100.1],
                    [0],
                    [100.1],
                    [900.9]])
minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
scaled_feature = minmax_scale.fit_transform(feature)
print(scaled_feature)

# mean=0, std=1
scaler = preprocessing.StandardScaler()
standardized = scaler.fit_transform(feature)
print(standardized)

# Normalizer sqrt(x^2+y^2)=1
features = np.array([[0.5,0.5],
                    [1.1,3.4],
                    [1.5,20.2],
                    [1.63,34.4],
                    [10.9,3.3]])
normalizer = preprocessing.Normalizer(norm="l2")
print(normalizer.transform(features))

features = np.array([[2,3],
                     [2,3],
                     [2,3]])
polynomial_interaction = preprocessing.PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
print(polynomial_interaction.fit_transform(features))

# Transforming features
# def add_ten(x: int) -> int:
#     return x + 10

# transformer = preprocessing.FunctionTransformer(add_ten)
transformer = preprocessing.FunctionTransformer(lambda x: x+10)
print(transformer.transform(features))

from sklearn.covariance import EllipticEnvelope 
from sklearn.datasets import make_blobs 

features, labels = make_blobs(n_samples = 10,
                         n_features = 2,
                         centers = 1,
                         random_state= 1)
print(features)
features[0,0], features[0,1] = 20, 20
# # 绘制数据
# plt.figure(figsize=(8, 6))
# plt.scatter(features[:, 0], features[:, 1], c=labels, cmap='viridis', s=50, edgecolor='k')
# plt.title("Visualization of Blobs")
# plt.xlabel("Feature 1")
# plt.ylabel("Feature 2")
# plt.grid(True)
# plt.show()

outlier_detector = EllipticEnvelope(contamination=.1)
outlier_detector.fit(features)
print(outlier_detector.predict(features))


import pandas as pd 
from sklearn.cluster import KMeans

features, labels = make_blobs(n_samples = 50,
                              n_features = 2,
                              centers = 3,
                              random_state = 1)
dataframe = pd.DataFrame(features, columns=["feature_1","feature_2"])
clusterer = KMeans(3, random_state=0)
clusterer.fit(features)
dataframe["group"] = clusterer.predict(features)
print(dataframe.head(20))

# 绘制数据
plt.figure(figsize=(8, 6))
plt.scatter(features[:, 0], features[:, 1], c=labels, cmap='viridis', s=50, edgecolor='k')
plt.title("Visualization of Blobs")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()