from unittest import TestCase
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_testing.actions import ReadyToTest
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
import launch_testing


def generate_test_description():

    launch_file_sim = PathJoinSubstitution(
        [FindPackageShare("dynaarm_description"), "launch", "view.launch.py"]
    )
    return (
        LaunchDescription(
            [
                IncludeLaunchDescription(PythonLaunchDescriptionSource(launch_file_sim)),
                # Notify when ready
                ReadyToTest(),
            ]
        ),
        {},
    )


class TestNodesRunning(TestCase):
    def test_nodes_started(self):
        assert True


if __name__ == "__main__":
    launch_testing.main()
