from grader import *

DISTINCTION = 1
PASS_2 = 2
PASS_3 = 3
PASS_4 = 4

      
distinction = [[(30, 1),(30, 1),(30, 1),(30, 1)],
               [(30, 1),(30, 1),(30, 1),(30, 1)],
               [(30, 1),(30, 1),(30, 1),(30, 1)],
              ]

pass_2 = [[(30, 2),(30, 2),(30, 2),(30, 2)],
          [(30, 2),(30, 2),(30, 2),(30, 2)],
          [(30, 2),(30, 2),(30, 2),(30, 2)],
         ]

pass_3 = [[(30, 3),(30, 3),(30, 3),(30, 3)],
          [(30, 3),(30, 3),(30, 3),(30, 3)],
          [(30, 3),(30, 3),(30, 3),(30, 3)],
         ]

pass_4 = [[(30, 4),(30, 4),(30, 4),(30, 4)],
          [(30, 4),(30, 4),(30, 4),(30, 4)],
          [(30, 4),(30, 4),(30, 4),(30, 4)],
         ]

maddie = [[(30, 4), (30, 4)],
          [(60, 3), (60, 3), (60, 2)],
          [(60, 3), (60, 2)],
         ]

maddie = [[(30, 4), (30, 4)],
          [(60, 3), (60, 3), (60, 2)],
          [(60, 3), (60, 2)],
         ]

rajiv = [[(60, 4),(30, 4), (30, 2)],
         [(30, 2),(30, 1), (60, 2)],
         [(30, 1),(30, 3), (30, 2), (30, 3)],
        ]

assert get_weighted_credits(30, 0) == 0
assert get_weighted_credits(30, 1) == 30
assert get_weighted_credits(30, 2) == 60

assert get_credits(distinction) == 360
assert get_credits(pass_2) == 720
assert get_credits(pass_3) == 1080
assert get_credits(pass_4) == 1440

assert quality_assurance(distinction) == DISTINCTION
assert quality_assurance(pass_2) == PASS_2
assert quality_assurance(pass_3) == PASS_3
assert quality_assurance(pass_4) == PASS_4
assert quality_assurance(maddie) == PASS_2
assert quality_assurance(rajiv) == PASS_2

assert credits_to_grades(630) == DISTINCTION
assert credits_to_grades(900) == PASS_2
assert credits_to_grades(1170) == PASS_3
assert credits_to_grades(1440) == PASS_4

assert get_final_classifaction(distinction) == DISTINCTION
assert get_final_classifaction(pass_2) == PASS_2
assert get_final_classifaction(pass_3) == PASS_3
assert get_final_classifaction(pass_4) == PASS_4

assert get_final_classifaction(maddie) == PASS_3
assert get_final_classifaction(rajiv) == PASS_2

assert grade_to_classification(1) == "1st"
assert grade_to_classification(2) == "2:1"
assert grade_to_classification(3) == "2:2"
assert grade_to_classification(4) == "3rd"

print("ALL TESTS PASSED".center(80, "-"))
