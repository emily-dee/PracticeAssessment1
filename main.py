all_projects = dict[str, list]()
project_count = int(input("How many projects would you like to create? "))

for project in range(project_count):
    project_name = input('Please enter a project title: ')
    all_projects[project_name] = []

def add_people(project_dictionary: dict):
    for project in project_dictionary:
        name_list = list[str]()
        print(f'Time to add three people to project {project}')
        for person in range(3):
            student_name = input('Next name please: ')
            name_list.append(student_name)
        project_dictionary[project] = name_list

def print_projects(project_dictionary: dict):
    for project, name_list in project_dictionary.items():
        print(f'Here are the people in project {project}:')
        for name in name_list:
            print(name)


# Please type your code above this line

add_people(all_projects)
print_projects(all_projects)
