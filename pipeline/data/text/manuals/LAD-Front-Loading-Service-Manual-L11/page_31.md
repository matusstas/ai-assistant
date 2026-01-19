# 5. MALFUNCTION CODES AND EXPLANATIONS

## E50

| Malfunction code | Root Reason                                     | Possible cause                                                                                                                                           |
|------------------|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| E50              | Motor inverter PCB detects abnormal signals and show the error | The external voltage is abnormal, which causes the motor inverter PCB to judge that the voltage is too high or too low                                   |
|                  |                                                | The motor inverter PCB is overloaded -> It may be that the motor rotation is blocked, causing the motor inverter PCB to overload                         |
|                  |                                                | The motor inverter PCB is damaged, causing the motor inverter PCB to detect excessive current or abnormal IPM temperature sampling.                       |
|                  |                                                | The motor inverter PCB is abnormal due to the main PCB issue. There are the following situations: 1) The motor speed signal cannot be detected; 2) Due to the abnormality of the main PCB, the temperature of the motor inverter PCB is abnormal, and the motor temperature is misjudged to be too high; 3) The motor inverter read the information (Flash) incorrectly due to the defective motor inverter PCB. |