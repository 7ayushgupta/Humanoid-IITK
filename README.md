# ROS Tutorials

Before executing the bash files
`source /opt/ros/kinetic/setup.bash`

### Nodes
A node really isn't much more than an executable file within a ROS
package. ROS nodes use a ROS client library to communicate with other
nodes. Nodes can publish or subscribe to a Topic. Nodes can also provide
or use a Service.

`rosnode list` and `rosnode info` are commands used to get info about
rosnode

__Renaming Nodes in real time___
`$ rosrun turtlesim turtlesim_node __name:=my_turtle`

`rosnode list` and `rosnode cleanup` are required to remove data about
the existing nodes

We use rqt_graph for plotting the ROS Structure

### ROS Topics
The turtlesim_node and the turtle_teleop_key node are communicating with
each other over a ROS Topic. turtle_teleop_key is publishing the key
strokes on a topic, while turtlesim subscribes to the same topic to
receive the key strokes.

### ROS Messages
Communication on topics happens by sending ROS messages between nodes.
For the publisher (turtle_teleop_key) and subscriber (turtlesim_node) to
communicate, the publisher and subscriber must send and receive the same
type of message. This means that a topic type is defined by the message
type published on it. The type of the message sent on a topic can be
determined using rostopic type.


__Controlling turtle by publishing data__
You may have noticed that the turtle has stopped moving; this is because
the turtle requires a steady stream of commands at 1 Hz to keep moving.
We can publish a steady stream of commands using rostopic pub -r
command:

For ROS Hydro and later,
`rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0,
0.0]' '[0.0, 0.0, -1.8]''`

### ROS Services
Services are another way that nodes can communicate with each other.
Services allow nodes to send a request and receive a response.

### ROS Actionlib Client
TODO

__ERROR while using mixcell__
Use sudo to run the application.

