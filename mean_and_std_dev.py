import matplotlib.pyplot as plt
import numpy as np



# rf_cpu  = [0.00,  394.45, 100.10, 100.22,   0.00]
# rf_ram  = [39.03,  57.12, 157.90, 172.70,   38.9]
# dt_cpu  = [0.00,     0.0, 953.62,  28.28,   0.00]
# dt_ram  = [31.85,  31.85,  99.62,  32.41,  42.41]
# knn_cpu = [0.00,  554.24, 100.01,  51.86,   0.00]
# knn_ram = [38.71, 133.20, 155.70,  38.91,  38.76]
# gnb_cpu = [0.00,   0.0  , 914.24,  44.46,   0.00]
# gnb_ram = [32.44,  32.44,  85.79,  32.99,  32.99]
# mlp_cpu = [0.00,  573.53, 100.15, 100.17, 100.25]
# mlp_ram = [32.20, 128.10, 145.60, 145.60, 145.60]

rf_cpu  = [394.45,  100.22]
rf_ram  = [ 157.90, 172.70, 33.30]
dt_cpu  = [ 953.62,  28.28]
dt_ram  = [ 99.62,  32.41, 33.30]
knn_cpu = [554.24, 100.01]
knn_ram = [133.20, 155.70, 33.30]
gnb_cpu = [ 914.24,  44.46]
gnb_ram = [85.79,  32.99, 33.30]
mlp_cpu = [573.53, 100.17]
mlp_ram = [128.10, 145.60, 33.30]

rf_cpu_max = [394.45]
rf_ram_max = [172.70]
dt_cpu_max = [953.62]
dt_ram_max = [99.62]
knn_cpu_max = [554.24]
knn_ram_max = [155.70]
gnb_cpu_max = [914.24]
gnb_ram_max = [85.79]
mlp_cpu_max = [573.53]
mlp_ram_max = [145.60]


#mean = sum(test_list) / len(test_list)
#variance = sum([((x - mean) ** 2) for x in test_list]) / len(test_list)


mean_rf_cpu = sum(rf_cpu)/len(rf_cpu)
var_rf_cpu = sum([((x - mean_rf_cpu) ** 2) for x in rf_cpu]) / len(rf_cpu)
res_rf_cpu = var_rf_cpu ** 0.5

mean_dt_cpu = sum(dt_cpu)/len(dt_cpu)
var_dt_cpu = sum([((x - mean_dt_cpu) ** 2) for x in dt_cpu]) / len(dt_cpu)
res_dt_cpu = var_dt_cpu ** 0.5

mean_knn_cpu = sum(knn_cpu)/len(knn_cpu)
var_knn_cpu = sum([((x - mean_knn_cpu) ** 2) for x in knn_cpu]) / len(knn_cpu)
res_knn_cpu = var_knn_cpu ** 0.5

mean_gnb_cpu = sum(gnb_cpu)/len(gnb_cpu)
var_gnb_cpu = sum([((x - mean_gnb_cpu) ** 2) for x in gnb_cpu]) / len(gnb_cpu)
res_gnb_cpu = var_gnb_cpu ** 0.5

mean_mlp_cpu = sum(mlp_cpu)/len(mlp_cpu)
var_mlp_cpu = sum([((x - mean_mlp_cpu) ** 2) for x in mlp_cpu]) / len(mlp_cpu)
res_mlp_cpu = var_mlp_cpu ** 0.5



#ram
mean_rf_ram = sum(rf_ram)/len(rf_ram)
var_rf_ram = sum([((x - mean_rf_ram) ** 2) for x in rf_ram]) / len(rf_ram)
res_rf_ram = var_rf_ram ** 0.5

mean_dt_ram = sum(dt_ram)/len(dt_ram)
var_dt_ram = sum([((x - mean_dt_ram) ** 2) for x in dt_ram]) / len(dt_ram)
res_dt_ram = var_dt_ram ** 0.5

mean_knn_ram = sum(knn_ram)/len(knn_ram)
var_knn_ram = sum([((x - mean_knn_ram) ** 2) for x in knn_ram]) / len(knn_ram)
res_knn_ram = var_knn_ram ** 0.5

mean_gnb_ram = sum(gnb_ram)/len(gnb_ram)
var_gnb_ram = sum([((x - mean_gnb_ram) ** 2) for x in gnb_ram]) / len(gnb_ram)
res_gnb_ram = var_gnb_ram ** 0.5

mean_mlp_ram = sum(mlp_ram)/len(mlp_ram)
var_mlp_ram = sum([((x - mean_mlp_ram) ** 2) for x in mlp_ram]) / len(mlp_ram)
res_mlp_ram = var_mlp_ram ** 0.5



x = np.array(['RF', 'DT', 'KNN', 'GNB', 'MLP'])
#y = np.array([mean_rf_cpu, mean_dt_cpu, mean_knn_cpu, mean_gnb_cpu, mean_mlp_cpu]) # Effectively y = x**2
#e = np.array([res_rf_cpu, res_dt_cpu, res_knn_cpu, res_gnb_cpu, res_mlp_cpu])

y = np.array([mean_rf_ram, mean_dt_ram, mean_knn_ram, mean_gnb_ram, mean_mlp_ram]) # Effectively y = x**2
e = np.array([res_rf_ram, res_dt_ram, res_knn_ram, res_gnb_ram, res_mlp_ram])

plt.errorbar(x, y, e, linestyle='None', marker='s')
plt.xlabel('Algorithms', fontsize=10)
plt.ylabel('CPU percentage', fontsize=10)
plt.ylabel('Memory in MB', fontsize=10)
#plt.plot(x, y)
plt.title("Algorithms and Memory Usage")
#plt.title("Algorithms and RAM Usage")
plt.show()