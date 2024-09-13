#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class robot_node(Node):
    def __init__(self,x,res):
        super().__init__("Task5_1")
        self.res=self.checker(x)
        self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
         self.get_logger().info(self.res)
    def checker(self,x):
        if(x%2==0):
            return "number is even"
        else:
            return "number is odd"

def main(args=None):
    rclpy.init(args=args)
    # node=Node("py_node")
    # node.get_logger().info("hello world")
    node=robot_node(20,"")
    
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=="__main__":
    main()