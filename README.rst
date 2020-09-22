===================
Zuraaa Vote Checker
===================

Uma forma não oficial de verificar quando alguem votou no seu bot.

Instalação
----------

**É necessário Python 3.6 ou superior.**

A instalação pode ser feita via PyPI. Basta executar o seguinte comando:

.. code :: sh

    python -m pip install zuraaa-vote-checker    

Modo de usar
------------

O uso é simples, basta carregar uma cog chamada ``zuraaaVoteChecker`` (case-sensitive)

Depois disso é só escutar o evento ``zuraaa_vote``.

- Ele recebe um único parâmetro do tipo `discord.User <https://discordpy.readthedocs.io/en/latest/api.html#discord.User>`_, representando quem votou.

**Exemplo:**

.. code :: python
    
    from discord.ext.commands import Bot

    bot = Bot(command_prefix = '.')

    @bot.event
    async def on_zuraaa_vote(user):
        print(f'{user.name} votou!')

    bot.load_extension('zuraaaVoteChecker')

    bot.run('TOKEN')

----

**Você pode acessar a quantidade de usuários que votaram no bot também!**

Basta acessar o atributo ``zuraaa_vote_streak``, na classe do seu bot.
Ele irá contar a quantidade de votos desde que a cog foi carregada.
