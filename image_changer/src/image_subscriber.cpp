#include <ros/ros.h>
#include <image_transport/image_transport.h>

void imageCallback(const sensor_msgs::ImageConstPtr& input_image)
{
		int b = 1;
		int c = 1;
		sensor_msgs::Image new_image;

		new_image.header.stamp     = ros::Time::now();
		new_image.height           = input_image->height;
		new_image.width            = input_image->width;
		new_image.encoding         = input_image->encoding;
		new_image.is_bigendian     = input_image->is_bigendian;
		new_image.step             = input_image->step;

		for(int i=0; i<new_image.width*new_image.height;i++)
			new_image.data[i]=b*input_image->data[i]+c;
}




int main(int argc, char **argv)
{
	ros::init(argc, argv, "image_listener");
	ros::NodeHandle nh;
	image_transport::ImageTransport it(nh);
	image_transport::Subscriber sub = it.subscribe("camera/image",1, imageCallback);
	ros::spin();
}

