```markdown
# 5. MALFUNCTION CODES AND EXPLANATIONS

## E50

### Check Procedure:

Check whether the voltage used by the machine is reasonable:
1. For the model with the voltage of 220V~240V on the rating label, check whether the voltage used by the machine is less than 165V or more than 275V.
2. For the model with the voltage of 110V~127V on the rating label, check whether the voltage used by the machine is less than 83V or more than 158V.

- **No**: Adjust the operating voltage of the machine to the recommended voltage on the rating label, and run the machine again for one cycle.

- **Yes**: Check whether the motor operation is blocked, such as whether there are foreign matters stuck in the motor, which affect the motor rotation.

  - **Yes**: Remove the foreign matters that affect the rotation of the motor, replace the motor and run it for another cycle.
  
  - **No**: Replace the motor and run it again for one cycle to see if the problem is solved.
  
    - **Yes**: The problem is that the defective motor inverter PCB.
    
    - **No**: Replace the main PCB and run it again for one cycle to see if the problem is solved.
    
      - **Yes**: The problem is that the defective harness (Broken somewhere).
      
The maximum possibility of this problem is:
1. The voltage used by the machine exceeds the recommended voltage range of the machine;
2. The motor is defective, causing E50 alarm, and the motor needs to be replaced.
```