# Albero-Decisionale-su-dataset-Iris
Esempio di albero di decisione creato utilizzando il dataset Iris cosi strutturato:

* 150 campioni;
* 4 attributi (petal width, petal length, sepal width, sepal length);
* 3 classi (0= Iris Setosa, 1= Iris Versicolour, 2= Iris Virginica);
* 50 campioni per classe.

La libreria utilizzata è *DecisionTreeClassifier* fornita da sklearn. 
L' esempio è stato utilizzato per vedere gli effetti del *Reduced Error Pruning* e della variazione del *guadagno informativo*
tramite l'*entropia* o l'impurità di *gini* gli unici due metodi di impurità implementati dal DecisionTreeClassifier
