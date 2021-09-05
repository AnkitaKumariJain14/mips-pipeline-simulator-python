# MIPS-pipeline_simulator-python
A simple MIPS Pipeline simulator that works with a subset of MIPS instructions and outputs the instructions to be scheduled.
### Example:
   #### Input:
        add $1, $8, $9
        mul $4, $1, $2
        lw $3, 0($5)
        mul $6, $2, $4
        sw $7, 0($4)
   #### Output:
        add $1, , $8, , $9
        mul $4 , [L3] $1 , $2
        lw $3, , 0($5)
        mul $6 , $2 , [L4] $4
        sw $7, , 0($4)
