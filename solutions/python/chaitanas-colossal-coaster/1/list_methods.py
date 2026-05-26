def add_me_to_the_queue(express_queue: list, normal_queue: list, ticket_type: int, person_name: str):
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue: list, friend_name: str) -> int:
    return queue.index(friend_name)


def add_me_with_my_friends(queue: list, index: int, person_name: str) -> list:
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue: list, person_name: str):
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue: list, person_name: str):
    return queue.count(person_name)


def remove_the_last_person(queue: list):
    return queue.pop()


def sorted_names(queue: list):
    return sorted(queue)
