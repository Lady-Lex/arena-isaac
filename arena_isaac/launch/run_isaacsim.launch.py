import launch
from arena_bringup.substitutions import LaunchArgument
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import EnvironmentVariable, PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import ExecutableInPackage


def generate_launch_description():
    ld = []
    LaunchArgument.auto_append(ld)

    logger = LaunchArgument(
        name='log_level',
        default_value='debug',
        description='Logging level',
    )

    run_isaacsim_path = ExecutableInPackage(
        executable='run_isaacsim',
        package='arena_isaac',
    )

    return LaunchDescription([
        *ld,
        launch.actions.DeclareLaunchArgument(
            "log_level",
            default_value=["debug"],
            description="Logging level",
        ),
        SetEnvironmentVariable(
            name='ARENA_WORLD_NAME',
            value=LaunchConfiguration('world'),
        ),
        ExecuteProcess(
            cmd=[
                PathJoinSubstitution([EnvironmentVariable('ISAAC_PATH'), 'python.sh']),
                run_isaacsim_path,
                '--log-level', logger.substitution
            ],
            output='log',
        ),
    ])
