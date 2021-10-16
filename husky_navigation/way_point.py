#!/usr/bin/env python3
# license removed for brevity

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(goal):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()


    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        for x in [-2,-4]:
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = x
            goal.target_pose.pose.orientation.w = 1.0
            result = movebase_client(goal)
            if result:
                rospy.loginfo("Goal execution done!")
                continue
            else:
                rospy.loginfo(f"Error: {x}")
                break
		        	
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

