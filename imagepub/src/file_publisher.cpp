#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>

// image_transport/image_transport.h includes everything we need to publish and subscribe to images. 
// These headers will allow us to load an image using OpenCV and convert it to the ROS message format. 

int main(int argc, char** argv)
{
  ros::init(argc, argv, "image_publisher");
  
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
  //we create an image transport instance, initialising it with our NodeHandle.
  
  image_transport::Publisher pub = it.advertise("camera/image", 1);
  //we are going to publish on the base topic "camera/image", second argument is size of our publishing queue

  cv::Mat image = cv::imread(argv[1], CV_LOAD_IMAGE_COLOR);
  cv::waitKey(30);
  sensor_msgs::ImagePtr msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();
  //loading the image using Opencv function, and then converting it to ROS type of messages
  ros::Rate loop_rate(5);
  while (nh.ok()) {
    pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
  }
  //publishing as in any other publisher node
}