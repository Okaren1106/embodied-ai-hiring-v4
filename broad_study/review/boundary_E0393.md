## E0393 US_APPTRONIK RF_HARDWARE_ELECTRICAL Senior Electrical Engineer - Sensor FPGA and PCB (Aggregator)
TASK FPGA SENSOR_BRIDGE_FPGA_BOARD_SUBSYSTEM_EXECUTION
REVIEW ["UNKNOWN", "DERIVED_CONTEXT_OR_OBJECT_CORRECTION", "CATALOG_BOUNDARY"]
SCOPE BOUNDARY_CONTEXTS: all coded/candidate clauses + adjacent lines + visible headings; omitted lines are not certified read.
F1 [原字节同已全文复读 E0402:full_description:1] Apptronik is a human-centered  … he home, and beyond.
F2 [原字节同已全文复读 E0402:full_description:2] We operate at the cutting edge … orld for the better.
F3 JOB SUMMARY
F4 We're looking for a Senior Electrical Engineer to help design and build the electronics for Apollo's sensor bridge. Strong candidates will have experience with FPGA hardware for both PCBA design and RTL development. This role works closely with the perception team to give Apollo sight and enable critical safety functions. You'll take direct, hands-on ownership of defined subsystems within the board — schematic capture, layout guidance, and RTL blocks — executing against an architecture defined in partnership with the team's Staff and/or Principal engineers.
F5 ESSENTIAL DUTIES AND RESPONSIBILITIES or KEY ACCOUNTABILITIES
F6 Electronics & FPGA Design Execution:
F7 Contribute to requirements definition and own part selection, schematic capture, layout guidance, and RTL implementation for assigned subsystems of a multi-Gbps, mixed-signal PCBA that aggregates camera sensor data and human-robot interface functions into an efficient cable interface routed across dynamic joints. Carry the design through prototype, validation, and manufacturing release, in coordination with the engineer(s) owning overall board architecture. Generate and maintain design documentation including: schematics, RTL documentation, test plans, and fab/assembly drawings.
F8 High-Speed & Mixed-Signal Hardware Design:
F9 Design and validate high-speed digital interfaces (CSI-2, GMSL2/FPD-Link/PoC, 10GbE) including signal integrity, impedance control, and length-matching. Contribute to the board's power tree design for proper power sequencing and low-power consumption. Design for EMC, ESD, and thermal constraints.
F10 FPGA RTL Development:
F11 Develop RTL (VHDL/Verilog) for CSI-2 ingest, Ethernet packetization, timestamp/metadata insertion, and camera synchronization logic for deterministic multi-camera and multi-IMU synchronization, working within an FPGA architecture defined collaboratively with senior technical staff. Support timing closure, clock-domain crossing, and resource/power budgeting for your RTL blocks. Assist with integration of high-speed transceivers and external PHYs.
F12 Validation, Bring-Up, and Debugging:
F13 Develop and execute validation plans for your assigned subsystems, spanning board-level and FPGA-level testing. Build test fixtures and use lab equipment (high-bandwidth oscilloscopes, protocol analyzers, logic analyzers) to validate latency, bandwidth, and synchronization requirements. Debug across the hardware/RTL boundary — link training failures, timing violations, ISP misconfiguration, power sequencing faults — using rigorous, first-principles root-cause analysis, escalating and collaborating with technical leads on cross-subsystem issues.
F14 Lifecycle Management & Vendor Alignment:
F15 Support the entire component lifecycle through PLM systems, managing third-party relationships with hardware vendors and contract manufacturers (CMs) to ensure successful production scaling and design-for-manufacturability (DFM/DFA).
F16 Cross-Functional Collaboration:
F17 Collaborate closely with cross-functional teams, including technical lead, project managers, software, mechanical, thermal, systems engineers, and manufacturing. Act as a mentor within the electrical engineering team, guiding junior engineers on best practices for hardware design, documentation, and troubleshooting.
F18 Technical Execution:
F19 Execute assigned work streams reliably and communicate progress clearly to technical leads and program management. Contribute to design reviews and root-cause analysis for hardware and software defect resolution within your scope. Provide work breakdowns and time estimates for your own work to inform project execution, and raise design or schedule risks proactively.
F20 SKILLS AND REQUIREMENTS
F21 Experience in FPGA hardware design for time-sensitive, high-performance applications (image processing, high-speed data acquisition, real-time networking, or similar), including:
F22 FPGA device selection and architecture definition
F23 RTL development in VHDL and/or Verilog
F24 High-speed interface design (CSI-2, GMSL/SerDes, Ethernet, PCIe, or comparable)
F25 Timing closure, clock-domain crossing, and resource optimization
F26 Integration of high-speed transceivers and external PHY devices
F27 FPGA tool flows (Vivado, Quartus, or Lattice Radiant) and simulation (ModelSim/Questa or equivalent)
F28 Understanding of high-speed digital design fundamentals: signal integrity, impedance-controlled routing, differential pairs, stack-up, and timing analysis across the board-to-FPGA boundary.
F29 Experience with camera/image sensor hardware: SerDes (GMSL, FPD-Link, or similar), MIPI CSI-2, and ISP integration — automotive or robotics vision systems strongly preferred.
F30 Experience with Ethernet-based sensor streaming and sensor bridges.
F31 [原字节同已全文复读 E0374:full_description:18] Excellent communication (verba … ctions and diagrams.
F32 Excellent problem-solving and hardware debugging skills. Hands-on experience with prototyping and testing, including the use of lab equipment.
F33 Ability to thrive in a fast-paced, high-growth environment where "perfect" is the enemy of "shipped," knowing exactly when a design is robust enough for the real world.
[未在本包显示 F34,F35,F36]
F37 At least 5 years of experience in Electrical Engineering.
F38 PHYSICAL REQUIREMENTS
F39 Prolonged periods of sitting at a desk and working on a computer
[未在本包显示 F40,F41,F42,F43,F44,R23]
EV E0393:O1 SK_PCB DUTY_OWN_DEVELOP/UNCONDITIONAL @F7
EV E0393:O2 SK_OSCILLOSCOPE DUTY_OWN_USE/UNCONDITIONAL @F13
EV E0393:O3 SK_LOGIC_ANALYZER DUTY_OWN_USE/UNCONDITIONAL @F13
EV E0393:O4 SK_PCB GENERAL/UNCONDITIONAL @F4
EV E0393:O5 TC_SAFETY SEPARATE/UNRESOLVED @F2
EV E0393:O6 TC_PERCEPTION SEPARATE/UNCONDITIONAL @F4
EV E0393:O7 TC_SAFETY SEPARATE/COLLABORATION_OBJECT @F4
EV E0393:O8 TC_POWER_ELECTRONICS SEPARATE/COLLABORATION_OBJECT @F9
EV E0393:O9 TC_THERMAL_MANAGEMENT SEPARATE/BACKGROUND @F9
EV E0393:O10 TC_EVALUATION DUTY_OWN_DEVELOP/UNCONDITIONAL @F13
EV E0393:O11 TC_REALTIME GENERAL/CHOICE @F21
EV E0393:O12 TC_SIMULATION GENERAL/EXAMPLE @F27
EV E0393:O13 TC_EVALUATION GENERAL/UNCONDITIONAL @F32
EV E0393:1:0 V2_EMC_SIPI DUTY_OWN_USE/UNCONDITIONAL @F9
EV E0393:2:0 V2_ETHERNET DUTY_OWN_USE/UNCONDITIONAL @F11
EV E0393:3:0 V2_PLM SEPARATE/COLLABORATION_OBJECT @F15
EV E0393:3:1 V2_DFM SEPARATE/COLLABORATION_OBJECT @F15
EV E0393:5:0 V2_PROJECT_METHOD DUTY_OWN_USE/UNCONDITIONAL @F19
EV E0393:6:0 V2_ETHERNET GENERAL/CHOICE_AND_EXAMPLE @F24
EV E0393:6:1 V2_GMSL GENERAL/UNRESOLVED @F24
EV E0393:7:0 V2_EMC_SIPI GENERAL/UNCONDITIONAL @F28
EV E0393:8:0 V2_GMSL GENERAL/CHOICE @F29
EV E0393:9:0 V2_ETHERNET GENERAL/UNCONDITIONAL @F30
EV E0393:ADD1 TC_EVALUATION DUTY_OWN_USE/UNCONDITIONAL @F13
EV E0393:ADD2 V2_SOP_OPERATION DUTY_OWN_DEVELOP/UNCONDITIONAL @F31
EV E0393:ADD3 V2_REQUIREMENTS_ENGINEERING SEPARATE/COLLABORATION_OBJECT @F7
CAND E0393:4 REJECT:project managers是协作对象而非MS Project软件；开发调试不计运行服务。 @F17
CAND E0393:10 OUTSIDE:RTL/VHDL/Verilog明确开发内容，冻结硬件细目录缺项。 @F11
CAND E0393:11 OUTSIDE:protocol analyzers协议分析仪细项未覆盖。 @F13
CAND E0393:12 OUTSIDE:Vivado、Quartus、Lattice Radiant在including下是任选工具，目录缺细项。 @F27
CAND E0393:13 OUTSIDE:ModelSim/Questa or equivalent为仿真工具关系，目录未覆盖。 @F27
OLD_NOTES Senior子系统直接设计明确，不因help/collaborate的总体介绍否定该具体责任；电源架构、需求定义仍是Contribute协作。