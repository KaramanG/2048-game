from json import load, dump
highest_score_path = 'files/highest_score.json'
def get_highscore():
        try:
            with open(highest_score_path, 'r') as file:
                return load(file)
        except FileNotFoundError:
            with open(highest_score_path, 'w') as file:
                dump(0, file)
            return 0
        
def set_highscore(new_high_score):
    with open(highest_score_path, 'w') as file:
        dump(new_high_score, file)