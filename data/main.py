import re
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from string import ascii_uppercase
#import matplotlib.pyplot as plt
#read a fila with bch extension
#read the file with bch extension
# file = open("./benchmarks/optim/hard/chem-1.bch", "r")
# list = []
# for line in file:
#     #print(line)
#     #extract only the characters with x with numbers using a regex
#     regex = re.compile(r'x\d+')
#     #use the regex on lines
#     matches = regex.finditer(line)
#     for match in matches:
#         #print(match.group(), "found at", match.start(), "-", match.end())
#         # save all the matches in a list but not repeated
#         if match.group() not in list:
#              list.append(match.group())
        
# print(list)
# print(len(list))

y_verd = np.array([2.95320958552e-05, 0.00010619843323, 0.5, 0.00010619843323, 2.95320958552])
y_pred = np.array([2.10943541823e-06, 7.58560237352, 7.14285714286, 7.58560237352, 2.10943541823])

# transform continuous varibles to discrete variables on the arrays
for i in range(len(y_verd)):
    if y_verd[i] < 0.5:
        y_verd[i] = 0
    else:
        y_verd[i] = 1

for i in range(len(y_pred)):
    if y_pred[i] < 0.5:
        y_pred[i] = 0
    else:
        y_pred[i] = 1
     
confm=confusion_matrix(y_verd, y_pred)
print(confm)

sns.heatmap(confm, annot=True, fmt="d", cmap="YlGnBu", xticklabels=ascii_uppercase[0:2], yticklabels=ascii_uppercase[0:2])
plt.ylabel("Original Precision Label")
plt.xlabel("Predicted Label considered entrance values")
plt.title("Confusion Matrix for medium problem")
plt.show()

y_verd_2 = np.array([2.57300368342e-08, 2.57300368342e-08, 2.57300368342e-08, 2.57300368342e-08, 2.57300368342e-08])
y_pred_2 = np.array([5.14600736684e-09, 5.14600736684e-09, 5.14600736684e-09, 5.14600736684e-09, 5.14600736684e-09])

# transform continuous varibles to discrete variables on the arrays
for i in range(len(y_verd_2)):
    if y_verd_2[i] < 0.5:
        y_verd_2[i] = 0
    else:
        y_verd_2[i] = 1

for i in range(len(y_pred_2)):
    if y_pred_2[i] < 0.5:
        y_pred_2[i] = 0
    else:
        y_pred_2[i] = 1
     
confm2=confusion_matrix(y_verd_2, y_pred_2)
print(confm2)

sns.heatmap(confm2, annot=True, fmt="d", cmap="YlGnBu", xticklabels=ascii_uppercase[0:2], yticklabels=ascii_uppercase[0:2])
plt.ylabel("Original Precision Label")
plt.xlabel("Predicted Label considered entrance values")
plt.title("Confusion Matrix for easy problem")
plt.show()


y_verd_3 = np.array([0.4357687687865, 0.02957687687865, 2.768768786509, 34.768768786509, 0.0768768786509])
y_pred_3 = np.array([0.0396153426169545, 0.0026888069889682, 0.251706253319, 3.160797162409909, 0.0069888071500818])

# transform continuous varibles to discrete variables on the arrays
for i in range(len(y_verd_3)):
    if y_verd_3[i] < 0.5:
        y_verd_3[i] = 0
    else:
        y_verd_3[i] = 1

for i in range(len(y_pred_3)):
    if y_pred_3[i] < 0.5:
        y_pred_3[i] = 0
    else:
        y_pred_3[i] = 1
     
confm3=confusion_matrix(y_verd_3, y_pred_3)
print(confm3)

sns.heatmap(confm3, annot=True, fmt="d", cmap="YlGnBu", xticklabels=ascii_uppercase[0:2], yticklabels=ascii_uppercase[0:2])
plt.ylabel("Original Precision Label")
plt.xlabel("Predicted Label considered entrance values")
plt.title("Confusion Matrix for hard problem")
plt.show()

list_Linealizer_time = [0.00156540600001, 0.00129612300001,0.00170638300001,0.00152754200001,0.00169250300001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Linealizer")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the Linealizer algorithm for easy problem")
plt.legend()
plt.show()

list_Linealizer_time = [0.0175088730001, 0.0205858250001, 0.0320129600001,0.0184028890001,0.0198788090001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Network Execution")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the ANN for easy problem")
plt.legend()
plt.show()

list_Linealizer_time = [0.000752900000001,  0.000418586000001, 0.000804849000001, 0.00114606800001, 0.000279203000001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Simplex Execution")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the Simplex algorithm for easy problem")
plt.legend()
plt.show()

list_Linealizer_time = [2.57300368342e-08, 2.57300368342e-08, 2.57300368342e-08, 2.57300368342e-08, 2.57300368342e-08]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Precision cont consider the number of entry values")
plt.xlabel("Number of variables")
plt.ylabel("Percentage of precision")
plt.title("Percentage of precision of the iterations for easy problem")
plt.legend()
plt.show()

#### MEDIUM #####
list_Linealizer_time = [0.0206720790001, 0.0218346080001, 0.0165140420001, 0.0221773420001, 0.0200189850001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Linealizer")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the Linealizer algorithm for medium problem")
plt.legend()
plt.show()

list_Linealizer_time = [0.558092955001, 0.512725123001, 0.364417935001,0.513259493001,0.452759055001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Network Execution")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the ANN for medium problem")
plt.legend()
plt.show()

list_Linealizer_time = [0.150827633001,  0.146546427001, 0.121254475001, 0.149986162001, 0.144760759001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Simplex Execution")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the Simplex algorithm for medium problem")
plt.legend()
plt.show()

list_Linealizer_time = [2.95320958552e-05, 0.00010619843323, 0.5, 0.00010619843323, 2.95320958552e-05]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Precision cont consider the number of entry values")
plt.xlabel("Number of variables")
plt.ylabel("Percentage of precision")
plt.title("Percentage of precision of the iterations for medium problem")
plt.legend()
plt.show()

#### HARD ####

list_Linealizer_time = [4863.00169250300001, 3739.00169250300001, 4866.00169250300001, 2866.00169250300001, 4031.00169250300001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Linealizer")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the Linealizer algorithm for hard problem")
plt.legend()
plt.show()

list_Linealizer_time = [5832.0198788090401, 4603.0198788090401, 5605.0198788090401, 4001.0198788090401, 4555.0198788090401]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Network Execution")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the ANN for hard problem")
plt.legend()
plt.show()

list_Linealizer_time = [5305.000279203000001, 4201.000279203000001, 5201.000279203000001, 3908.000279203000001, 5201.000279203000001]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Simplex Execution")
plt.xlabel("Number of variables")
plt.ylabel("Time (s)")
plt.title("Time of execution of the Simplex algorithm for hard problem")
plt.legend()
plt.show()

list_Linealizer_time = [0.4357687687865, 0.02957687687865, 2.768768786509, 34.768768786509, 0.0768768786509]
eje_x = [1,2,3,4,5]

#haz una grafica de los tiempos de ejecucion de los algoritmos
plt.plot(eje_x, list_Linealizer_time, label = "Precision cont consider the number of entry values")
plt.xlabel("Number of variables")
plt.ylabel("Percentage of precision")
plt.title("Percentage of precision of the iterations for hard problem")
plt.legend()
plt.show()