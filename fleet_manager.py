

valid_ranks = ["Ensign", "Lieutenant Junior", "Lieutenant", "Lt. Commander", "Commander", "Captain"]
salary_list = [200, 300, 400, 500, 600, 700]

def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Kirk"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    divs = ["Command", "Command", "Operations", "Security", "Command"]
    ids = [0,1,2,3,4]

    return names, ranks, divs, ids

def display_menu():
    student_name = input("Please enter your full name:")
    print("\n--- MENU ---")
    print(f"The current student logged in is:{student_name}")
    print("1. Add Mmber")
    print("2. Remove Member")
    print("3. Update Rank")
    print("4. Display Roster")
    print("5. Search Crew")
    print("6. Filter by division")
    print("7. Calculate Payroll")
    print("8. Count Officers")        
    print("9. Exit")
    choice = input("Please select menu option")
    return choice

def add_member(names, ranks, divs, ids):
    while True:
        new_id = int(input("Please enter the id of the new crew memeber:"))
        if new_id in ids:
            print("Id is already used, please enter a valid id!")
            continue
        else:
            break
    while True:
        new_rank = input("Please enter the rank of the new member:")
        if new_rank not in valid_ranks:
            print("Please enter a valid TNG rank!")
            continue
        else:
            break
    new_name = input("Please enter the name of the new crew member:")
    new_div = input("Please enter the division of the new crew member")
    names.append(new_name)
    ranks.appned(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    return names, ranks, divs, ids

        

def remove_member(names, ranks, divs, ids):
    while True:
        rem_id = int(input("Please enter the id of the crew member you want to remove:"))
        if rem_id not in ids:
            print("The ID enter is not valid. Please enter a valid ID!")
            continue
        else:
            break
    rem_index = ids.index(rem_id)
    names.pop(rem_index)
    ranks.pop(rem_index)
    divs.pop(rem_index)
    ids.pop(rem_index)

    return names, ranks, divs, ids


def update_rank(names, ranks, ids):
    while True:
        update_id = int(input("Please enter the id of the crew member that you want to update the rank for:"))
        if update_id not in ids:
            print("Invalid id entered. Please enterr a valid id!")
        else:
            break
    update_index = ids.index(update_id)
    while True:
        new_rank = input("Please enter the new rank:")
        if new_rank not in valid_ranks:
            print("Invalid rank entered. Please enter a valid rank!")
            continue
        else:
            break
    ranks[update_index] = new_rank

    return names, ranks, ids 

def display_roster(names, ranks, divs, ids):
    w = 20
    print(f"{"Name":^{w}} | {"Rank":^{w}} | {"Division":^{w}} | {"ID":^{w}}")
    for i in range(len(names)):
        print(f"{names[i] :^{w}} | {ranks[i] :^{w}} | {divs[i] :^{w}} | {ids[i] :^{w}}")

def search_crew(names, ranks, divs, ids):
    search_string = input("Please enter the search term:")
    found_indeces = [i for i, name in enumerate(names) if search_string in name]
    if found_indeces:
        for index in found_indeces:
            print(names[index], ranks[index], divs[index], ids[index])
    else:
        print("No crew member found!")



def filter_by_division(names, divs):
    division = input("Please select the division from Command , Operations or Sciences")
    counter = 0
    for el in divs:
        if el == division:
            index = divs.index(el)
            print(names[index], el)
            counter += 1
    print(f"Search completed.Total members found:{counter}")


#The salary_list corresponds to the valid_ranks list defined at the top.
def calculate_payroll(ranks):
    salary_list = [200, 300, 400, 500, 600, 700]
    total_cost = 0
    for rank in ranks:
        index = valid_ranks[rank]
        credit_val = salary_list[index]
        total_cost += credit_val
    return total_cost


def count_officers(ranks):
    counter = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            counter += 1
    return counter

def main():
    names, ranks, divs, ids = init_database()
    while True:
        choice = display_menu()
        match choice:
            case "1":
                names, ranks, divs, ids = add_member(names, ranks, divs, ids)

            case "2":
                names, ranks, divs, ids = remove_member(names, ranks, divs, ids)
                
            case "3":
                names, ranks, ids = update_rank(names, ranks, ids)

            case "4":
                display_roster(names, ranks, divs, ids)

            case "5":
                search_crew(names, ranks, divs, ids)

            case "6":
                filter_by_division(names, divs)

            case "7":
                payroll = calculate_payroll(ranks)
                print(f"The total payroll is {payroll}")

            case "8":
                officers = count_officers(ranks)
                print(f"The total number of officers is:{officers}")

            case "9":
                break

            case _:
                print("Invalid choice entered. Please enter a valid choice from the menu!")
                continue




if __name__ == "__main__":
    main()
