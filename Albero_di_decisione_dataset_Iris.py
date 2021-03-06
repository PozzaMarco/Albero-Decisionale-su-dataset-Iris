from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2 

#Parametri di configurazione
criteria = ["entropy","gini"] #criteri di impurità
max_depth = 15 #massima altezza dell'albero.
test_size = 0.2

iris_dataset = load_iris()
iris_dataframe = pd.DataFrame(data= np.c_[iris_dataset['data'], iris_dataset['target']], columns= iris_dataset['feature_names'] + ['target'])
#display(iris_dataframe)

attributes = iris_dataframe[["petal length (cm)", "petal width (cm)"]]
#display(attributes)

classes = iris_dataframe[["target"]]
#display(classes)

X_train, X_test, Y_train, Y_test = train_test_split(attributes, classes, test_size = test_size, random_state=5)

for criterion in criteria:
  X_attributes = np.vstack((X_train, X_test))
  Y_classes= np.vstack((Y_train, Y_test)).flatten()
  
  tree = DecisionTreeClassifier(criterion = criterion, max_depth = max_depth, random_state = 0)
  tree.fit(X_train, Y_train);
  
  fileName = "decisionTree_" + str(criterion)
  fileDOT = fileName + ".dot"
  filePNG = fileName + ".png"
  
  export_graphviz(tree, out_file=fileDOT, feature_names=['petal length','petal width'])
  
  !dot $fileDOT -Tpng -o $filePNG #trasformo il file.dot in un immainge.png
  
  predictedClasses = tree.predict(X_test)
  accurancy = round(tree.score(X_test,Y_test),2)*100
    
  #Stampa del grafico associato all'albero
  plot_decision_regions(X_attributes, Y_classes.astype(np.integer), clf=tree)
  plt.title("Classificazione con criterio di impurità = " + str(criterion) + "\n Accuratezza: " + str(accurancy) + 
             "%\n Profondità albero: " + str(max_depth) + " \n Dimensione del training set: " + str((1 - test_size)*100) +"%")
  plt.xlabel("petal length[cm]")
  plt.ylabel("petal width[cm]")
  plt.legend(loc="upper left")
  plt.show()
    
  !rm *.dot
