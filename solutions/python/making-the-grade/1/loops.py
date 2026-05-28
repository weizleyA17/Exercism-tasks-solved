def round_scores(student_scores: list):
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    failed_Students = []
    for score in student_scores:
        if score <= 40:
            failed_Students.append(score)
    return len(failed_Students)


def above_threshold(student_scores, threshold):
    above = []
    for score in student_scores:
        if score >= threshold:
            above.append(score)
    return above


def letter_grades(highest):
    step = (highest - 40) // 4
    return [41 + (i * step) for i in range(4)]


def student_ranking(student_scores: list, student_names: list) -> list:
    result = []
    for index, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        # Monta a string no formato certinho
        ranking_string = f"{index}. {name}: {score}"

        # Adiciona na nossa lista de resultados
        result.append(ranking_string)

    return result


def perfect_score(student_info):
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
