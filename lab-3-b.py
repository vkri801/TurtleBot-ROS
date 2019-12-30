import rospy
from geometry_msgs.msg import Twist

class PhotoTaker():
    def __init__(self):
        # initiliaze
        rospy.init_node('PhotoTaker', anonymous=False)
        rospy.on_shutdown(self.shutdown)

        # tell user how to stop TurtleBot
        rospy.loginfo("To stop TurtleBot CTRL + C")
        count = 0

        # loop ten times, or until the user presses Ctrl-C
        while count < 10 and not rospy.is_shutdown():
            count += 1
            print 'Performing loop %d' % (count, )
            self.move_forward()

            # Wait for the robot to move into the correct position
            rospy.sleep(5)  
            self.take_photo()
            if not rospy.is_shutdown():
                self.move_backwards()
                # Wait for the robot to move into the correct position
                rospy.sleep(5)  
                self.take_photo()

        rospy.loginfo('All done')

    def move_forward(self):
        print 'Moving forward'

    def move_backwards(self):
        print 'Moving backwards'

    def take_photo(self):
        print 'Taking photo'
                        
    def shutdown(self):
        # stop turtlebot
        rospy.loginfo("Stop TurtleBot")
	    
        # sleep just makes sure TurtleBot receives the stop command prior to shutting down the script
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        PhotoTaker()
    except:
        rospy.loginfo("PhotoTaker node terminated.")
