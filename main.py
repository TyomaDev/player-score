import GameDataHandler

if __name__ == '__main__':
    print(f"Средний бал участников- {GameDataHandler.get_average_player_score('DATA.csv')}")
    print(f"Средний бал в раундах- {GameDataHandler.get_average_round_score('DATA.csv')}")
