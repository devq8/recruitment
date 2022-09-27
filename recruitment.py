# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
from operator import index


def get_skills():
    return ['Python', 'JavaScript', 'CSS', 'HTML']


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    print('\nSkills:')
    for index, skill in enumerate(skills):
        print(f"{index+1}. {skill}")
    print('\n')

# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    picked_skills = []
    # Validate the number of skill entered by the user. (Need to be added)

    picked_skills.append(get_skills()[int(input('Choose a skill from above by entering its number: ')) - 1])
    picked_skills.append(get_skills()[int(input('Choose another skill from above by entering its number: ')) - 1])
    
    return picked_skills


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}
    cv['name'] = input('What\'s your name? ')
    cv['age'] = int(input('How old are you? '))
    cv['experience'] = int(input('How many years of experience do you have? '))
    show_skills(get_skills())
    cv['skills'] = get_user_skills(skills)
    return cv


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    
    if 25 < cv['age'] < 40 and cv['experience'] > 3 :
        # Check desired skills
        
        if cv['skills'][0] in desired_skill and cv['skills'][1] in desired_skill:
            print(f"You have been accepted, {cv['name']}.")
            return True
        else:
            print(f"Sorry, you have not been accepted, {cv['name']}.")
            return False
    else:
        print(f"Sorry, you have not been accepted, {cv['name']}.")
        return False

def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:\n")

    desired_skills = ['CSS', 'HTML']
    
    
    check_acceptance(get_user_cv(get_skills()), desired_skills)
        

if __name__ == "__main__":
    main()

