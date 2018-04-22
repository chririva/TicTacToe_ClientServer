from unittest import TestCase
from TicTacToe import TicTacToe


class TestGame(TestCase):
    def test_right_name1(self):
        game = TicTacToe()
        name = 'Bob'
        game.set_name_player1(name)
        self.assertEqual(name, game.get_name_player1())

    def test_right_name2(self):
        game = TicTacToe()
        name = 'Bob'
        game.set_name_player2(name)
        self.assertEqual(name, game.get_name_player2())

    def test_is_free(self):
        game = TicTacToe()
        result = game.is_free(1);
        ex_result = True;
        self.assertEqual(result, ex_result)

    def test_is_free1(self):
        game = TicTacToe()
        game.put_choice(2, 4)
        result = game.is_free(4);
        ex_result = False;
        self.assertEqual(result, ex_result)

    def test_symbol1(self):
        game = TicTacToe()
        self.assertEqual(game.set_symbol1('X'),True)

    def test_symbol2(self):
        game = TicTacToe()
        self.assertEqual(game.set_symbol2('O'), True)

    def test_get_next1(self):
        game = TicTacToe()
        self.assertEqual(game.get_next(), 1)

    def test_get_next2(self):
        game = TicTacToe()
        game.put_choice(1, 100)
        self.assertEqual(game.get_next(), 1)

    def test_get_next3(self):
        game = TicTacToe()
        game.put_choice(2, 1)
        self.assertEqual(game.get_next(), 1)

    def test_get_next4(self):
        game = TicTacToe()
        game.put_choice(1, 8)
        self.assertEqual(game.get_next(), 2)

    def test_game1(self):
        game = TicTacToe()
        game.put_choice(1, 1)
        game.put_choice(2, 2)
        game.put_choice(1, 5)
        game.put_choice(2, 7)
        game.put_choice(1, 9)
        game.put_choice(2, 4)
        self.assertEqual(game.status_of_the_match(), 1)

    def test_game2(self):
        game = TicTacToe()
        game.put_choice(1, 1)
        game.put_choice(1, 2)
        game.put_choice(1, 3)
        self.assertEqual(game.status_of_the_match(), 1)

    def test_game3(self):
        game = TicTacToe()
        game.put_choice(2, 1)
        game.put_choice(2, 4)
        game.put_choice(1, 10)
        game.put_choice(1, 3)
        game.put_choice(2, 7)
        self.assertEqual(game.status_of_the_match(), 2)

    def test_game4(self):
        game = TicTacToe()
        game.put_choice(2, 2)
        game.put_choice(2, 6)
        game.put_choice(2, 9)
        game.put_choice(2, 7)
        game.put_choice(1, 8)
        game.put_choice(1, 5)
        game.put_choice(1, 4)
        game.put_choice(1, 3)
        game.put_choice(1, 1)
        self.assertEqual(game.status_of_the_match(), 3)

    def test_game4(self):
        game = TicTacToe()
        game.put_choice(2, 2)
        game.put_choice(2, 6)
        game.put_choice(2, 9)
        game.put_choice(2, 7)
        self.assertEqual(game.status_of_the_match(), 0)

