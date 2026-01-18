```markdown
9. Main Control has malfunctioned.
   a. Unplug washer or disconnect power.
   b. Replace the main control.
   c. Reassemble all parts and panels.
   d. Plug in washer or reconnect power. Calibrate washer and perform Quick Overview Test to verify repair.

## TEST #2: Valves
This test checks the electrical connections to the valves and the valves themselves.

1. Check the electrical connections to the valves by performing the Cold and Hot Valve tests under Manual Overview Test Mode. Each test activates and deactivates the selected valve. The following steps assume one (or more) valve(s) did not turn on.

2. For the valve(s) in question, check the individual solenoid valves:
   a. Unplug washer or disconnect power.
   b. Remove console to access main control.
   c. Remove connector J3 from main control. Refer to Main Control Board Connector and Pinouts.

3. Check resistance of the valve coils across the following J3 connector pinouts:

| Valve     | Pinout  |
|-----------|---------|
| Hot Valve | J3, 1 and 4 |
| Cold Valve| J3, 1 and 2 |

   Resistance should be 890–1.3k Ω.
   - If resistance readings are tens of ohms outside of range, replace the valve assembly.
   - If resistance readings are within range, replace main control and calibrate washer. Perform Quick Overview Test to verify repair.

## TEST #3a: Drive System – Shifter
This test checks connections, shifter motor, switch, and optical sensor.

**NOTE:** Refer to figure “Shifter Assembly Strip Circuit” for tests and measurements.

**IMPORTANT:** Drain water from tub before accessing bottom of washer.

### Functional Check:
1. Check the shifter and electrical connections by performing both the Spin and Agitate test under Manual Overview Test Mode. The following steps assume that this step was unsuccessful.

2. Unplug washer or disconnect power.

3. Check to see if basket will turn freely.
   - If basket turns freely, go to step 4.
   - If basket does not turn freely, determine what is causing the mechanical friction or lockup.

4. Remove console to access main control.

5. Visually check that the J2 and J16 connectors are inserted all the way into the main control.
   - If visual checks pass, go to step 6.
   - If connectors are not inserted properly, reconnect J2 and J16 and repeat step 1.

### Shifter Motor:
6. Remove connector J16 from main control. With an ohmmeter, verify resistance of the shifter motor across the following J16 connector pinouts:

| Component | J16 Connector Pinout |
|-----------|-----------------------|
| Shifter Motor | J16, 1 and 2              |

   Resistance should be 2k to 3.5k Ω.
   - If values are correct, reconnect J16 and proceed to step 7.
   - If values are open or out of range, go to step 13.

7. Plug in washer or reconnect power.

8. With a voltmeter set to AC, connect the black probe to J16-2 (N) and red probe to J16-1 (L). Activate shifter motor by switching between Spin and Agitate modes. Energize outputs using Manual Overview Test Mode.

   **NOTE:** It will take 4–15 seconds for the shifter to change states.
   - If 120 VAC is present, go to step 9.
   - If 120 VAC is not present, go to step 17.

### Shifter Switch:
9. With a voltmeter set to DC, connect the black probe to J2-3 (Circuit Gnd) and red probe to J2-1 (Shifter Switch). In Manual Overview Test Mode, switch between Spin and Agitate modes. Voltage should toggle between 0 and +5 VDC.

   - SPIN = +5 VDC
   - AGITATE = 0 VDC

**Figure - Shifter Assembly Strip Circuit**

Maytag® 3.5 cu ft Commercial-Grade Residential Agitator Washer  ∙  3-5
```