import rclpy
from rclpy.node import Node
import random
class robot_node(Node):
    def __init__(self,temp,humditiy,pressure):
        super().__init__("task5_2")
        self.temp=temp
        self.humditiy=humditiy
        self.pressure=pressure
        self.create_timer(1,self.timer_callback)

    def timer_callback(self):
         self.get_logger().info(" temp ="+ str(self.temp) + " humdidity= " + str(self.humditiy) +" pressure ="+ str(self.pressure))
   

def main(args=None):
    rclpy.init(args=args)
    # node=Node("py_node")
    # node.get_logger().info("hello world")
    temp = 100*random.random()
    humidity = 100*random.random()
    pressure = 100*random.random()
    node=robot_node(temp,humidity,pressure)
    
    rclpy.spin(node)
    rclpy.shutdown()



if __name__=="__main__":
    main()