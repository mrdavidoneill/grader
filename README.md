# Open University Degree Grader

A grader to find out your final degree classification

## Instructions

Use the my_grades list to input your grades with the following shape:<br />
my_grades = [[YEAR1], [YEAR2], [YEAR3]]<br />
where each YEAR is a tuple of "course credits" and "pass grade" attained.<br />
eg. (30, 1) for a distinction on a course worth 30 credits

## Reference

The document "Working out your Class of Honours" (Open University, 2016) was used to determine classification.<br />
https://help.open.ac.uk/documents/policies/working-out-your-class-of-honours/files/50/honours-class-working-out.pdf

## Testing

A simple test file is included which confirms that:

- all distinction, gets a 1st
- all pass level 2 gets a 2:1
- all pass level 3 gets a 2:2
- all pass level 4 gets a 3rd
- the example student Maddie, gets a 2:2 (with quality assurance at 2:1)
- the example student Rajiv, gets a 2:1 (with quality assurance at 2:1)
