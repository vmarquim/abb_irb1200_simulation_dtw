# abb_irb1200_simulation_dtw
Gazebo Simulation with Moveit Controls in Rviz and DTW Plot comparing simulated and theoretical trajectory

1. Install ROS Noetic [Tutorial here](https://wiki.ros.org/noetic/Installation/Ubuntu)

2. Install Moveit [Tutorial here](https://moveit.ros.org/install/)
```
sudo apt install ros-noetic-moveit
```

3. Install Pandas, NumPy and DTW
```
pip install pandas dtw-python numpy
```

4. To start the Robot Simulation in Gazebo and the RViz with Moveit, Run the simulation launch file
```
roslaunch abb_irb1200_simulation_dtw simulation_dtw_program.launch
```

5. Run the run and compare launch file
```
roslaunch abb_irb1200_simulation_dtw run_and_compare.launch --mode
```

6. Flags
```
--square
--circle
--random-valid
```
