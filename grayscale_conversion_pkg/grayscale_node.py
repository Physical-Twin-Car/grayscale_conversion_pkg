import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class GrayscaleNode(Node):
    def __init__(self):
        super().__init__('grayscale_node')

        # convert OpenCV naar ROS images
        self.bridge = CvBridge()

        self.camera_subscription = self.create_subscription(Image, '/camera/front', self.image_callback, 10)
        self.grayscale_publisher = self.create_publisher(Image, '/camera/image_grayscale', 10)

    def image_callback(self, msg):
        # conversie van de image naar OpenCV
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        # maak er een grayscale image van
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # convsersie terug naar ROS image
        grayscale_msg = self.bridge.cv2_to_imgmsg(grayscale_frame, 'mono8')

        self.grayscale_publisher.publish(grayscale_msg)

def main(args=None):
    rclpy.init(args=args)
    node = GrayscaleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
