skills = {}

# ----------------------
# Add Skill
# ----------------------
def add_skill():
    while True:
        print("\n---- Add Skill Menu ----")
        print("1. Add Skill")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if choice == 1:
            skill = input("Enter skill: ").strip().title()

            if not skill:
                print("Skill name cannot be empty.\n")
                continue

            if skill in skills:
                print("Skill already exists.\n")
                continue

            progress = input("Enter progress: ").strip()

            if not progress:
                progress = "Just Started"

            skills[skill] = {
                "progress": progress,
                "status": "In Progress"
            }

            print(f"\n✔ {skill} added successfully.\n")

        elif choice == 2:
            break

        else:
            print("Invalid choice.\n")


# ----------------------
# Update Skill Progress
# ----------------------
def update_skill():

    skill = input("Enter skill to update: ").strip().title()

    if not skill:
        print("Skill name cannot be empty.\n")
        return

    if skill in skills:
        progress = input("Enter new progress: ").strip()

        if not progress:
            print("Progress cannot be empty.\n")
            return

        skills[skill]["progress"] = progress
        print(f"\n Progress updated for {skill}\n")

    else:
        print("\nSkill not found\n")


# ----------------------
# Show All Skills
# ----------------------
def show_skills():

    if not skills:
        print("\nNo skills added yet.\n")
        return

    print("\n======= Your Skills =======")

    for skill, info in skills.items():
        print(f"\nSkill   : {skill}")
        print(f"Progress: {info['progress']}")
        print(f"Status  : {info['status']}")

    print("\n===========================\n")


# ----------------------
# Mark Skill Completed
# ----------------------
def mark_complete():

    skill = input("Enter skill to mark complete: ").strip().title()

    if not skill:
        print("Skill name cannot be empty.\n")
        return

    if skill in skills:
        skills[skill]["status"] = "Completed"
        print(f"\n {skill} marked as completed\n")
    else:
        print("\nSkill not found\n")


# ----------------------
# Main Loop
# ----------------------
while True:

    print("========== Skill Tracker ==========")
    print("1. Add Skill")
    print("2. Update Progress")
    print("3. Mark Skill Completed")
    print("4. View Skills")
    print("5. Exit")
    print("===================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nPlease enter a valid number.\n")
        continue

    if choice == 1:
        add_skill()

    elif choice == 2:
        update_skill()

    elif choice == 3:
        mark_complete()

    elif choice == 4:
        show_skills()

    elif choice == 5:
        print("\nThanks for using Skill Tracker!\n")
        break

    else:
        print("\nInvalid choice.\n")