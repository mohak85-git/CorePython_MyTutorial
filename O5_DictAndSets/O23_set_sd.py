morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

possible_courses = morning ^ afternoon
print(possible_courses)

morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

# the symmetric difference is not defined for lists so we have to type cast
# to set.
possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)
