
#Quick script to generate the urdf, since doing it by hand would be insane.

width = 16
height = 16

col_pos = [-0.425, -0.365, -0.305, -0.245, -0.185, -0.125, -0.065, -0.005, 0.055, 0.115, 0.175, 0.235, 0.295, 0.355, 0.415, 0.475]
row_pos = [0.45, 0.39, 0.33, 0.27, 0.21, 0.15, 0.09, 0.03, -0.03, -0.09, -0.15, -0.21, -0.27, -0.33, -0.39, -0.45]
col = [i for i in range(1,width+1)]
row = [i for i in range(1,height+1)]

f= open("../urdf/pixelbot.urdf","w+")


f.write('''<?xml version="1.0" encoding="utf-8"?>
<!-- This URDF was automatically created by SolidWorks to URDF Exporter! Originally created by Stephen Brawner (brawner@gmail.com) 
     Commit Version: 1.6.0-1-g15f4949  Build Version: 1.6.7594.29634
     For more information, please see http://wiki.ros.org/sw_urdf_exporter -->
<robot
  name="pixelbot">
  <link name="dummy">
   </link>
    <joint name="dummy_joint" type="fixed">
     <parent link="dummy"/>
     <child link="base_link"/>
   </joint>
  <link
    name="base_link">
    <inertial>
      <origin
        xyz="-8.2294E-15 -0.005 -4.5605E-16"
        rpy="0 0 0" />
      <mass
        value="3.5372" />
      <inertia
        ixx="0.33762"
        ixy="-3.5168E-19"
        ixz="-5.004E-15"
        iyy="0.67309"
        iyz="-2.1066E-17"
        izz="0.33553" />
    </inertial>
    <visual>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://pixelbot/meshes/base_link.STL" />
      </geometry>
      <material
        name="">
        <color
          rgba="0.79216 0.81961 0.93333 1" />
      </material>
    </visual>
    <collision>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://pixelbot/meshes/base_link.STL" />
      </geometry>
    </collision>
  </link>''')


for i in row:
    for j in col:
        f.write('''<link
    name="{0}-{1}">
    <inertial>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <mass
        value="0.024018" />
      <inertia
        ixx="5.4136E-06"
        ixy="-2.2058E-23"
        ixz="-4.1359E-24"
        iyy="5.2106E-06"
        iyz="9.099E-23"
        izz="1.0211E-05" />
    </inertial>
    <visual>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://pixelbot/meshes/w11.STL" />
      </geometry>
      <material
        name="">
        <color
          rgba="0.79216 0.81961 0.93333 1" />
      </material>
    </visual>
    <collision>
      <origin
        xyz="0 0 0"
        rpy="0 0 0" />
      <geometry>
        <mesh
          filename="package://pixelbot/meshes/w11.STL" />
      </geometry>
    </collision>
  </link>
  <joint
    name="{0}-{1}"
    type="revolute">
    <origin
      xyz="{2} -0.005 {3}"
      rpy="1.5708 0 0" />
    <parent
      link="base_link" />
    <child
      link="{0}-{1}" />
    <axis
      xyz="1 0 0" />
    <limit
      lower="-6"
      upper="6"
      effort="0"
      velocity="0" />
  </joint>'''.format(i, j, col_pos[j-1], row_pos[i-1] ))


f.write("</robot>")
f.close()  