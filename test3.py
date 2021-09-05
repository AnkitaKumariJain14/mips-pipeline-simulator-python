if __name__ == '__main__':
    import sys
    instructions = []
    subset_inst=[]
    cycle=1
    destination=[]
    # with open("input.txt",'r') as f:
    #     for line in f:
    #         instructions.append(line.split())

    # with open("forwarding.txt",'r') as f:
    #     for line in f:
    #         instructions.append(line.split())

    # with open("stallandforward.txt",'r') as f:
    #     for line in f:
    #         instructions.append(line.split())

    with open("stall.txt",'r') as f:
        for line in f:
            instructions.append(line.split())

    # with open("new_input.txt",'r') as f:
    #     for line in f:
    #         instructions.append(line.split())
    
    # sys.stdout = open("result.txt","w")
    # sys.stdout= open("forward_result.txt","w")
    # sys.stdout= open("stallforward.txt","w")
    sys.stdout = open("stall_output.txt","w")
    # sys.stdout = open("new_result.txt","w")

    inst_length= len(instructions)
    first_instr= instructions[0]

    if(first_instr[0]=="lw" or first_instr[0]=="sw"):
        print(instructions[0][0],instructions[0][1], ",", instructions[0][2])
    else:
        print(instructions[0][0],instructions[0][1], ",", instructions[0][2], ",", instructions[0][3])
    for i in range(1,len(instructions)):
        if(instructions[i][0]=="add" or instructions[i][0]=="sub" or instructions[i][0]=="mul"):
            # Stall
            if(instructions[i-3][0]=="lw" ):
                r_destn_previous= instructions[i-3][1].strip(",")
                rs= instructions[i][2].strip(",")
                rt= instructions[i][3].strip(",")
                rd= instructions[i][1].strip(",")
                if rs==(r_destn_previous) :
                   print("STALL")
                   print(instructions[i][0], rd, ",",rs, ",", rt)
                   continue
                elif rt==(r_destn_previous) :
                    print("STALL")
                    print(instructions[i][0], rd, ",",rs, ",", rt)
                    continue
                else: 
                    print(instructions[i][0], rd, ",",rs, ",", rt)
            elif(instructions[i-3][0]=="sw" ):
                r_destn_previous= instructions[i-3][2].strip(")").split("(")[1]
                rs= instructions[i][2].strip(",")
                rt= instructions[i][3].strip(",")
                rd= instructions[i][1].strip(",")
                if rs==(r_destn_previous) :
                   print("STALL")
                   print(instructions[i][0], rd, ",",rs, ",", rt)
                   continue
                elif rt==(r_destn_previous) :
                    print("STALL")
                    print(instructions[i][0], rd, ",",rs, ",", rt)
                    continue
                else: 
                    print(instructions[i][0], rd, ",",rs, ",", rt)     
            #forwarding and stall+forwarding
            if(instructions[i-1][0]=="lw") :
               rd_previous_3 = instructions[i-1][1].strip(",")
               rd_previous_4 = instructions[i-2][1].strip(",")
               rd= instructions[i][1].strip(",")
               rs= instructions[i][2].strip(",")
               rt= instructions[i][3].strip(",")
               if rs==(rd_previous_3) :
                   print(instructions[i][0], rd, ",",rs, ",", rt)
                   print("STALL")
                   print(instructions[i][0], rd, ",", "[L4]",rs, ",", rt)
               elif rt==(rd_previous_3) :
                   print(instructions[i][0], rd, ",",rs, ",", rt)
                   print("STALL")
                   print(instructions[i][0], rd, ",", rs, ",","[L4]", rt) 
               elif rs==(rd_previous_4) :
                   if(instructions[i-1][0]=="lw" or instructions[i-1]=="sw"):
                       if(rs==instructions[i-1][2].strip(")").split("(")[1] or rs== instructions[i-1][1].strip(",")):
                           print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", "[L4]",rs,",",rt)
                   elif(instructions[i-1][0]=="add" or instructions[i-1][0]=="sub" or instructions[i-1][0]=="mul"):
                       if(rs==instructions[i-1][2].strip(",") or rs== instructions[i-1][3].strip(",")):
                            print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", "[L4]",rs,",",rt)
               elif rt==(rd_previous_4) :
                   if(instructions[i-1][0]=="lw" or instructions[i-1]=="sw"):
                       if(rt==instructions[i-1][2].strip(")").split("(")[1] or rt== instructions[i-1][1].strip(",")):
                           print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", rs,",","[L4]",rt)
                   elif(instructions[i-1][0]=="add" or instructions[i-1][0]=="sub" or instructions[i-1][0]=="mul"):
                       if(rt==instructions[i-1][2].strip(",") or rt== instructions[i-1][3].strip(",")):
                            print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", rs,",","[L4]",rt)
               else:
                   print(instructions[i][0],rd, ",", rs, ",", rt) 
                   continue
            #for storeword case
            elif(instructions[i-1][0]=="sw"):
               rd_previous_3 = instructions[i-1][2].strip(")").split("(")[1]
               rd_previous_4 = instructions[i-2][1].strip(",")
               rd= instructions[i][1].strip(",")
               rs= instructions[i][2].strip(",")
               rt= instructions[i][3].strip(",")
               if rs==(rd_previous_3) :
                   print(instructions[i][0], rd, ",",rs, ",", rt)
                   print("STALL")
                   print(instructions[i][0], rd, ",", "[L4]",rs, ",", rt)
               elif rt==(rd_previous_3) :
                   print(instructions[i][0], rd, ",",rs, ",", rt)
                   print("STALL")
                   print(instructions[i][0], rd, ",", rs, ",","[L4]", rt) 
               elif rs==(rd_previous_4) :
                   if(instructions[i-1][0]=="lw" or instructions[i-1]=="sw"):
                       if(rs==instructions[i-1][2].strip(")").split("(")[1] or rs== instructions[i-1][1].strip(",")):
                           print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", "[L4]",rs,",",rt)
                   elif(instructions[i-1][0]=="add" or instructions[i-1][0]=="sub" or instructions[i-1][0]=="mul"):
                       if(rs==instructions[i-1][2].strip(",") or rs== instructions[i-1][3].strip(",")):
                            print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", "[L4]",rs,",",rt)
               elif rt==(rd_previous_4) :
                   if(instructions[i-1][0]=="lw" or instructions[i-1]=="sw"):
                       if(rt==instructions[i-1][2].strip(")").split("(")[1] or rt== instructions[i-1][1].strip(",")):
                           print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", rs,",","[L4]",rt)
                   elif(instructions[i-1][0]=="add" or instructions[i-1][0]=="sub" or instructions[i-1][0]=="mul"):
                       if(rt==instructions[i-1][2].strip(",") or rt== instructions[i-1][3].strip(",")):
                            print(instructions[i][0], rd, ",",rs, ",", rt)
                       else:
                            print(instructions[i][0], rd, ",", rs,",","[L4]",rt)
               else:
                   print(instructions[i][0],rd, ",", rs, ",", rt) 
                   continue
            #for register instructions
            else:
                rd_previous = instructions[i-1][1].strip(",")
                rd_previous_2 = instructions[i-2][1].strip(",")
                rd= instructions[i][1].strip(",")
                rs= instructions[i][2].strip(",")
                rt= instructions[i][3].strip(",")
                if rs==(rd_previous) :
                    print(instructions[i][0], rd, ",", "[L3]",rs, ",", rt)
                elif rt==(rd_previous) :
                    print(instructions[i][0], rd, ",", rs, ",","[L3]", rt) 
                elif rs==(rd_previous_2) :
                    print(instructions[i][0], rd, ",", "[L4]",rs, ",", rt)
                elif rt==(rd_previous_2) :
                    print(instructions[i][0], rd, ",", rs, ",","[L4]", rt)
                else:
                    print(instructions[i][0],rd, ",", rs, ",", rt)
        #output for lw or sw
        elif(instructions[i][0]=="lw" or instructions[i][0]=="sw"):
                print(instructions[i][0], instructions[i][1], ",", instructions[i][2])
    sys.stdout.close()    