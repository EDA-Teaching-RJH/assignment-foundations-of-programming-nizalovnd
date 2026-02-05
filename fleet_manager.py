

valid_ranks = ["Ensign", "Lieutenant Junior", "Lieutenant", "Lt. Commander", "Commander", "Captain"]

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

def add_memeber(names, ranks, divs, ids):
    while True:
        new_id = int(input("Please enter the id of the new crew memeber:"))
        if new_id in ids:
            print("Id is already used, please enter a valid id!")
            continue
        else:
            break
    while True:
        new_rank = int(input("Please enter the rank of the new member:"))
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
    pass

def update_rank(names, ranks, ids):
    pass

def display_roster(names, ranks, divs, ids):
    pass

def search_crew(names, ranks, divs, ids):
    pass

def filter_by_division(names, divs):
    pass

def calculate_payroll(ranks):
    pass

def count_officers(ranks):
    pass

def main():
    pass


if __name__ == "__main__":
    main()
