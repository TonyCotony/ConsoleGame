from envs import field_dict, players_points


def check_winner() -> bool:
    for row_count in field_dict.values():
        horizontal_streak = 0
        vertical_streak: dict[int: dict] = {}
        for idx, value in enumerate(field_dict[row_count]):
            horizontal_streak += 1 if value in players_points.values() else 0
            if horizontal_streak >= 4:
                return True

            # higher_row_mark =

            if field_dict[row_count - 1][idx] == field_dict[row_count][idx]:
                vertical_streak.update({row_count: 1})

            if vertical_streak[row_count - 1][idx]['mark'] == field_dict[row_count][idx]:
                try:
                    v_count = vertical_streak[row_count - 1][idx]['v_count'] + 1
                except KeyError:
                    v_count = 0
                if v_count >= 4:
                    return True
                vertical_streak.update({
                    row_count: {idx: {
                        'mark': field_dict[row_count][idx],
                        'v_count': v_count,
                    }}})


def change_game_field(column: int, row: int, mark: str):
    field_dict[column][row] = mark


def calculate_new_marked_row(turn_column_number: int) -> int:
    for key in field_dict.keys():
        if field_dict[key][turn_column_number] in players_points.values():
            return key - 1


def get_new_turn_input(player: str) -> int | None:
    while True:
        input_data = input(f'{player}, Ваш ход. Выберите поле для хода (введите число от 1 до 8):\n')
        if int(input_data) in field_dict[' ']:
            return int(input_data)


def start_game():
    game_status: bool = True
    count: int = 0  # чтобы получать корректный результат от %
    while game_status:
        for field in field_dict.values():
            print(field)
        player = 'Второй игрок'
        if count % 2 == 0:
            player = 'Первый игрок'
        column_turn: int = get_new_turn_input(player)
        new_row_to_mark = calculate_new_marked_row(column_turn - 1)
        change_game_field(column_turn, new_row_to_mark, players_points[player])


start_game()
