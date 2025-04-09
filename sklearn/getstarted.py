# estimator, 所有可以从数据中学习的对象。1. 统一接口 fit(特征数据X,目标值y); 2. 超参数, 不会在fit()过程中学习; 3. 学习参数, 带下划线, coef_
# 常见的有 Classifier(分类器), Regressor(回归器), Transformer(转换器), Clusterer(聚类器)
from sklearn.ensemble import RandomForestClassifier 
clf = RandomForestClassifier(random_state=0)
X = [[1,2,3],[11,12,13]] # X里行是样本，列是特征
y = [0,1] # y是一维数组，第i个数据对应X里第i行
print(clf.fit(X,y))

# Once the estimator is fitted, it can be used for predicting target values of new data.
print(clf.predict(X))
print(clf.predict([[4,5,6],[14,15,16]]))

# Transformer, Preprocessor
from sklearn.preprocessing import StandardScaler
X = [[0, 15], [1, -10]]
print(StandardScaler().fit(X).transform(X))

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 

pipe = make_pipeline(StandardScaler(), LogisticRegression())
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
pipe.fit(X_train, y_train)
print(accuracy_score(pipe.predict(X_test), y_test))

# Model evaluation: cross-validation
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate 

X, y = make_regression(n_samples=1000, random_state=0)
lr = LinearRegression()
result = cross_validate(lr, X, y)
print(result['test_score'])

# 自动参数搜索
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint 

X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
param_distributions = {'n_estimators': randint(1,5), 'max_depth': randint(5,10)}
search = RandomizedSearchCV(estimator=RandomForestRegressor(random_state=0), n_iter=5, param_distributions=param_distributions, random_state=0)
search.fit(X_train, y_train)
print(search.best_params_)