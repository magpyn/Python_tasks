class GradeCalculator:

    MAX_FAILING_GRADES_TO_PASS = 2

    @staticmethod
    def check_student_promotion(final_grades):
        failing_grades = GradeCalculator.get_number_of_failing_grades(final_grades)
        if failing_grades > GradeCalculator.MAX_FAILING_GRADES_TO_PASS:
            return False
        return True

    @staticmethod
    def calculate_student_avg(final_grades):
        grade_sum = 0
        for grade in final_grades:
            grade_sum += grade.value
        return grade_sum / len(final_grades)
