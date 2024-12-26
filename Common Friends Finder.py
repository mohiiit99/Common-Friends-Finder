# Common Friends Finder


def get_friends():
   
    print("Enter friends for each person (comma-separated). Type 'done' to finish.")
    friends_data = {}
    while True:
        person = input("Enter person name (or type 'done'): ").strip()
        if person.lower() == 'done':
            break
        friends = input(f"Enter friends of {person} (comma-separated): ").strip().split(',')
        friends_data[person] = [friend.strip() for friend in friends]
    return friends_data

def find_common_friends(person1, person2, friends_data):
   
    friends1 = friends_data.get(person1, [])
    friends2 = friends_data.get(person2, [])
    return list(set(friends1) & set(friends2))

def main():
    print("=== Common Friends Finder ===")

    
    friends_data = get_friends()

    print("\nFind common friends between two people.")
    person1 = input("Enter the first person's name: ").strip()
    person2 = input("Enter the second person's name: ").strip()

    if person1 in friends_data and person2 in friends_data:
        common_friends = find_common_friends(person1, person2, friends_data)
        if common_friends:
            print(f"\nCommon friends between {person1} and {person2}: {', '.join(common_friends)}")
        else:
            print(f"\n{person1} and {person2} have no common friends.")
    else:
        print("\nOne or both persons are not in the friends data.")

if __name__ == "__main__":
    main()
