n = ["Picard", "Riker", "Data", "Worf"]
r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
d = ["Command", "Command", "Operations", "Security"]

active = True

def run_system_monolith():
    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")
    
    
    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        #infinite loop, adding line to add 1 to loading every cycle loading+=1
        loading += 1
        
    fuel = 100

    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")
        
        #assign operator "=" was used instead of equal "=="
        if opt == "1":  
            print("Current Crew List:")
            
            #the iteration iterates over too many indeces, change range(10) to range(len(n))
            for i in range(len(n)):
                print(n[i] + " - " + r[i]) 
                
        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
            #new_rank was not appended to the rank list
            #new division was not appended to the division list
            n.append(new_name)
            r.append(new_rank)
            d.append(new_div)
            print("Crew member added.")
            
        elif opt == "3":
            rem = input("Name to remove: ")
            #if the name is not found in the list the .index(rem) will result in an error 
            try:
                idx = n.index(rem)
            except IndexError as e:
                print("The entered name was not found in our database!")
            n.pop(idx)
            r.pop(idx)
            d.pop(idx)
            print("Removed.")
            
        elif opt == "4":
            print("Analyzing...")
            count = 0
            
            for rank in r:
                #incorrect logic for the if statement, this evaluates to true every time as "Commander" is a non-empty string, replacing with rank == "Commander"
                if rank == "Captain" or rank == "Commander": 
                    count = count + 1
            #str and int cannot be concatenated, converting count to string
            print("High ranking officers: " + str(count)) 
            
        elif opt == "5":
            print("Shutting down.")
            break
            
        else:
            print("Invalid.")
            
        
        x = 10

        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
            #second condition in if/elif/else statements should be written as elif not a second if, in this case an else statement is appropriate as the length of the list cannot be negative.
        else:
            print("Database empty.")

        #the fuel block is completely useless as it just breaks on the first iteration. I am slightly confused as to the intended logic of this block.
        #placed initial fuel=100 outside of the loop and implemented logic which removed 1 unit of fuel every iteration of the main while loop, whilst maintaining as much of the original code as possible
        consumption = 1
        while fuel > 0:
            
            print("Idling...")
            fuel -= consumption
            print(f"Fuel left {fuel}")
            break 
            
        print("End of cycle.")

#run_system_monolyth was not called, added ()
run_system_monolith()
