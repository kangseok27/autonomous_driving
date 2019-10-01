cmake_minimum_required(VERSION 2.8.3)
project(patrolbot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
)

catkin_python_setup()

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES patrolbot
#  DEPENDS system_lib
  CATKIN_DEPENDS
    roscpp
    rospy
    std_msgs
    geometry_msgs
)

###########
## Build ##
###########

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

catkin_install_python(PROGRAMS 
  node/main_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch maps param rviz
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

