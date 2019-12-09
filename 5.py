# Advent of Code - day 5
import re

dbg = False
d1_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]
d5_input = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,81,30,225,1102,9,63,225,1001,92,45,224,101,-83,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,41,38,225,1002,165,73,224,101,-2920,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,18,14,224,1001,224,-32,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,67,38,225,1102,54,62,224,1001,224,-3348,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1,161,169,224,101,-62,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,2,14,18,224,1001,224,-1890,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1101,20,25,225,1102,40,11,225,1102,42,58,225,101,76,217,224,101,-153,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,102,11,43,224,1001,224,-451,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,77,23,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,7,226,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,434,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,599,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1107,677,677,224,1002,223,2,223,1005,224,629,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,644,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]

# Returns the last two digits of the input as integer
def get_op(instr: int):
    ret = int(str(instr)[-2:])
    if (dbg):
        print("Op={}".format(ret))
    return ret

# Returns the parameter mode from instr[index] or 0 if instructions are of old style
def get_mode(instr: int, param_num: int):
    ret = 0
    if (len(str(instr)) > 1+param_num):
        ret = int(str(instr)[-2-param_num])
    if (dbg):
        print("Mode for param {} in instruction {} is {}".format(param_num, instr, ret))
    return ret

# Returns program[value] for mode 0 and value for mode 1
def get_param(program: list, mode: int, value: int):
    ret = None
    if (mode == 1):
        ret = value
    else:
        ret = program[value]
    if (dbg):
        print("Mode={}, returning {}".format(mode, value))
    return ret

def int_code_interpreter(program):
    if (dbg):
        print(program)
    i = 0
    num_params = 0
    while i < len(program):
        instr = program[i]
        opcode = get_op(instr)
        if opcode == 99:
            #print("Returning")
            return program

        if (dbg):
            print("Index: {} Opcode:{}".format(i, opcode))

        if opcode == 1: # Sum params 1 and 2, save result to param3
            if (dbg):
                print(program[i:i+4])
            num_params = 3
            p1 = get_param(program, get_mode(instr, 1), program[i+1])
            p2 = get_param(program, get_mode(instr, 2), program[i+2])
            output = program[i+3]
            if (dbg):
                print("Add: {}+{}={} => saving to position {}".format(p1, p2, p1+p2, output))
            program[output]=p1+p2

        elif opcode == 2: # Multiply params 1 and 2, save result to param3
            if (dbg):
                print(program[i:i+4])
            num_params = 3
            p1 = get_param(program, get_mode(instr, 1), program[i+1])
            p2 = get_param(program, get_mode(instr, 2), program[i+2])
            output = program[i+3]
            if (dbg):
                print("Multiply: {}*{}={} => saving to position {}".format(p1, p2, p1*p2, output))
            program[output]=p1*p2

        elif opcode == 3: # Take a single value as input, save it to param1
            if (dbg):
                print(program[i:i+2])
            num_params = 1
            user_input = input("Enter an integer: ")
            output = program[i+1]
            if (dbg):
                print("Output: input={} => saving to position {}".format(user_input, output))
            program[output] = int(user_input)

        elif opcode == 4: # Output value from param1
            if (dbg):
                print(program[i:i+2])
            num_params = 1
            p1 = get_param(program, get_mode(instr, 1), program[i+1])
            if (dbg):
                print("Output from position {} => {}".format(program[i+1], p1))
            print(p1)

        else:
            print("ERROR (Opcode:{})".format(opcode))

        i += 1+num_params
        #print(program)

#print(int_code_interpreter([1,9,10,3,2,3,11,0,99,30,40,50]))
#print(int_code_interpreter([1,0,0,0,99]))
#print(int_code_interpreter([2,3,0,3,99]))
#print(int_code_interpreter([2,4,4,5,99,0]))
#print(int_code_interpreter([1,1,1,4,99,5,6,0,99]))

# Day 2 part 1 - Should print 3790689
prg = d1_input[:]
prg[1:3]=[12,2]
print(int_code_interpreter(prg)[0])

# Day 2 part 2 - Should print 6533
#expected = 19690720
#for noun in range(0,99):
#    for verb in range(0,99):
#        prg = d1_input[:]
#        prg[1]=noun
#        prg[2]=verb
#        #print("noun={} verb={}".format(noun, verb))
#        #print(prg)
#        result = int_code_interpreter(prg)
#        #print("Noun={} verb={} results {}".format(noun, verb, result[0]))
#        if expected == result[0]:
#            print("Match found with noun={} and verb={}, exiting!".format(noun, verb))
#            break

# Day 5 part 1
print(int_code_interpreter([1002,4,3,4,33])) # Test code, should print [1002,4,3,4,99]
print(int_code_interpreter([1101,100,-1,4,0])) # Test code, should print [1101,100,-1,4,99]
int_code_interpreter([3,0,4,0,99]) # Test code, should print whatever you give as input and halt

# The real code, should print nothing but zeroes with one last non-zero
int_code_interpreter(d5_input)
