import numpy as np

agents = np.empty(10, dtype=bool)
                #Panel User  Enter  Temp   Ext   Alum   Luz   Alarm  Riego  Cerr
initial_state = [True, True, False, False, False, False, False, False, False, False]

def main(initial_state, iter):
    agents = initial_state
    print("     PanCon | User | Entr | Temp | Ext | Alum | Luz | Alar | Rie | Cer")
    print(f'agents: {agents}, iteration: 0')
    for i in range(iter):
        if agents[0]==True and agents[2] == True and (agents[1] == False or agents[6] == False): 
            agents[7] = True
        if agents[6] == False and agents[0] == True and agents[4] == True: 
            agents[5] = True 
            agents[8] = True
        if agents[0]==True and agents[1]== True and agents[6] == True: 
            agents[2] = False 
            agents[4] = False
        if agents[0]==True and agents[1] == False: 
            agents[3] = True
        if agents[0]==True and agents[3] == True or agents[6] == False: 
            agents[9] = True
        if agents[9] == True and agents[2] == True: 
            agents[7] = True
        print(f'agents: {agents}, iteration: {i+1}')

main(initial_state, 10)
