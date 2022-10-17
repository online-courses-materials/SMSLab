from setuptools import setup

package_name = 'learning_tf2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cvlab',
    maintainer_email='sardor@inha.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',
        ],
    },
)
