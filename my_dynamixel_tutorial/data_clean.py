#importing numpy from Scipy stack
import scipy.io as sio
import numpy as np

angles_content = sio.loadmat('Data_angles/angles_new.mat')
left_angles_matrix = angles_content['la']
right_angles_matrix = angles_content['ra']

cleaned_left = np.matrix(left_angles_matrix)
cleaned_left = np.delete(cleaned_left, 0,0)
cleaned_left = np.delete(cleaned_left, 5,0)
cleaned_left = cleaned_left.T
cleaned_left[:,0] *= -1
cleaned_left[:,1] *= -1
cleaned_left[:,4] *= -1
for i in range(0, 199):
	if cleaned_left[i,3]>26:
		cleaned_left[i,3] = 26


cleaned_right = np.matrix(right_angles_matrix)
cleaned_right = np.delete(cleaned_right, 0,0)
cleaned_right = np.delete(cleaned_right, 5,0)
cleaned_right = cleaned_right.T
cleaned_right[:,0] *= -1
cleaned_right[:,2] *= -1
cleaned_right[:,3] *= -1
cleaned_right[:,4] *= -1
for i in range(0, 200):
	if cleaned_right[i,3]>26:
		cleaned_right[i,3] = 26


np.savetxt("Data_angles/cleaned_angles_left.csv", cleaned_left, delimiter=",")
np.savetxt("Data_angles/cleaned_angles_right.csv", cleaned_right, delimiter=",")

angles_matrix = np.column_stack((cleaned_right[:,[4]],cleaned_right[:,[3]],cleaned_right[:,[2]],cleaned_right[:,[1]],cleaned_right[:,[0]],cleaned_left[:,[0]],cleaned_left[:,[1]],cleaned_left[:,[2]],cleaned_left[:,[3]],cleaned_left[:,[4]]))
angles_matrix = np.multiply(angles_matrix, 0.0174532925)
1print(angles_content)
print(angles_matrix.shape)
print(angles_matrix)
np.savetxt("Data_angles/angles_data.csv", angles_matrix, delimiter=",")




