# Hexasense API v0.1 - Hardware Implementation

## Design Intent

The intention of this hardware design is to provide a means of sensing the position of the actuators of the HEXA robot whilst maintaining the ability to fully revert the robot 
to it's original factory state.
<br>
Any instance where modification of the robot's hardware would be required, an appropriate 3D printed part has been designed to integrate in place of the original robot hardware.
<br>
It is also intended that the SBC component part of this system should function as an analogue for the HEXA robot to allow future integration of the Hexasense API software solution and ADC system 
directly with the HEXA robot itself, negating the need for the additional SBC hardware.
<br>


## Hardware Description

The hardware implementation to add a proprioceptive sensing system to the HEXA Robot can be described as having three component parts to it's structure.
<br>
- A "Digital Twin" Data Processing & Relay System - Comprising of an off-the-shelf Raspberry Pi 4B SBC
- An Analogue To Digital Sensing & Conversion System - Comprising of a series of potentiometers mechanically coupled to the robot's actuators and an off-the-shelf ADC printed circuit board interfaced with the Data Processing & Relay System using the I2C protocol
- The Structural Hardware Assembly - A series of plastic parts manufactured using an FDM rapid prototyping process and designed to integrate the sensing system with the robot's hardware
<br>
These three component parts function together to deliver the desired actuator positional data required by the project.
<br>


## Schematic Diagram of Electronic Components

As this system uses off-the-shelf products as part of the complete integration, and as such these products are well documented by their manufacturers, detailed schematics of those products will be omitted from this documentation. Links to these resources will however be provided.
<br>
(insert system schematic here)
<br>
(insert description of system schematic here)
<br>
(insert description and links to off the shelf parts here)
<br>


## Structural Hardware Assembly


