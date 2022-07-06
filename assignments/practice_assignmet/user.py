class User:
    def __init__(self, first_name, last_name, email, age, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f'first_name: {self.first_name}')
        print(f'last_name: {self.last_name}')
        print(f'email: {self.email}')
        print(f'age: {self.age}')
        print(f'is_rewards_member: {self.is_rewards_member}')
        print(f'gold_card_points: {self.gold_card_points}')

    def enroll(self):
        if self.is_rewards_member:
            print('User already a member.')
            # return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            # return True

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print('Not enough points!')
            # return False


user_a = User('peter', 'an', 'peter@gmail.com', '36')
user_b = User('esther', 'lee', 'esther@gmail.com', '30')
user_a.enroll()
user_a.display_info()
user_b.display_info()
