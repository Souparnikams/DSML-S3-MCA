from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data1.csv')
X=df[['gives_birth','aquatic_animal','aerial_animal','has_legs']]
y=df[['class_label']]
target_names=['mammal','reptile','fish','amphibian','bird']
feature_names=['gives_birth','aquatic_animal','aerial_animal','has_legs']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
print(x_train)
print(y_train)
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
print(y_pred)
plt.figure(figsize=(15,15))
tree.plot_tree(clf,feature_names=feature_names,class_names=target_names)
plt.show()