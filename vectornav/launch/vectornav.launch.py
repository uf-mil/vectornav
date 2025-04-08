import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    this_dir = get_package_share_directory('vectornav')
    
    # Vectornav
    start_vectornav_cmd = Node(
        package='vectornav', 
        executable='vectornav',
        output='screen',
        remappings=[
            ('/vectornav/raw/attitude', '/vectornav/_'),
            ('/vectornav/raw/common', '/vectornav/_'),
            ('/vectornav/raw/gps', '/vectornav/_'),
            ('/vectornav/raw/gps2', '/vectornav/_'),
            ('/vectornav/raw/imu', '/vectornav/_'),
            ('/vectornav/raw/ins', '/vectornav/_'),
            ('/vectornav/raw/time', '/vectornav/_'),
            ('/vectornav/velocity_aiding', '/vectornav/_'),
        ],
        parameters=[os.path.join(this_dir, 'config', 'vectornav.yaml')])
    
    start_vectornav_sensor_msgs_cmd = Node(
        package='vectornav', 
        executable='vn_sensor_msgs',
        output='screen',
        remappings=[
            # remap these two topics
            ('/vectornav/imu', '/imu/data'),
            ('/vectornav/magnetic', '/imu/mag_raw'),
            # hide all others (unused)
            ('/vectornav/gnss', '/vectornav/_'),
            ('/vectornav/imu_uncompensated', '/vectornav/_'),
            ('/vectornav/pose', '/vectornav/_'),
            ('/vectornav/pressure', '/vectornav/_'),
            ('/vectornav/raw/attitude', '/vectornav/_'),
            ('/vectornav/raw/common', '/vectornav/_'),
            ('/vectornav/raw/gps', '/vectornav/_'),
            ('/vectornav/raw/gps2', '/vectornav/_'),
            ('/vectornav/raw/imu', '/vectornav/_'),
            ('/vectornav/raw/ins', '/vectornav/_'),
            ('/vectornav/raw/time', '/vectornav/_'),
            ('/vectornav/temperature', '/vectornav/_'),
            ('/vectornav/time_gps', '/vectornav/_'),
            ('/vectornav/time_pps', '/vectornav/_'),
            ('/vectornav/time_startup', '/vectornav/_'),
            ('/vectornav/time_syncin', '/vectornav/_'),
            ('/vectornav/velocity_aiding', '/vectornav/_'),
            ('/vectornav/velocity_body', '/vectornav/_'),
        ],
        parameters=[os.path.join(this_dir, 'config', 'vectornav.yaml')])

    # Create the launch description and populate
    ld = LaunchDescription()

    ld.add_action(start_vectornav_cmd)
    ld.add_action(start_vectornav_sensor_msgs_cmd)

    return ld
