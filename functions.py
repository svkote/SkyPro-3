from json import load


def load_candidates():
    """Загружает и возвращает данные из файла"""
    filename = 'candidates.json'

    with open(filename, encoding="utf-8") as file:
        data = load(file)

    return data


def get_all() -> list:
    """Возвращает список всех кандидатов"""
    data = load_candidates()
    candidates = []

    for candidate in data:
        candidates.append(candidate['name'])

    return candidates


def get_by_pk(pk) -> dict or str:
    """Возвращает кандидата по pk"""
    data = load_candidates()

    for candidate in data:
        if candidate['pk'] == pk:
            return candidate

    return 'Такого кандидата нет'


def get_by_skill(skill_name) -> list:
    """Возвращает кандидатов по навыку"""
    data = load_candidates()
    candidates = []

    for candidate in data:
        if skill_name in candidate['skills']:
            candidates.append(candidate['name'])

    return candidates

# data = load_candidates('candidates.json')
# get_all(data)
