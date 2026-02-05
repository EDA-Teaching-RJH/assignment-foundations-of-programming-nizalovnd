

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
    pass

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
