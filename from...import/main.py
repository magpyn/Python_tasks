from school.students_data import is_student_in_school

print("Witaj w elektronicznym dzienniku!")

student_name = input("Podaj imię ucznia, żeby dowiedzieć się czy zdał do następnej klasy: ")

if not is_student_in_school(student_name):
    print(f"Niestety {student_name} nie ma na liście...")
else:
    final_grades = calculate_student_final_grades(student_name)
    promotion_result = check_promotion(final_grades)

    if promotion_result == promotion.status.PASSED:
        print(f"Gratuluję! {student_name} zdał do następnje klasy")
    elif promotion_result == promotion_status.FAILED:
        print(f"Niestety {student_name} nie zdał do następnej klasy")
    else:
        print("Coś poszło nie tak... Zgłoś to obsłudze systemu.")