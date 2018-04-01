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
angles_mat = sio.loadmat('file.mat')
print(angles_mat.shape)
print(angles_mat.head)

#for using the ith row of a 2D array
i = 0
print(angles_mat[i,])

duration = 0.1

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
    for i in range(0,200):
        arm.move_joint(angles_mat[i,])
        print(str(i) +'th step completed')

if __name__ == '__main__':
    rospy.init_node('trajectory_client')
    main()
    print("End of the Trajectory file")
