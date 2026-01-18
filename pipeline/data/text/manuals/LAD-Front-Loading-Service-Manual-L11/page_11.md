```markdown
# 4 FACTORY PATTERN DETECTION

## 4.1 Service mode

| LED Display | Check Target                             | Check Method                                                                                                                                                        | Check Item                            |
|-------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| t06         | Pressure switch checking                | Press [K7] button to activate inlet valve. The inlet valve enters the overflow water level to display the current water level frequency in real time.              | LED displays the current water level. |
| t07         | Water temperature sensor and heater checking | Press [K7] button to activate the main inlet valve and get the water lever to heating level then turn on the heater and 5 mins later turned off automatically.    | LED displays the current temperature.  |
| t08         | Inlet valve checking                    | 1. Press [K7] button; <br> 2. Press [K1] button, switch off the main wash inlet valve, switch on prewash valve for 5s; <br> 3. Press [K1] to switch on main wash and prewash valve to get the water lever to setting level; <br> 4. Press [K7] button to drain out the water. | LED displays the corresponding status. |
| t09         | Rotating checking                       | Press [K7] button, inner drum rotates in 45r/m clockwise for 15s and stops for 10s then rotates counterclockwise for 15s, over and over again.                  | LED displays the rotation speed.      |
| t10         | Spin speed checking                     | Press [K7] button, the number on the display goes up in the same pace with the real speed and when it reaches 400rpm, you need to press [K1] then [K2] button to get the machine to reach its target speed. | LED displays the rotation speed.      |
```