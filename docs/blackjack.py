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
        self.cards_print = f'**{name}**: '

    def pull_new_card(self, __cards, __card_types):
        card, points = random.choice(list(__cards.items()))
        card_type = random.choice(__card_types)

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


def black_jack(ctx):
    player = __Player(21, ctx.author)

    playing = True
    while playing:
        while True:

            player.pull_new_card()

            await ctx.send(player.get_card_print())

            # Keeps looping until a valid msg is passed
            # if you get a valid msg, save the value
            h_s = await prompt(ctx, question_to_prompt='Enter **h** for hit or **s** for stand: ',
                               valid_answers=['h', 's'], str=True)
            if h_s == "s":
                pass

            if player.check_for_bust():
                await ctx.send(ctx.author.mention + " BUST!")
                break
            elif player.check_for_win():
                await ctx.send(ctx.author.mention + "You win!!")
                break
        choice = await prompt(ctx, question_to_prompt='Do you want to continue(Yes, No)',
                              valid_answers=['yes', 'no'], str=True)
        if choice == "no":
            playing = False
