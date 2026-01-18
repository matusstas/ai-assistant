```markdown
# 5. MALFUNCTION CODES AND EXPLANATIONS

**E64**
- **Define:** Motor inverter PCB error (Only BLDC model have this error code)
  
- **Reasons:** Poor communication between main PCB board and motor inverter PCB (abnormal signal transmission).
  - (a) Press the start button, and the main PCB board sends a command to communicate with the motor inverter PCB. If there is no reply from the motor inverter PCB within 20 seconds, it is considered as communication failure. After disconnecting the power supply of the motor inverter PCB for 2 minutes (resetting the motor inverter), power on again and try to send a command to connect the motor inverter. If communication is successful, start the operation. If it fails, give a direct alarm. A total of 7 attempts are made.
  - (b) During operation, the main PCB board sends a command to communicate with the motor inverter PCB. If there is no reply from the motor inverter within 20 seconds, it is considered as communication failure. After disconnecting the power supply of the motor inverter for 2 minutes (resetting the motor inverter), power on again and try to send a command to communicate with the motor inverter. If the communication is successful, the operation will resume. Otherwise, after trying the above methods for 7 times, the communication fails and gives an alarm. Totally try 15 times.
```