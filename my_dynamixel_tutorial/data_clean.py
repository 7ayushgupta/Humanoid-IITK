#importing numpy from Scipy stack
import scipy.io as sio
import numpy as np

angles_content = sio.loadmat('angles.mat')
left_angles_matrix = angles_content['la']
right_angles_matrix = angles_content['ra']

cleaned_left = np.matrix(left_angles_matrix)
cleaned_left = np.delete(cleaned_left, 0,0)
cleaned_left = np.delete(cleaned_left, 5,0)
cleaned_left = cleaned_left.T

cleaned_right = np.matrix(right_angles_matrix)
cleaned_right = np.delete(cleaned_right, 0,0)
cleaned_right = np.delete(cleaned_right, 5,0)
cleaned_right = cleaned_right.T

np.savetxt("cleaned_angles_left.csv", cleaned_left, delimiter=",")
np.savetxt("cleaned_angles_right.csv", cleaned_right, delimiter=",")

#import numpy as np
#np.genfromtxt('myfile.csv',delimiter=',')




