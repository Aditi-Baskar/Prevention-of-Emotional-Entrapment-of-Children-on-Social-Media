import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
y_test = pd.read_csv("C:\\Users\\Kripa\\Desktop\\oporg(test).csv")
y_pred = pd.read_csv("C:\\Users\\Kripa\\Desktop\\opclssf(nb-test).csv")
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))