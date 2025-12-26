def process_league_stats(filename):
    result = {}
    list_of_MVP = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")
            try:
                player = parts[0]
                team = parts[1]
                goals = int(parts[2])
                assists = int(parts[3])
            except IndexError:
                continue
            except ValueError:
                continue
            total = goals + assists
            if team not in result:
                result[team] = 0
            result[team] += total
            if total > 15:
                list_of_MVP.append([player, total])
    return result, list_of_MVP


def generate_season_summary(team_totals, mvp_list):
    with open("season_summary.txt", "w") as f:
        f.write("TEAM PERFORMANCE (Total Contributions)\n")
        f.write("--------------------------------------\n")
        for team in team_totals:
            f.write(team + ": " + str(team_totals[team]) + "\n")
        f.write("\n")
        f.write("MVP CANDIDATES (> 15 contribs)\n")
        f.write("------------------------------\n")
        for item in mvp_list:
            f.write(item[0] + " (" + str(item[1]) + ")\n")
teams, mvp_players = process_league_stats("soccer_stats.txt")
generate_season_summary(teams, mvp_players)
