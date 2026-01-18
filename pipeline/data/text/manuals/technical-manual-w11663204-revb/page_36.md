```markdown
# COMPONENT TESTING (CONT.)

- If voltage corresponds to setting, go to step 10.
- If voltage does not switch, go to step 12.

## Optical Sensor:
1. With a voltmeter set to DC, connect the black probe to J2-3 (Circuit Gnd) and red probe to J2-4 (+13 VDC).
   - If +13 VDC is present, go to step 11.
   - If +13 VDC is not present, go to step 17.
   
11. Activate Tachometer Verification Mode from the Service Diagnostic Test Modes. Slowly turn the basket by hand. The 4 status LEDs should illuminate one at a time to represent basket RPM.
   - If the tachometer is not verified, go to step 12.
   - If the tachometer is verified, go to step 17.

12. Unplug washer or disconnect power.
13. Tilt washer back to access the bottom of the washer and the drive motor area.
14. Visually check the electrical connections to the shifter.
   - If visual check passes, go to step 15.
   - If connections are loose, reconnect the electrical connections and repeat step 11.

15. With an ohmmeter, check the harness for continuity between the shifter and main control using the pinouts in the following chart.
   - If there is continuity, go to step 16.
   - If there is no continuity, replace the lower washer harness and repeat step 1.

| Shifter Connector Pin |  To Main Control  |
|-----------------------|-------------------|
| Pin 2                 | J16-2             |
| Pin 3                 | J16-1             |
| Pin 4                 | J2-4              |
| Pin 5                 | J2-3              |
| Pin 6                 | J2-2              |
| Pin 7                 | J2-1              |

16. Replace the shifter assembly.  
   a. Unplug washer or disconnect power.  
   b. Replace shifter assembly.  
   c. Reassemble all parts and panels.  
   d. Plug in washer or reconnect power. Calibrate washer and perform Quick Overview Test to verify repair.

## TEST #3b: Drive System – Motor

This test checks the motor, motor relay, motor windings, wiring, and start capacitor.

**NOTE:** Refer to figure “Drive Motor Strip Circuit” for tests and measurements.

**IMPORTANT:** Drain water from tub before accessing bottom of washer.

1. Check the motor and electrical connections by performing the Gentle or Heavy Agitation test under Manual Overview Test Mode. The following steps assume that this step was unsuccessful.
2. Unplug washer or disconnect power.
3. Check to see if basket will turn freely.
   - If basket turns freely, go to step 4.
   - If basket does not turn freely, determine what is causing the mechanical friction or lockup.
4. Remove console to access main control.
5. Visually check that the J2 and J16 connectors are inserted all the way into the main control.
   - If connectors are not inserted properly, reconnect J2 and J16 and repeat step 1.
6. Plug in washer or reconnect power. Run the Gentle Agitation test under Manual Overview Test Mode.
7. With a voltmeter set to AC, connect black probe to motor relay pin 2 and red probe to J16-6 (CCW Winding).
   - If 120 VAC is cycling ON during CCW rotation, go to step 8.
   - If 120 VAC is not present, go to Test #1: Main Control.

---

**Figure - Drive Motor Strip Circuit**
```