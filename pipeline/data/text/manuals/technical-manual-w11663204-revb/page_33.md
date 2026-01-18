```markdown
# Wiring Diagram

**IMPORTANT:** Electrostatic discharge may cause damage to machine control electronics. 

**NOTE:** Schematic shows shifter in SPIN position, lock switch open, and motor off.

## CONTROL ASSEMBLY

### POWER CORD
- **J7**
  - LI: 1
  - GND: 2
  - N: 3

### WATER VALVES
- **J3**
  - WH: 1
  - HOT: 2
  - COLD: 3
  - BU: 4
  - RD: 5

### WATER TEMPERATURE
- **BK**
  - WATER TEMPERATURE THERMISTOR
    - 150 °C: 75K to 15K
    - 25 °C: 47K to 15K
    - 0 °C: 189K to 27K

### PRESSURE SWITCH
- **J10**
  - ROTARY ENCODER: 4 POSITION EXTRA RINSE
- **ROTARY ENCODER**
  - WATER LEVEL

### ENCODER SWITCH
- **J11**
  - ROW 3: 1
  - ROW 2: 2

### LID SWITCH INPUT
- **J15**
  - RD: 4
  - WH: 2
  - BU: 3
  - YL: 4

## MOTOR RELAY
- **J16**
  - 1: COL
  - 2: 5
  - 3: 6
  - 4: 7
  - GND TO TOP: 1

### SHIFTER
- **J2**
  - SHIFTER POSITION INPUT: 1
  - RPM INPUT: 2
  - +10 VDC: 4
  - AGITATE: 5
  - SPIN: 6

### DRAIN PUMP 
- **TN**
  - 12V AC MOTOR
  - MOTOR RESISTANCE 14Ω TO 25Ω

### DRIVE MOTOR
- **WH**
  - CCW WINDING: 33.3Ω/8.8Ω
  - CW WINDING: 6Ω

### LID SWITCH
- **BU**
  - OPEN WHEN LID IS OPEN

## LEGEND
- Ground
- Connector
- Pad
- Control Position
- Package (Assembly Width)
- Thermal Switch (heat seal)
- Reactor / Emitter
- Relay
- Lid Lock Indicator
- Fuse Resistor
- Thermal
- Temp Sensor
```
