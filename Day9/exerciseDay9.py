#grading system for students
student_scores ={
    "Tony" : 99,
    "Banner" : 90,
    "Natasha" : 67,
    "Hulk" : 2,
    "Steve" : 40,
}
new_student_grades = {}
for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <=100:
        new_student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <=90:
        new_student_grades[key] = "Exceeds Expectation"
    elif student_scores[key] >= 71 and student_scores[key] <=80:
        new_student_grades[key] = "Acceptable"

    else:
        new_student_grades[key] = "Fail"

print(new_student_grades)


#travel log

travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ["Paris","Lille","Renne","Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 3,
        "cities" : ["Berlin", "Hamburg", "Frankfurt"]
    },
]
print(travel_log,"\n")

def add_new_country(country,t_visit,list_cities):
    travel_log.append({"country" : country, "visits" : t_visit , "cities" : list_cities })

add_new_country("Russia" , 2 , ["Moscow", "Saint Petersburg"])
print(travel_log)
