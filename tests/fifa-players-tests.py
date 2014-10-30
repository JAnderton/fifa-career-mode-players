import json

import BeautifulSoup

import fcmp.build_player_index


def test_find_players():
    output_tuples = fcmp.build_player_index.find_players(
        BeautifulSoup.BeautifulSoup(open('resources/html/players-0.html', 'r').read()))

    actual = __tuples_to_json__(output_tuples)
    expected = json.loads(open('resources/data/find_players_test_data.json', 'r').read())
    assert actual.__eq__(expected)


def __tuples_to_json__(tuple_array):
    dictionary = {
        'name': [],
        'url': [],
        'status': []
    }

    for tuple_element in tuple_array:
        dictionary['name'].append(tuple_element[0])
        dictionary['url'].append(tuple_element[1])
        dictionary['status'].append(tuple_element[2])

    return json.dumps(dictionary)