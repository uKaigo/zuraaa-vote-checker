import re

from discord.ext.commands import Cog

__all__ = ('setup',)

class ZuraaaVoteChecker(Cog):
    """
    Cog que vai escutar as mensagens.
    
    Attributes
    ----------
    vote_streak: :class:`int`
        A quantidade de votos desde que a cog carregou.
    """

    def __init__(self, bot):
        self.__bot = bot

        self.__bot.zuraaa_vote_streak = 0

        fmt = fr'\((\d+)\) (?=votou no bot `{bot.user}`)'
        self.__compiled_re = re.compile(fmt)

    @Cog.listener()
    async def on_message(self, message):
        await self.__bot.wait_until_ready()

        if not message.channel.id == 537433191393525760:
            return

        match = self.__compiled_re.search(message.content)

        if match:
            user_id = match.group(1)

            user = self.__bot.get_user(int(user_id))

            self.__bot.dispatch('zuraaa_vote', user)

    @Cog.listener()
    async def on_zuraaa_vote(self, _):
        self.__bot.zuraaa_vote_streak += 1

def setup(bot):
    bot.add_cog(ZuraaaVoteChecker(bot))
