players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]


class Player:
    new_team = []

    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
        self.new_team.append(self)

    @classmethod
    def add_players(cls, players):
        player_info = []
        for player in players:
            player_info.append(cls(player))
        return player_info

    @classmethod
    def get_team(cls, team_list):
        for player in team_list:
            Player(player)

    @classmethod
    def display_team(cls):
        for team_list in (cls.new_team):
            print(
                f"Player Name: {team_list.name}  Age: {team_list.age}  Position: {team_list.position}  Team: {team_list.team}")

    # def display_player_info(self):
    #     print(
    #         f"Player Name: {self.name}  Age: {self.age}  Position: {self.position}  Team: {self.team}")

#     @classmethod
#     def add_players(cls, data):
#         player_info = []
#         for info in data:
#             player_info.append(cls(info))
#         return player_info


# kevin = {
#     "name": "Kevin Durant",
#     "age": 34,
#     "position": "small forward",
#     "team": "Brooklyn Nets"
# }
# jason = {
#     "name": "Jason Tatum",
#     "age": 24,
#     "position": "small forward",
#     "team": "Boston Celtics"
# }
# kyrie = {
#     "name": "Kyrie Irving",
#     "age": 32, "position": "Point Guard",
#     "team": "Brooklyn Nets"
# }

# player_jason = Player(jason)
# player_kevin = Player(kevin)
# player_kyrie = Player(kyrie)
# player_jason.display_player_info()
# player_kevin.display_player_info()
# player_kyrie.display_player_info()


# player_kevin=Player(players[0])

# player_kevin.display_player_info()


Player.get_team(players)
Player.display_team()
