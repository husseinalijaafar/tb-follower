from setuptools import setup
from glob import glob
import os

package_name = 'learning_tf2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hussein',
    maintainer_email='husseinali.jaafar@ryerson.ca',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'turtlebot_tf2_target_broadcaster = learning_tf2_py.turtlebot_tf2_target_broadcaster:main',
        'turtlebot_tf2_target_listener = learning_tf2_py.turtlebot_tf2_target_listener:main',
        ],
    },
)
