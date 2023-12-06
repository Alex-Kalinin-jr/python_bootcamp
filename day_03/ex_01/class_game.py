from collections import Counter


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        player1.history.clear()
        player2.history.clear()
        for _ in range(self.matches):
            x = player1.play_round(player2)
            y = player2.play_round(player1)
            if x and y:
                self.registry[player1.name] += 2
                self.registry[player2.name] += 2
            elif x and not y:
                self.registry[player1.name] += 3
                self.registry[player2.name] -= 1
            elif y and not x:
                self.registry[player2.name] += 3
                self.registry[player1.name] -= 1
            else:
                pass
            player1.add(x)
            player2.add(y)

    def top3(self):
        return self.registry.most_common(3)


class Player():

    def __init__(self, buff_name):
        self.history = []
        self.name = buff_name

    def get_last_action(self):
        if len(self.history) == 0:
            return None
        return self.history[-1]

    def get_last_action_range(self, count):
        if len(self.history) < count:
            return None
        return self.history[-count:]

    def add(self, round):
        self.history.append(round)


class Cheater(Player):

    def __init__(self, buff_name):
        super().__init__(buff_name)

    def play_round(self, other: Player):
        return False


class Cooperator(Player):

    def __init__(self, buff_name):
        super().__init__(buff_name)

    def play_round(self, other: Player):
        return True


class Copycat(Player):

    def __init__(self, buff_name):
        super().__init__(buff_name)

    def play_round(self, other: Player):
        if  other.get_last_action() is None:
            return True
        return other.get_last_action()


class Grudger(Player):

    def __init__(self, buff_name):
        super().__init__(buff_name)

    def play_round(self, other: Player):
        if (other.get_last_action() is None or
        (self.get_last_action() is True and other.get_last_action() is True)):
            return True
        return False


class Detective(Player):

    def __init__(self, buff_name):
        super().__init__(buff_name)
        self.checker = None

    def play_round(self, other: Player):
        if len(self.history) in [0, 1, 2, 3]:
            return len(self.history) != 1
        elif len(self.history) == 4:
            if False in other.get_last_action_range(4):
                self.checker = 'Copypat'
            else:
                self.checker = 'Cheater'

        if self.checker == 'Copypat':
            if  other.get_last_action() is None:
                return True
            return other.get_last_action()

        if self.checker == 'Cheater':
            return False


class Custom(Player):

    def __init__(self, buff_name):
        super().__init__(buff_name)

    def play_round(self, other: Player):
        if  other.get_last_action() is None:
            return False
        return not other.get_last_action()

def main():
    players = [Cooperator('Cooperator'),
               Detective('Detective'),
               Cheater('Cheater'),
               Grudger('Grudger'),
               Copycat('Copycat')]
    my_sec_game = Game()

    for i in players:
        for j in players:
            if i != j:
                my_sec_game.play(i, j)

    print('RESULTS OF GAME TOUR')
    print(my_sec_game.top3())

    players.append(Custom('custom'))

    for i in players:
        for j in players:
            if i != j:
                my_game = Game()
                my_game.play(i, j)
                print('RESULTS OF 1 vs 1 GAME TOUR')
                print(my_game.top3())

if __name__ == '__main__':
    main()
