```markdown
# 6 TROUBLESHOOTING

## Fault tree
1. Maintenance non-heating malfunction

```
Non-heating
```
- Y
  - Whether NTC is short or open circuit
    - Y → Change NTC
    - N → Whether the connection is correct
      - Y → Whether the heater is well
        - Y → Change the PCB
        - N → Change the heater
      - N → Reliable connection
```