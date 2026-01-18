```markdown
## COMPONENT TESTING (CONT.)

8. With a voltmeter set to AC, connect black probe to motor relay pin 2, red probe to 16-7 (CW Winding).
   
   - If 120 VAC is cycling ON during CW rotation, go to step 9.
   - If 120 VAC is not present, go to Test #1: Main Control.

9. Unplug washer or disconnect power.

10. Remove connector J16 from main control. With an ohmmeter, check resistance of motor windings across the following J16 connector pinouts:

    **NOTE:** If the console has a cycle selector knob and 4 rotary switches, the motor size is 1/2 HP.
    
    | Size   | Motor Winding | J16 Pin | Resistance   |
    |--------|---------------|---------|--------------|
    | 1/2 HP | CCW Winding   | J16-6 to motor relay pin 2 | 3.5 to 6 Ω |
    |        | CW Winding    | J16-7 to motor relay pin 2 | 3.5 to 6 Ω |
    
    - If values are open or out of range, go to step 11.
    - If values are correct, go to step 15.

11. Tilt washer back to access drive system.

12. Visually check the mounting bracket and electrical connections to the motor and shifter.

13. If visual check passes, go to step 13.

14. If connections are loose, reconnect the electrical connections, reassemble cover, and repeat step 1.

15. With an ohmmeter, check resistance of motor windings at the following connectors:

    **NOTE:** If the console has a cycle selector knob and 4 rotary switches, the motor size is 1/2 HP.

    | Size   | Motor Winding | Motor Pinout | Resistance  |
    |--------|---------------|--------------|-------------|
    | 1/2 HP | CCW Winding   | Pins 4 and 2 | 3.5 to 6 Ω  |
    |        | CW Winding    | Pins 3 and 2 | 3.5 to 6 Ω  |

    - If values are open or out of range, replace motor.

16. Test Motor Capacitor.

    **NOTE:** A faulty capacitor may cause the motor to “hum”, not start, or turn slowly.
    
    - Discharge the capacitor by touching the leads of a 20,000 Ω resistor to the two terminals.
    - Disconnect the wires from the capacitor terminals.
    - With an ohmmeter, measure across the terminals and note reading.

    - If a steady increase in resistance is noted, continue to step 16.
    - If the capacitor is either shorted or open, replace capacitor, calibrate the washer, and repeat step 1.

17. If the preceding steps did not correct the motor problem, replace the main control.
    
    - Unplug washer or disconnect power.
    - Replace the main control.
    - Reassemble all parts and panels.
    - Plug in washer or reconnect power. Calibrate washer and perform Quick Overview Test to verify repair.

## TEST #4: Console and Indicators

Console and Indicators Check:

This test is performed when any of the following situations occurs during "UI Test Mode":
- None of the LEDs light up
- One or more Status LEDs are flashing
- Turning rotary switch does not toggle LED

### None of the LEDs light up:

1. Unplug washer or disconnect power.
2. Access the main control and visually check that all connectors are inserted all the way into their respective headers.
3. Visually check that the main control assembly is properly inserted in the console.
4. If both visual checks pass, follow procedure under Test #1: Main Control to verify supply volts.

5. To verify repair, activate the Service Diagnostic Mode, and then perform UI Test Mode.

### One or more Status LEDs are flashing:

If one or more of the status LEDs are flashing (on and off in 0.5 second intervals), refer to the following notes to identify the switch(es) in question. Refer the wiring diagram when performing the following procedures.

a. Verify the switch connector is inserted all the way into the main control.

b. Check the harness between the switch and main control for continuity. Check for shorts.

c. Replace the switch.

d. Replace the main control.

**NOTE:** The number and location of rotary switches varies between makes and models.

**NOTE:** Regardless of location, switches are read from left to right (not counting the pressure transducer), the left-most switch being #1.

**NOTE:** Each rotary switch and the cycle selector knob is represented by the following status LEDs:
- Rotary Switch #1 – toggles (1) POWER LED
- Rotary Switch #2 – toggles (2) SOAK/WASH LED
- Rotary Switch #3 – toggles (3) RINSE LED
- Rotary Switch #4 – toggles (4) FINAL SPIN LED
- Cycle Select Knob – toggles (5) DONE LED
```