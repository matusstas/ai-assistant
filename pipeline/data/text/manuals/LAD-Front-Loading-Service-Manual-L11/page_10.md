# 4 FACTORY PATTERN DETECTION

## 4.1 Service mode

|   |   |   |   |   |
|---|---|---|---|---|
| K1 | K3 | K5 |   | K7 |
| K2 | K4 | K6 |   |   |

Before entering into service mode, make sure no water remains in the inner drum, if not, select spin only program to drain them out.  
Turn on the machine and take turns pressing [K3] [K5] [K3] [K5] buttons in 10s.  
Press [K1] or [K2] to select test program. Press [K7] to confirm your selection and start the selected test. If you want to go back to test selection interface, press the [K7] to cancel previous selection.

### LED Display

| Check Target                     | Check Method                                                                                                                                               | Check Item                                           |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| t01 Version switchover           | Press [K7] button                                                                                                                                         | LED displays “xxx” (x means current version)        |
| t02 Error code checking           | 1. Press [K7] button; <br> 2. Press [K1] to show the next code and press [K2] to show the last code; <br> 3. Press [K3] and [K4] button at the same time continuously for 3s, all the error code records deleted, LED displays “E00”. | LED displays “Exx” (x means error code)             |
| t03 Version information checking   | Press [K7] button enter into service mode. <br> Press [K7] again, LED displays project number and version number in turn.                                 |                                                     |
| t05 Drain-pump checking           | Press [K7] button to drain out all the remaining water.                                                                                                  | If all water drained out, LED displays “EP” or “good”, <br> After 20s, if there is still water remains in it, LED displays “FP” or “Err”. |