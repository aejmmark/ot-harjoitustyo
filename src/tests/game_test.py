
import unittest
import game
import pygame

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()
        self.game.start()

    def test_jump(self):
        self.pos = self.game.player.pos.y
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
        self.game.run(10)
        self.new_pos = self.game.player.pos.y
        self.game.quit_game()
        self.assertTrue(self.new_pos < self.pos)
    
    def test_left_movement(self):
        self.pos = self.game.player.pos.x
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.run(10)
        self.new_pos = self.game.player.pos.x
        self.game.quit_game()
        self.assertTrue(self.new_pos < self.pos)

    def test_right_movement(self):
        self.pos = self.game.player.pos.x
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        self.game.run(10)
        self.new_pos = self.game.player.pos.x
        self.game.quit_game()
        self.assertTrue(self.new_pos > self.pos)

    def test_win_condition(self):
        self.pos = self.game.player.pos.x
        self.game.new_event(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.run(200)
        self.new_pos = self.game.player.pos.x
        self.game.quit_game()
        self.assertTrue(self.new_pos < self.pos)

    def test_quitting_wont_win(self):
        self.game.run(10)
        self.game.quit_game()
        self.assertFalse(self.game.win)
