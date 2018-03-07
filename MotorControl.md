# Controlling Servos with ROS, and Mixcell


__NOTE:__ _If having error while using Mixcell, to connect to motor._
For using correctly in Joint mode, we need to set the CCW Angle limit to 4095, it can be set to anywhere actually. Basically, the motor stops after reaching that limit so, need to make sure it is huge. We can make the motor go in the backward direction also.

__tilt.yaml__ is a file which contains the ROS parameters. This is done so that we can change the basic variables everywhere (like global values) without having to change them in each program. We make a seperate file for the parameters in yaml format.

~~~
<node name="tilt_controller_spawner" pkg="dynamixel_controllers" type="controller_spawner.py"
          args="--manager=dxl_manager
                --port pan_tilt_port
                tilt_controller"
          output="screen"/>
~~~
As far as I can understand, this is equivalent to launching a rosnode _tilt_controller_spawner_ (much like CMakeList), and the arguments passed are given here.

~~~
rostopic pub -1 /tilt_controller/command std_msgs/Float64 -- 1.5
~~~
Here, we publish a message to the tilt_controller/command topic which basically is the recieving point (learn about topics :P)


For two motors:
~~~
dual_motor_controller:
    controller:
        package: dynamixel_controllers
        module: joint_position_controller_dual_motor
        type: JointPositionControllerDual
    joint_name: dual_motor
    joint_speed: 1.17
    motor_master:
        id: 7
        init: 0
        min: -2047
        max: 2047
    motor_slave:
        id: 15
~~~
Here, we are writing the parameters which will be used by the controller files. Easy enough to understand. The motor_master and motor_slave are nothing very special but just two different names for the motors.

We create a launch file like in the previous example.
~~~
<launch>
    <!-- Start dual_motor joint controller -->
    <rosparam file="$(find my_dynamixel_tutorial)/dual_motor.yaml" command="load"/>
    <node name="dual_motor_controller_spawner" pkg="dynamixel_controllers" type="controller_spawner.py"
          args="--manager=dxl_manager
                --port your_dynamixel_usb_port
                dual_motor_controller"
          output="screen"/>
</launch>
~~~