DISTINCTION = 1
PASS_2 = 2
PASS_3 = 3
PASS_4 = 4


# MY GRADES
# [[year1], [year2], [year3]]
# Each year = (credits, pass_level)

my_grades = [[(30, 1),(30, 1),(30, 1),(30, 1)],
             [(30, 4),(30, 4),(30, 4),(30, 1)],
             [(30, 1),(30, 1),(30, 1),(30, 1)],
            ]

def percent_to_grade(percent):
    """ Convert percentage to grade
        Input: float
        Output: int
    """
    if percent >= 85:
        return DISTINCTION
    elif percent >= 70:
        return PASS_2
    elif percent >= 55:
        return PASS_3
    elif percent >= 40:
        return PASS_4
    

def get_weighted_credits(course_credits, year_multiplier):
    """ Converts credits & year, to credits with multiplier
        Input: int, int (0,1,2)
        Output: int
    """
    return course_credits * year_multiplier

def get_credits(grades):
    """ Get credits earned
        Input: list of list of grades
               [[year1], [year2], [year3]]
               where each year is a tuple:
                   (course_credits, grade)
        Output: int
    """
    total_credits = 0
    for year_multiplier, year_grades in enumerate(grades):
        for grade in year_grades:
            total_credits += get_weighted_credits(grade[0], year_multiplier) * grade[1]
    return total_credits
        
        

def quality_assurance(grades):
    """
    First class at least 60 credits at Distinction grade
    Upper second class 61 to 120 grade credits
    Lower second class 121 to 180 grade credits
    Third class 181 to 240 grade credits

    Input: list of list of grades
           [[year1], [year2], [year3]]
    Output: grade
    """
    my_credits = {DISTINCTION: 0,
                  PASS_2: 0,
                  PASS_3: 0,
                  PASS_4: 0}
    running_total = 0
    for grade in grades[2]:
        my_credits[grade[1]] += grade[0] * grade[1]

    running_total += my_credits[DISTINCTION]
    if running_total >= 60:
        return DISTINCTION

    running_total += my_credits[PASS_2]
    if running_total >= 61:
        return PASS_2

    running_total += my_credits[PASS_3]
    if running_total >= 121:
        return PASS_3

    running_total += my_credits[PASS_4]
    if running_total >= 181:
        return PASS_4


def credits_to_grades(total_credits):
    """ Convert total credits to grade classification
        Input: int
        Output: int (1,2,3,4)
    """
    if total_credits <= 630:
        return DISTINCTION
    elif total_credits <= 900:
        return PASS_2
    elif total_credits <= 1170:
        return PASS_3
    elif total_credits <= 1440:
        return PASS_4


def get_final_classifaction(grades):
    """ Return final classification from all grades
        Input: list of list of grades
               [[year1], [year2], [year3]]
               where each year is a tuple:
                   (course_credits, grade)
        Output: int (1,2,3,4)
    """
    return max(credits_to_grades(get_credits(grades)), quality_assurance(grades))
        
if __name__ == "__main__":
    print(get_final_classifaction(my_grades))

        
