## N0827 US_FIELD_AI RF_SYSTEMS_ENGINEERING_INTEGRATION Senior Sensor & Perception Engineer, Robotics Hardware
TASK SUBSYSTEM SENSOR
REVIEW ["UNKNOWN", "CATALOG_BOUNDARY"]
SCOPE BOUNDARY_CONTEXTS: all coded/candidate clauses + adjacent lines + visible headings; omitted lines are not certified read.
F1 [原字节同已全文复读 N0799:full_description:1] FieldAI’s Irvine team is where … ts run in the field.
F4 Hardware Team:
F5 The Hardware Team at Field AI develops perception and compute payloads that power autonomous robotics systems in complex real-world environments. Our work spans the full hardware stack designing and integrating sensing systems (LiDAR, camera, TOF, IMU, GPS), embedded compute (CPUs, GPUs, microcontrollers, ROS, sensor drivers), electrical systems (power distribution, communication), and mechanical components (structures, thermal regulation, ingress protection). The team focuses on both development (research, design, prototyping, testing) and operations (production, testing, QA, debugging). We’re a small, fast-moving team, and we care deeply about improving: 1) core capabilities, 2) system reliability, 3) system scalability. As a growing team we are also building operational systems and procedures from the ground up.
F7 Sensor Systems Role:
F8 As a Sensor Systems Engineer on the Hardware Team, you will contribute to the design, integration, calibration, and validation of the sensing systems that underpin our autonomy stack. You will work with a diverse array of sensors—LiDARs, depth cameras, IMUs, GPS, and more—ensuring each one delivers accurate, time-synchronized, and spatially consistent data in a range of environments and operating conditions. You will collaborate closely with the autonomy, compute, electrical, and mechanical teams to build tightly integrated solutions ready for deployment in challenging field environments. Additionally, while your focus will be on sensors you will likely contribute across all hardware domains.
F11 What You Will Get To Do
[未在本包显示 F14]
F15 Sensor Architecture: Work across hardware and software teams to define sensing requirements. Identity, test, and select sensors such as LiDARs, depth cameras, GPS, IMUs, ToF, and other devices.
F16 Systems Integration: Integrate sensors with electrical (USB, Ethernet, I2C, CAN, GMSL), mechanical (mounts, jigs, isolation), and software (configurations, drivers, ROS nodes) systems. Ensuring power, thermal, and protocol compatibility.
F17 Spatial Performance: Architect system to meet spatial sampling performance requirements including spatial coverage, range, resolution, and transform accuracy.
[未在本包显示 F18]
F20 2. Sensor System Implementation
F21 Performance Characterization: Evaluate sensor performance (spatial resolution, temporal drift, EMI noise, sync errors etc.). Test under real-world environmental conditions (vibration, lighting, moisture, temperature).
F22 Calibration: Design and execute both intrinsic and extrinsic calibrations. Build alignment rigs and calibration boards as needed.
F23 Optimization: Tune sensor configurations (exposure, gain, filtering, frame rate, etc.) and processing pipeline (filtering etc.)  for optimal performance
[未在本包显示 F24]
F26 3. Sensor System Production & Servicing
F27 Build: Work with vendors to procure sensors. Develop QA checks for incoming units. Support payload integration and manufacturing at scale.
F28 Debug: Conduct root cause analysis of sensor systems including issues across hardware and software boundaries.
F29 Monitor: Develop protocols for monitoring the sensing system health, data quality, and calibration status during field deployments.
F31 What You Have
F33 Education: B.S., M.S. or Ph.D. in Robotics, Electrical Engineering, Engineering Physics, Physics, or a related field.
F34 [原字节同已全文复读 N0740:full_description:32] Experience Level: We are recru … and staff engineers.
F35 Hands-On Sensors Experience: Hands-on work with perception sensors such as LiDAR, depth cameras, IMUs, GPS.
F36 Systems Thinking: Cross-functional collaboration experience across electrical, mechanical, and software teams.
F37 Sensor Physics: Strong foundation in optics, signal processing, and electromagnetic wave propagation.
F38 Lab Skills: Hands-on testing, calibration, and debugging skills (oscilloscopes, logs, vibration/thermal setups)
F39 Communication Protocols: Experience with protocols such as USB, Ethernet, GMSL, CAN, I2C, and CSI.
F40 Computer & Software: Experience working with ROS/ROS2, sensor drivers, coordinate transforms (TF), and timing protocols (PTP, NTP, etc.).
F41 Timing & Triggers: Experience with timestamping, synchronization, triggering, and latency constraints.
F42 Calibration & Characterization: Experience designing and executing intrinsic, extrinsic, and temporal calibrations, along with sensor characterization under real-world environmental conditions.
F43 Simulation: Experience high-fidelity simulation environments (Gazebo, Isaac Sim, RViz) for sensor modeling.
F45 What Will Set You Apart
[未在本包显示 F51]
F53 Why Join FieldAI in Irvine?
F54 [原字节同已全文复读 N0799:full_description:47] In Irvine, you will work where …  for real-world use.
F55 [原字节同已全文复读 N0799:full_description:48] You will collaborate with a wo …  challenge segments.
[未在本包显示 F57,F58,F60,F62]
EV N0827:O1 SK_ROS SEPARATE/UNRESOLVED @F5
EV N0827:O2 SK_ROS DUTY_OWN_USE/UNCONDITIONAL @F16
EV N0827:O3 SK_OSCILLOSCOPE GENERAL/EXAMPLE @F38
EV N0827:O4 SK_ROS GENERAL/UNRESOLVED @F40
EV N0827:O5 SK_ROS2 GENERAL/UNRESOLVED @F40
EV N0827:O6 SK_GAZEBO GENERAL/EXAMPLE @F43
EV N0827:O7 SK_ISAAC GENERAL/EXAMPLE @F43
EV N0827:O8 TC_FOUNDATION_MODEL SEPARATE/UNRESOLVED @F54
EV N0827:O9 TC_PERCEPTION SEPARATE/UNRESOLVED @F54
EV N0827:O10 TC_SLAM SEPARATE/UNRESOLVED @F54
EV N0827:O11 TC_MANIPULATION SEPARATE/UNRESOLVED @F54
EV N0827:O12 TC_SAFETY SEPARATE/UNRESOLVED @F54
EV N0827:O13 TC_RELIABILITY SEPARATE/UNRESOLVED @F1
EV N0827:O14 TC_EMBEDDED SEPARATE/UNRESOLVED @F5
EV N0827:O15 TC_POWER_ELECTRONICS SEPARATE/UNRESOLVED @F5
EV N0827:O16 TC_MECHANICAL SEPARATE/UNRESOLVED @F5
EV N0827:O17 TC_THERMAL_MANAGEMENT SEPARATE/UNRESOLVED @F5
EV N0827:O18 TC_MECHANICAL DUTY_OWN_USE/UNCONDITIONAL @F16
EV N0827:O19 TC_EVALUATION DUTY_OWN_USE/UNCONDITIONAL @F21
EV N0827:O20 TC_RELIABILITY DUTY_OWN_USE/UNCONDITIONAL @F21
EV N0827:O21 TC_EVALUATION DUTY_OWN_DEVELOP/UNCONDITIONAL @F22
EV N0827:O22 TC_PERCEPTION GENERAL/UNCONDITIONAL @F35
EV N0827:O23 TC_EVALUATION GENERAL/UNCONDITIONAL @F38
EV N0827:O24 TC_RELIABILITY GENERAL/EXAMPLE @F38
EV N0827:O25 TC_EVALUATION GENERAL/UNCONDITIONAL @F42
EV N0827:O26 TC_SIMULATION GENERAL/UNCONDITIONAL @F43
EV N0827:O27 TC_EVALUATION DUTY_OWN_USE/UNCONDITIONAL @F22
EV N0827:O28 TC_EVALUATION DUTY_OWN_USE/UNCONDITIONAL @F27
EV N0827:1:0 V2_CALIBRATION DUTY_OWN_USE/UNCONDITIONAL @F8
EV N0827:2:0 V2_USB DUTY_OWN_USE/UNCONDITIONAL @F16
EV N0827:2:1 V2_ETHERNET DUTY_OWN_USE/UNCONDITIONAL @F16
EV N0827:2:2 V2_I2C DUTY_OWN_USE/UNCONDITIONAL @F16
EV N0827:2:3 V2_CAN DUTY_OWN_USE/UNCONDITIONAL @F16
EV N0827:2:4 V2_GMSL DUTY_OWN_USE/UNCONDITIONAL @F16
EV N0827:8:0 V2_EMC_SIPI DUTY_OWN_USE/UNCONDITIONAL @F21
EV N0827:9:0 V2_CALIBRATION DUTY_OWN_DEVELOP/UNCONDITIONAL @F22
EV N0827:10:0 V2_CALIBRATION DUTY_OWN_USE/UNCONDITIONAL @F29
EV N0827:12:0 V2_CALIBRATION GENERAL/UNCONDITIONAL @F38
EV N0827:20:0 V2_PTP GENERAL/UNCONDITIONAL @F40
EV N0827:20:1 V2_NTP GENERAL/UNCONDITIONAL @F40
EV N0827:24:0 V2_CALIBRATION GENERAL/UNCONDITIONAL @F42
EV N0827:25:0 V2_RVIZ GENERAL/CHOICE @F43
CAND N0827:11 REJECT:招募各年限工程师不是人力资源技能项。 @F34
CAND N0827:19 OUTSIDE:CSI未单列冻结项。 @F39
CAND N0827:21 OUTSIDE:TF坐标变换未单列冻结项。 @F40
OLD_NOTES 传感系统集成。标定/总线/PTP/RViz保留。