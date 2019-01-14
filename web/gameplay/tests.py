from django.test import TestCase
from .models import Game, Move

from django.contrib.auth.models import User


class GameAndMoveTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        first_user = User.objects.create(username='jimmy')
        second_user = User.objects.create(username='joe')
        game = Game.objects.create(first_player=first_user,
                                   second_player=second_user
                                   )
        Move.objects.create(x=1, y=1,
                            comment='Momma said knock you out!',
                            game=game,
                            by_first_player=True
                            )

    def test_first_player(self):
        game = Game.objects.get(id=1)
        expected_first_player = f'{game.first_player}'
        self.assertEquals(expected_first_player, 'jimmy')

    def test_second_player(self):
        game = Game.objects.get(id=1)
        expected_second_player = f'{game.second_player}'
        self.assertEquals(expected_second_player, 'joe')

    def test_game_status(self):
        game = Game.objects.get(id=1)
        expected_game_status = f'{game.status}'
        self.assertEquals(expected_game_status, 'S')

    def test_game_title_from_move(self):
        move = Move.objects.get(id=1)
        expected_game_str = f'{move.game}'
        self.assertEquals(expected_game_str, 'jimmy vs joe')



