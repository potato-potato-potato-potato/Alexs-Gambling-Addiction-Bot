import random

from .discordSendUtil import prompt


class __Player:

    def __init__(self, perfect_points, __cards, __card_types, name="", dealer=False):
        self.perfect_points = perfect_points
        self.__cards = __cards
        self.__card_types = __card_types
        self.name = name
        self.dealer = dealer

        self.points = 0
        self.cards_print = f'**{self.name}**: '

    def pull_new_card(self):
        card, points = random.choice(list(self.__cards.items()))
        card_type = random.choice(self.__card_types)

        self.cards_print += f'**{card}**{card_type} '
        self.points += points

    def check_for_win(self):
        if self.points == self.perfect_points:
            return True

    def check_for_bust(self):
        if self.points > self.perfect_points:
            return True

    def get_card_print(self):
        return self.cards_print

    def reset(self):
        self.points = 0
        self.cards_print = f'**{self.name}**: '
        


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
    dealer = __Player(21, __cards, __card_types, name='Dealer')

    playing = True
    while playing:
        await __ctx.send(f"{__ctx.author.mention}, enter **QUIT** anytime to leave $$$$$$")
        while True:

            player.pull_new_card()

            await __ctx.send(player.get_card_print())

            if player.check_for_bust():
                await __ctx.send(__ctx.author.mention + " BUST!")
                break
            elif player.check_for_win():
                await __ctx.send(__ctx.author.mention + "You win!!")
                break

            # Keeps looping until a valid msg is passed
            # if you get a valid msg, save the value
            h_s = await prompt(__client, __ctx, question_to_prompt='Enter **h** for hit or **s** for stand: ',
                               valid_answers=['h', 's', 'quit'], str=True)
            if h_s == "s":
                pass
            elif h_s == 'quit':
                break
        choice = await prompt(__client, __ctx, question_to_prompt='Do you want to play a new game? (Yes, No)',
                              valid_answers=['y','yes','n', 'no'], str=True)
        if choice == "yes" or choice == 'y':
            player.reset()
        else:
            playing = False