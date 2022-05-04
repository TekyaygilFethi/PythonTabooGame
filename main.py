import preparejson
import json
import random as rnd


class Team:
    def __init__(self, name):
        self.score = 0
        self.name = name


def main():
    # preparejson.prepare_json()
    loaded_dict = json.load(open(f"all_data.json", encoding="utf-8"))
    keys = list(loaded_dict.keys())

    team1 = Team("Team 1")

    team2 = Team("Team 2")

    teams = [team1, team2]

    limit_score = int(input("Enter your limit score: "))

    choice = None
    idx = 0

    while choice != "q" and (limit_score >= team1.score or limit_score >= team2.score):
        print()
        print("Team1 Score:", team1.score)
        print("Team2 Score:", team2.score)
        print()
        choice = input("q to exit, any key to play: ")
        if choice == "q":
            break
        current_team = teams[idx % 2]
        print()
        print(current_team.name, "Starts...")
        print("-" * 30)
        for key in keys:
            rnd.shuffle(keys)
            print()
            print("Kelime: ", key)
            print("Yasaklı kelimeler: ", loaded_dict[key])
            in_choice = input("1.Tabu!\n2.Pas!\n3.Doğru!\n4.Süre bitti!\nSeçim: ")

            if in_choice == "1":
                current_team.score -= 10
                if current_team.score < 0:
                    current_team.score = 0
            elif in_choice == "2":
                continue
            elif in_choice == "3":
                current_team.score += 10
                if current_team.score >= limit_score:
                    print(current_team.name, "has won the game!")
                    choice = "q"
                    break
            else:
                break
        idx += 1


main()
