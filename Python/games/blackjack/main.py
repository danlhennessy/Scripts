from deck import deck
from player import player


class blackjack:
    def __init__(self):
        self.player = player(0)
        self.deck = deck()
        
    # Initialise game, create resources, create loop to run game until 21, deal cards
    def run(self):
        self.deck.buildDeck()
        self.deck.shuffle()
        curcard = self.deck.drawcard()
        curcard.showcard()
        self.player.curval += curcard.value
        self.player.turn(self.deck)




if __name__ == '__main__':
    game = blackjack()
    game.run()
