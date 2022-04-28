import numpy as np
import matplotlib.pyplot as plt
p = 1/2
n = np.arange(0,10)
X = np.power(p,n)
plt.bar(n,X)




data = pd.read_csv("C:/Users/Loe/Desktop/Project Resources/healthcare-dataset-stroke-data.csv")
n = 4
RANDOM_STATE = 42
data_dimension = 2

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = RANDOM_STATE)

qsvc = QSVC()
qsvc.quantum_kernel.quantum_instance = quantum_instance

qsvc.fit(X_train, X_test)
qsvc_score = qsvc.score(y_train, y_test)

print(f'QSVC classification test score: {qsvc_score}')

from sklearn.svm import SVC

svc = SVC(kernel=zz_kernel.evaluate)
svc.fit(X_train, y_train)
score = svc.score(X_test, y_test)
print(f'Callable kernel with ZZFeatureMap classification test score: {score}')