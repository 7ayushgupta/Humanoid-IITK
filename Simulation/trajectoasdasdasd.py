#!/usr/bin/env python
import roslib
roslib.load_manifest('my_dynamixel_tutorial')

import rospy
import actionlib
from std_msgs.msg import Float64
import trajectory_msgs.msg 
import control_msgs.msg  
from trajectory_msgs.msg import JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryAction, JointTrajectoryGoal, FollowJointTrajectoryAction, FollowJointTrajectoryGoal

duration = 0.6

class Joint:
        def __init__(self, motor_name):
            #arm_name should be b_arm or f_arm
            	self.name = motor_name   
		print(motor_name)        
		self.jta = actionlib.SimpleActionClient('/'+self.name+'_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
		rospy.loginfo('Waiting for joint trajectory action')
		self.jta.wait_for_server()
		rospy.loginfo('Found joint trajectory action!')

            
        def move_joint(self, angles):
            goal = FollowJointTrajectoryGoal()                  
            char = self.name[0] #either 'f' or 'b'
            goal.trajectory.joint_names = ['motor8', 'motor9','motor10','motor11','motor12','motor13','motor14','motor15','motor16','motor17']
            point = JointTrajectoryPoint()
            point.positions = angles
            point.time_from_start = rospy.Duration(duration)              
            goal.trajectory.points.append(point)
            self.jta.send_goal_and_wait(goal)
              

def main():
		arm = Joint('f_arm')
		arm.move_joint([3.2597091742569875, 	2.9253013624979176, 	3.6386024288647407, 	0.1536896448593132, 	-2.167514853282411, 	2.5709518004963345, 	0.2561747915769021, 	3.377825694924182, 	2.1475731030398975, 	3.3164664634087564])
		#arm.move_joint([2.9099615546190614, 	2.9038256314675186, 	3.4944082348034904, 	0.44485442848683593, 	-2.1475731030398975, 	2.5494760694659355, 	0.5031456984264903, 	3.2949907323783574, 	2.0969517370396713, 	3.3011266555298997])
		#arm.move_joint([3.060291671831854,2.6491848206785025,3.5419616392279454,0.320601984668099,-2.1475731030398975,2.7596314374062683,0.3021942152134713,3.5465635815916023,2.457437222192797,3.083301383650139])
		#arm.move_joint([3.060291671831854,2.6491848206785025,3.5419616392279454,0.320601984668099,-2.1475731030398975,2.7596314374062683,0.3021942152134713,3.5465635815916023,2.457437222192797,3.083301383650139])




print("Hello1")

                        
if __name__ == '__main__':
	rospy.init_node('trajectory_client')
	main()
	print("Hello")

