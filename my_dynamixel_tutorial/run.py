#!/home/ayush/anaconda3/bin/python python3
import roslib
roslib.load_manifest('my_dynamixel_tutorial')

#Importing necessary basic packages 
import rospy
import actionlib
from std_msgs.msg import Float64
import trajectory_msgs.msg 
import control_msgs.msg  
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal

#importing numpy from Scipy stack
import scipy.io as sio
import numpy as np
left_leg_mat = np.genfromtxt('Data_angles/cleaned_angles_left.csv',delimiter=',')
right_leg_mat = np.genfromtxt('Data_angles/cleaned_angles_right.csv',delimiter=',')
angles_mat = np.genfromtxt('Data_angles/angles_data.csv', delimiter=',')

#for using the ith row of a 2D array
duration = 5

#arm_name should be b_arm or f_arm
class Joint:

        def __init__(self, motor_name):
            #basic initialisation of an object from tjhe joint class
            self.name = motor_name   
            print(motor_name)        
            self.jta = actionlib.SimpleActionClient('/'+self.name+'_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
            rospy.loginfo('Waiting for joint trajectory action')
            self.jta.wait_for_server()
            rospy.loginfo('Found joint trajectory action!')
                
        def move_joint(self, angles):
            #setting up the trajectory
            goal = FollowJointTrajectoryGoal()                  
            char = self.name[0] #either 'f' or 'b'
            goal.trajectory.joint_names = ['motor8', 'motor9','motor10','motor11','motor12','motor13','motor14','motor15','motor16','motor17']
            point = JointTrajectoryPoint()
            point.positions = angles
            point.time_from_start = rospy.Duration(duration)              
            goal.trajectory.points.append(point)
            self.jta.send_goal_and_wait(goal)

def main():
    print("Start of the trajectory file")
    arm = Joint('f_arm')
    arr_ref = [     3.048019825528769,  1.915942004069166,  3.5619033894704586,     0.2945243112740431,     -2.383806144374286,     2.710544052193928,  0.5460971604872883,     3.667748063834568,  2.8440003807399785,     2.82252464970958]
    arm.move_joint(arr_ref)


    #for i in range(0,4):
    #print(str(i) + 'th step started')
    print(angles_mat[199])

    angles_mat[199]*=-1
    
    arr_temp = np.add(arr_ref, angles_mat[199])
    print(arr_temp)
    # print(arr_temp)
    # print(angles_mat[0]) 
    arm.move_joint(arr_temp)
    # #print(str(i) +'th step completed')

if __name__ == '__main__':
    rospy.init_node('trajectory_client')
    main()
    print("End of the Trajectory file")
