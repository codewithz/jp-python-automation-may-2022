# You’re a teacher who has just graded your students on a recent test.
# Unfortunately, you may have made the test too challenging,
#  and most of the students did worse than expected.
# To help everybody out, you’re going to curve everyone’s grades.

# It’ll be a relatively rudimentary curve, though.
# You’ll take whatever the average score is and declare that a C.
#  Additionally, you’ll make sure that the curve doesn’t
# accidentally hurt your students’ grades
# or help so much that the student does better than 100 % .

import numpy as np

CURVE_CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])


def curve(grades):
    average = grades.mean()
    change = CURVE_CENTER-average
    new_grades = grades+change
    return np.clip(new_grades, grades, 100)


print("O:", grades)
print("After Curve:", curve(grades))
