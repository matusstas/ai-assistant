```markdown
# Troubleshooting Tests

## TEST #1: Main Control
This test checks for incoming and outgoing supplies to and from the main control. This test assumes that proper voltage is present at the outlet.

1. Unplug washer or disconnect power.
2. Remove console to access main control.
3. Verify that all connectors are inserted all the way into the main control.
4. Plug in washer or reconnect power.
5. With a voltmeter set to AC, connect black probe to J7-3 (Neutral) and red probe to J7-1 (L1).
   - If 120 VAC is present, go to step 6.
   - If 120 VAC is not present, check the AC power cord for continuity (See Wiring Diagram).
6. Is the “Diagnostic LED” ON or OFF? (See Figure below for LED location.)
   - ON: (+5 VDC present) continue to step 7.
   - OFF: (+5 VDC missing) proceed to step 8.
7. With a voltmeter set to DC, connect black probe to J2-3 (Circuit Gnd) and red probe to J2-4 (+13 VDC).
   - If +13 VDC is present, main control supplies are good.
   - If +13 VDC is not present, go to step 8.
8. Check if shifter assembly is affecting the main control DC supplies.
   a. Unplug washer or disconnect power.
   b. Remove connector J2 from main control.
   c. Plug in washer or reconnect power.
   d. Repeat steps 6 and 7. Perform the +13 VDC check inside header J2 on the board – do not short pins together.
   - If one or more DC voltages are still missing, go to step 9.
   - If the DC voltages return, check for short in harness between main control and shifter assembly.
   - If harness and connections are good, replace shifter assembly.

## Main Control Board Connectors and Pinouts
| Pin | Description                          | Pin | Description                      |
|-----|--------------------------------------|-----|----------------------------------|
| J1  | Open                                 | J10 | J10-6 BLK ROW 2                  |
| J2  | +5 VDC                              | J11 | J11-6 RED ROW 4                  |
| J3  | TEMP THERMISTOR INPUT (HYBRID)     | J12 | J12-3 RED COLUMN 1               |
| J4  | PRESSURE TRANSDUCER INPUT           | J13 | J13-3 RED COLUMN 2               |
| J5  | Open                                 | J14 | J14-5 RED COLUMN 3               |
| J6  | Open                                 | J15 | J15-4 LOCK SWITCH                 |
| J7  | POWER CORD                          | J16 | J16-7 RED MOTOR COW WINDING (1)  |
| J8  | Open                                 | J17 | J17-6 RED MOTOR (NEUTRAL)        |

- Diagnostic LED

---

*Not available on all models.*
```