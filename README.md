# TurtleBot-ROS
All Python code snippets used to test out the Turtlebot.

Enter into terminal. 

roslaunch turtlebot_bringup minimal.launch
roslaunch turtlebot_navigation gmapping_demo.launch
roslaunch turtlebot_rviz_launchers view_navigation.launch
roslaunch turtlebot_teleop keyboard_teleop.launch

Brings up RVIZ and manual control for bot. After finishing, enter into terminal:

rosrun map_server map_saver -f /tmp/my_map
ls /tmp/

roslaunch turtlebot_bringup minimal.launch
roslaunch turtlebot_navigation amcl_demo.launch map_file:=/tmp/my_map.yaml
roslaunch turtlebot_rviz_launchers view_navigation.launch -- screen
