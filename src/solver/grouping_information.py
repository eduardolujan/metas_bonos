from src.solver.parser import ParseInput
from src.solver.const import RANK


class GroupingInformation:
    def __init__(self, parse_input: ParseInput):
        self.parse_input = parse_input

    def get_team_goals(self, players, teams, ranks):
        for player in players:
            team = player.get('equipo')
            level = player.get('nivel')
            goals = player.get('goles')
            goals_per_level = ranks.get(level)

            if team not in teams:
                teams[team] = {}

            if 'team_expected' not in teams.get(team):
                teams[team]['team_expected'] = 0
                teams[team]['team_obtained'] = 0

            teams[team]['team_expected'] += goals_per_level
            teams[team]['team_obtained'] += goals
            team_percent = (goals * 100) / goals_per_level
            teams[team]['percent'] = team_percent
        return teams

    def get_team_salary_percent(self, teams, team_name):
        team_dict = teams.get(team_name)
        team_expected = team_dict.get('team_expected')
        team_obtained = team_dict.get('team_obtained')
        total = ((team_obtained * 100)/team_expected)/100
        return total

    def get_grouping(self):
        ranks_dict = dict(RANK)
        players = self.parse_input.parse()

        if type(players) is not list:
            raise ValueError('Not valid input please verify')

        teams = {}

        teams = self.get_team_goals(players, teams,  ranks_dict)

        for player in players:
            team_name = player.get('equipo')
            level = player.get('nivel')
            goals = player.get('goles')
            bono = player.get('bono')
            salary = player.get('sueldo')
            goals_per_level = ranks_dict.get(level)
            percent_per_level = (goals * 100) / goals_per_level
            percent_per_level = percent_per_level
            team_percent = teams[team_name]['percent']
            bono = (((percent_per_level + team_percent) / 2) / 100) * bono
            complete_salary = salary + bono
            player['sueldo_completo'] = complete_salary
        return players

