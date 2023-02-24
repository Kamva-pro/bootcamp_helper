'''
    This is the team allocator project solution example project
'''


def student_list():
    students = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


    return students

def edit_teams(student_list):
    result_list = []
    for i in range(0, len(student_list), 4):
        team = student_list[i:i+4]
        for j, student in enumerate(team):
            name, date, location, seat, = student.split(" - ")
            team[j] = f"{name} - {date} - {location} - {seat}"
        result_list.extend(team)
    return result_list
    

def organise_students(full_student_list, campus, isTeam):
    new_student_list = []
    if not isTeam:
        for i in full_student_list:
            if campus in i:
                 student = i.lower()
                 no_spaces = student.replace(" ", "")
                 new_student_list.append(no_spaces)
    else: 
        for i in full_student_list:
            if campus in i:
                new_student_list.append(i)
        
    
    return new_student_list

def organise(student_list, campus):
    new_student_list = []
    for i in student_list:

        if campus in i:
            new_student_list.append(i)
    return new_student_list

def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_students = []
    dbn_students = organise_students(student_list, "Durban", False)

    return dbn_students



def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = []

    cpt_students = organise_students(student_list, "Cape Town", False)

    return cpt_students



def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = []

    jhb_students = organise_students(student_list, "Johannesburg", False)

    return jhb_students




def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = []

    nw_students = organise_students(student_list, "Phokeng", False)

    return nw_students



def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_physical_students_list = []

    dbn_physical_students_list = organise_students(dbn_students, "Durban Physical", False)

    return dbn_physical_students_list



def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    result_list = []
    
    result_list = edit_teams(dbn_physical_students)
    return result_list


def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    with open('dbn_physical_teams.txt', 'w') as f:
        for team in durban_physical_teams:
            f.write(team + '\n')



def cpt_physical_students(cpt_physical_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_physical_students_list = []

    cpt_physical_students_list = organise_students(cpt_physical_students, "Cape Town Physical", False)

    return cpt_physical_students_list



def cpt_physical_teams(cpt_physical_teams_list):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    result_list = []
    result_list = edit_teams(cpt_physical_teams_list)
        
    return result_list




def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''
    with open('capetown_final_teams.txt', 'w') as f:
        for team in capetown_final_teams:
            f.write(team + '\n')


def jhb_physical_students(jhb_physical_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    jhb_physical_students_list = []

    jhb_physical_students_list = organise_students(jhb_physical_students, "Johannesburg Physical", False)

    return jhb_physical_students_list



def jhb_physical_teams(jhb_physical_team_list):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    result_list = []
    result_list = edit_teams(jhb_physical_team_list)
        
    return result_list

def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    with open('jhb_final_teams.txt', 'w') as f:
        for team in jhb_final_teams:
            f.write(team + '\n')

    


def nw_physical_students(nw_physical_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    nw_physical_students_list = []

    nw_physical_students_list = organise_students(nw_physical_students, "Phokeng Physical", False)

    return nw_physical_students_list


def nw_physical_teams(nw_physical_teams_list):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''
    result_list = []
    result_list = edit_teams(nw_physical_teams_list)
        
    return result_list


def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''
    with open('nw_final_teams.txt', 'w') as f:
        for team in nw_final_teams:
            f.write(team + '\n')


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_campus = []

    virtual_campus = organise(student_list, "Virtual")

    return virtual_campus


def virtual_teams(virtual_students_list):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''

    virtual_teams = []
    
    for i in range(0, len(virtual_students_list),4):
        virtual_teams.extend(virtual_students_list[i:i+4])
    
    odd_teams = []
    for j in virtual_teams:
        if len(j) != 4:
            odd_teams.append(j)
            

    return odd_teams

virtual_teams(get_virtual_students(student_list()))
    



def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    with open('virtual_teams.txt', 'w') as f:
        for team in virtual_teams:
            f.write(team + '\n')


if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    dbn_campus_students(student_list())
    cpt_campus_students(student_list())
    jhb_campus_students(student_list())
    nw_campus_students(student_list())
    dbn_physical_students(student_list())
    cpt_physical_students(student_list())
    dbn_physical_teams(dbn_physical_students(student_list()))
    cpt_physical_teams(cpt_physical_students(student_list()))
    jhb_physical_students(student_list())
    jhb_physical_teams(jhb_physical_students(student_list()))
    nw_physical_teams(nw_physical_students(student_list()))
    get_virtual_students(student_list())
    

    pass


