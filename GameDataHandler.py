import csv


def get_file_data(path: str) -> list:
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        return data


def get_sportsman_scores(sportsmen_list: list) -> list:
    data = []
    for sportsman in sportsmen_list:
        sportsman_name = ''
        steps = []
        for key, value in sportsman.items():
            if key == 'sportsm':
                sportsman_name = value
            elif 'step' in key:
                steps.append({key: value})
        data.append({sportsman_name: steps})
    return data


def get_average_player_score(path: str) -> list:
    sportsmen_list = get_file_data(path)
    sportsman_scores = get_sportsman_scores(sportsmen_list)

    data = []
    for sportsman in sportsman_scores:
        name = ''
        steps = []
        for key, value in sportsman.items():
            steps = value
            name = key

        scores = 0
        count = 0
        for step in steps:
            for k, v in step.items():
                scores += float(v)
                count += 1

        average_score = round(scores / count, 2)
        data.append({name: average_score})

    return data


def get_average_round_score(path: str):
    steps = []
    for v in get_file_data(path):

        for key, value in v.items():
            if 'step' in key:
                steps.append({key: value})

    sums = {}
    counts = {}
    for step in steps:
        for key, value in step.items():
            num_value = float(value)
            if key in sums:
                sums[key] += num_value
                counts[key] += 1
            else:
                sums[key] = num_value
                counts[key] = 1
    averages_scores = {key: round(sums[key] / counts[key], 2) for key in sums}
    return averages_scores
