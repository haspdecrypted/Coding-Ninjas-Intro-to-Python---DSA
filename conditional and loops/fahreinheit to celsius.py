# Read input as sepcified in the question
# Print output as specified in the question
start_temp=int(input()) #start temp
end_temp=int(input())   #end temp
step_size=int(input())  #step size

present_temp= start_temp  #takes in present temp as the start value initializing
 
while present_temp<=end_temp:  #goes untill present temp is not less than equal to end line
    cel = 5/9 * (present_temp-32) #formula for celsius from fahrenheit
    print(present_temp, int(cel)) #printing format
    present_temp+=step_size #increments present temp with new step size which is entered
    
