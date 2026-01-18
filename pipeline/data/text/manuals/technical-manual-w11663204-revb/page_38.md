```markdown
## COMPONENT TESTING (CONT.)

**NOTE:** Status LED names may vary between makes and models. Use LED identification.

|   |  (1) **POWER**  | (2) **SOAK/ Wash** | (3) **RINSE** | (4) **FINAL SPIN** | (5) **DONE** |
|---|----------------|--------------------|---------------|---------------------|--------------|
|   |                |                    |               |                     |              |

### Turning rotary switch does not toggle LED:
Perform the procedures under “One or more Status LEDs are flashing.”

---

### TEST #5: Temperature Thermistor
This test checks valves, main control, temperature thermistor, and wiring.

1. Check the cold valve by performing Cold Valve test under **Manual Overview Test Mode**.
   - If cold water is being dispensed, proceed to step 2.
   - If hot water is being dispensed, verify proper hose connection.
   
2. Check the hot valve by performing Hot Valve test under **Manual Overview Test Mode**.
   - If hot water is being dispensed, ensure that household hot water is present.

3. Unplug washer or disconnect power.

4. Remove console to access main control.

5. Remove connector J3 from the main control. With an ohmmeter, measure the resistance of the temperature thermistor between pins J39 and J340. Verify that the approximate resistance, shown in the following table, is within ambient temperature range.

#### THERMISTOR RESISTANCE

| Approx. Temperature (°F) | Approx. Resistance (kΩ) |
|--------------------------|--------------------------|
| 32                       | 0                        |
| 41                       | 5                        |
| 50                       | 10                       |
| 59                       | 15                       |
| 68                       | 20                       |
| 77                       | 25                       |
| 86                       | 30                       |
| 95                       | 35                       |
| 104                      | 40                       |
| 113                      | 45                       |
| 122                      | 50                       |
| 131                      | 55                       |
| 140                      | 60                       |
| 149                      | 65                       |

- If the resistance is within the range shown in the table, go to step 6.
- If the resistance is infinite or close to zero, replace the temperature thermistor assembly.

---

### TEST #6: Water Level
This test checks the water level sensing components. This washer uses an on-board pressure transducer.

**NOTE:** Usually, if the pressure transducer malfunctions, the washer will generate a long fill or long drain error.

1. Check the functionality of the pressure transducer by running a small load cycle. The valves should turn off automatically after sensing the correct water level in the tub. The following steps assume that this step was unsuccessful.
   
2. Drain the tub until all water has been removed.

3. Unplug washer or disconnect power.

4. Remove console to access main control.

5. Check hose connection between the pressure transducer and the pressure dome attached to the tub.

6. Check to ensure hose is routed correctly in the lower cabinet and not pinched or crimped by the back panel.

7. Verify there is no water, suds, or debris in the hose or dome. Disconnect hose from main control and blow into hose to clear water, suds, or debris. 

8. Check hose for leaks. Replace if needed.

- If the preceding steps did not correct the problem,replace the main control and calibrate washer. Perform **Quick Overview Test** to verify repair.

---

### TEST #7: Drain Pump
Perform the following checks if washer does not drain.

**NOTE:** Refer to Figure “Drain Pump Strip Circuit” for tests and measurements.

**IMPORTANT:** Drain water from tub before accessing bottom of washer.

1. Check for obstructions in the usual areas. Clean and then perform step 2.

2. Check the drain pump and electrical connections by performing the **Drain Test** under **Manual Overview Test Mode**. The following steps assume that this step was unsuccessful.

3. Unplug washer or disconnect power.

4. Remove console to access main control.

5. Visually check that the J16 connector is inserted all the way into the main control.
   - If visual check passes, go to step 6.
   - If connector is not inserted properly, reconnect J16 and repeat step 2.

6. Remove connector J16 from main control. With an ohmmeter, verify resistance values shown below across the following J16 connector pinouts:

| Component  | J16 Connector Pinout       |
|------------|-----------------------------|
| Drain Pump | J16, 2 and 3                |

Resistance should be 14–25 Ω.
- If values are open or out of range, go to step 7.
- If values are correct, go to step 11.
```
