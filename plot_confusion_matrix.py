import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
array =[[   0,    0,    4,   88,    0],
 [   0,    0, 193,    7 ,   0],
 [   0,    0, 1086,  178,    0],
 [   0,    0,  128,  841,    0],
 [   0,    0,    0,  139,    0]]

df_cm = pd.DataFrame(array, index = [i for i in "01234"],columns = [i for i in "01234"])
#plt.xlabel('Predicted Label', fontsize=10)
#plt.ylabel('True Label', fontsize=10)

# disp = ConfusionMatrixDisplay(confusion_matrix=df_cm, display_labels=[0,1,2,3,4])
# disp.plot()
# plt.show()

plt.figure(figsize = (10,7))
s = sn.heatmap(df_cm, annot=True, fmt='g', cbar='False', cmap='Blues')
s.set(xlabel='Predicted Label', ylabel='True Label')
plt.show()