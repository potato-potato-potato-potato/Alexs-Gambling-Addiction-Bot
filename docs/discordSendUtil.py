
async def prompt(client, ctx, valid_answers, question_to_prompt, str=False):
    """
    Prompts the user with a question, with some inputs, and returns the users input.

    :param ctx: The message being snet
    :param valid_answers:  valid string answers that are acceptable
    :param question_to_prompt: The question the bot will ask before detecting a input
    :param client: The bot
    :return: returns a Message object of the valid input
    """
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content.lower() in valid_answers

    await ctx.send(question_to_prompt)
    response = await client.wait_for('message', check=check)

    if str:
        return response.content.lower()
    return response
