import json
DATA_PATH = "data/candidates.json"


def load_candidates_from_json(path=DATA_PATH):
    """Возвращает список всех кандидатов"""

    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_candidates_all():
    candidates = load_candidates_from_json()
    return candidates

#print(load_candidates_from_json())


def get_candidate_id(candidate_id):
    """Получает кандидатао id"""
    candidates = load_candidates_from_json(path=DATA_PATH)
    for candidate in candidates:
        if candidate.get("id") == candidate_id:
            return candidate

#print (get_candidate(3))


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""

    candidates = load_candidates_from_json()
    candidates_list = []
    for candidate in candidates:
        if candidate_name in candidate["name"].split():
            candidates_list.append(candidate)
    return candidates_list

# print(get_candidates_by_name("Day"))


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навык"""

    candidates = load_candidates_from_json()  # получаем кандидатов из функции
    candidates_skill = []  # список кандидатов по навыкам
    skill_name = skill_name.lower()

    for candidate in candidates:
        skills = candidate["skills"].lower().strip().split(", ")
        if skill_name in skills:
            candidates_skill.append(candidate)
    return candidates_skill


# print(get_candidates_by_skill("django"))