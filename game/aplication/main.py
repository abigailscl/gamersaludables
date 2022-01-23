from game import Game

g = Game()
g.register_user()
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()