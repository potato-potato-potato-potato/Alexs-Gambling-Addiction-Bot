import random

from .discordSendUtil import prompt
from .discordSendUtil import combine_strings


class __Player:

    def __init__(self, perfect_points, __cards, __card_types, name=""):
        self.perfect_points = perfect_points
        self.__cards = __cards
        self.__card_types = __card_types
        self.name = name

        self.cards = []
        self.points = 0

    def pull_new_card(self, hidden=False):
        card, points = random.choice(list(self.__cards.items()))
        card_type = random.choice(self.__card_types)

        self.cards.append(Card(f'**{card}**{card_type}', points, hidden))
        self.points += points

    def check_for_perfect_win(self):
        if self.points == self.perfect_points:
            return True
        return False

    def check_for_win(self, other_points):
        if self.points > other_points:
            return True
        return False

    def check_for_bust(self):
        if self.points > self.perfect_points:
            return True

    def get_card_print(self):
        cards = ' '.join([card.get_card_name() for card in self.cards])
        return f'**{self.name}**: {cards}'

    def flip(self, index, hidden=False):
        self.cards[index].flip(hidden)

    def reset(self):
        self.points = 0
        self.cards = []


class __Dealer(__Player):

    def ai_play(self, player_points):
        while (self.points < (self.perfect_points - 5)) and (self.points < player_points):
            self.pull_new_card()


class Card:
    def __init__(self, card, points, hidden=False):
        self.card = card
        self.points = points
        self.hidden = hidden

    def flip(self, hidden=False):
        self.hidden = hidden

    def get_card_name(self):
        if self.hidden:
            return f":grey_question:{self.card[self.card.index(':'):]}"
        else:
            return self.card


__cards = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

__card_types = [":hearts:", ":diamonds:", ":clubs:", ":spades:"]



async def black_jack(__ctx, __client):

    player = __Player(21, __cards, __card_types, name=__ctx.author.name)
    dealer = __Dealer(21, __cards, __card_types, name='Dealer')


    playing = True
    while playing:
        await __ctx.send(f"{__ctx.author.mention}, enter **QUIT** anytime to leave $$$$$$")

        dealer.pull_new_card()
        dealer.pull_new_card(hidden=True)
        while True:

            player.pull_new_card()

            await print_cards(__ctx, player, dealer)

            if player.check_for_bust():
                await __ctx.send(__ctx.author.mention + " BUST!")
                break
            elif player.check_for_perfect_win():
                await __ctx.send(__ctx.author.mention + "You win!!")
                break

            # Keeps looping until a valid msg is passed
            # if you get a valid msg, save the value
            h_s = await prompt(__client, __ctx, question_to_prompt='Enter **h** for hit or **s** for stand: ',
                               valid_answers=['h', 's', 'quit'], str=True)

            # VERY VERY VERY UGLY CODE
            if h_s == "s":
                dealer.ai_play(player.points)
                dealer.flip(1)

                await print_cards(__ctx, player, dealer)
                if dealer.check_for_bust():
                    await __ctx.send(dealer.name + " BUST!")
                    await __ctx.send(__ctx.author.mention + "You win!!")

                elif player.check_for_win(dealer.points):
                    await __ctx.send(__ctx.author.mention + "You win!!")

                else:
                    await __ctx.send(__ctx.author.mention + "You lose!!")
                break
            elif h_s == 'quit':
                break
        choice = await prompt(__client, __ctx, question_to_prompt='Do you want to play a new game? (Yes, No)',
                              valid_answers=['y', 'yes', 'n', 'no'], str=True)
        if choice == "yes" or choice == 'y':
            player.reset()
            dealer.reset()
        else:
            playing = False


async def print_cards(__ctx, player, dealer):
    final_string = combine_strings(player.get_card_print() + "\n", dealer.get_card_print())
    await __ctx.send(final_string)