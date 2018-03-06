#include <ros/ros.h>
#include <image_transport/image_transport.h>
//the above is a message type built into ROS to pass around images

int main(int argc, char **argv)
{
	ros::init(argc, argv, "noopencv_publisher");

	ros::NodeHandle nh; //main access point for communication
	image_transport::ImageTransport it(nh);
	image_transport::Publisher pub = it.advertise("cb_img",1); //tells the master that we are going to publish on the topic cb_img

    //initialising the image which needs to be generated
	sensor_msgs::Image gen_image; //naming it generated_image
	gen_image.header.stamp     = ros::Time::now();
	gen_image.height           = 1024;
	gen_image.width            = 1024;
	gen_image.encoding         = "mono8";
	gen_image.is_bigendian     = false;
	gen_image.step             = 1024;
	int flag = 0; 
	int blockWidth = gen_image.width/8;
	int blockHeight = gen_image.height/8;
	for(int i=0; i<gen_image.height;i++)
	{
		for(int b=0; b<8;b++)
		{
			for(int j=0;j<blockWidth;j++)
			{
				if(flag == 0)
	    	   		gen_image.data.push_back(0);
	  			if(flag == 1)
	    			gen_image.data.push_back(255);
	    	}
	    	if(flag)	
	    		flag = 0;
	    	else
	    		flag = 1;
	    }
	    if((i%blockHeight==0))
	    {
	    if(flag)	
	   		flag = 0;
	    else
	   		flag = 1;
	    }
	}
	ROS_INFO("Generated Image completely");
  	//image_publisher.publish(output_image);

	int frequency = 10;
	ros::Rate loop_rate(frequency);
	while(nh.ok()){
		pub.publish(gen_image);
		ros::spinOnce();
		loop_rate.sleep();
	}
}
