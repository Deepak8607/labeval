students = {}
sports_recommendations = {
    'agility': ['football', 'cricket'],
    'speed': ['football', 'cricket'],
    'strength': ['javelin throw', 'cricket'],
    'strategic_thinking': ['chess'],
}

def generate_diet_plan(sport):
    diet_plans = {
        'football': 'High-carb diet with protein-rich foods like chicken, fish.',
        'cricket': 'Balanced diet with a mix of proteins, carbs, fruits and vegetables.',
        'javelin throw': 'High-protein diet and foods like lean meat, eggs, and nuts.',
        'chess': 'Balanced diet with a focus on brain foods like nuts, fish, and fruits.',
    }
    return diet_plans.get(sport, 'General balanced diet with focus on healthy eating.')

def recommend_sport(attributes):
    recommended_sport = []
    for attr, value in attributes.items():
        if value in sports_recommendations:
            recommended_sport.extend(sports_recommendations[value])
    recommended_sport = list(set(recommended_sport))
    if recommended_sport:
        return recommended_sport[0]  
    


def add_student():
    name = input("Enter student's name: ")
    student_class = input("Enter student's class: ")
    height = float(input("Enter student's height (in cm): "))
    weight = float(input("Enter student's weight (in kg): "))
    preferred_sport = input("Enter student's preferred sport (cricket/football/chess/javelin throw): ").lower()

    attributes = {}
    attributes['agility'] = input("Is the student agile? (yes/no): ").lower() == 'yes'
    attributes['speed'] = input("Is the student fast? (yes/no): ").lower() == 'yes'
    attributes['strength'] = input("Does the student have good strength? (yes/no): ").lower() == 'yes'
    attributes['strategic_thinking'] = input("Does the student have good strategic thinking? (yes/no): ").lower() == 'yes'
    
    recommended_sport = recommend_sport(attributes)
    
    students[name] = {
        'class': student_class,
        'height': height,
        'weight': weight,
        'preferred_sport': preferred_sport,
        'recommended_sport': recommended_sport,
        'diet_plan': generate_diet_plan(recommended_sport),
    }


def display_students():
    for name, details in students.items():
        print(f"\nName: {name}")
        print(f"Class: {details['class']}")
        print(f"Height: {details['height']} cm")
        print(f"Weight: {details['weight']} kg")
        print(f"Preferred Sport: {details['preferred_sport']}")
        print(f"Recommended Sport: {details['recommended_sport']}")
        print(f"Diet Plan: {details['diet_plan']}")


def main():
    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()







Enter your choice: 1
Enter student's name: ram
Enter student's class: 12
Enter student's height (in cm): 56
