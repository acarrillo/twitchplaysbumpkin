import willie

@willie.module.rule('([^\s]+)')
def helloworld(bot, trigger):
    print trigger.bytes
    bot.say(trigger.bytes.decode(encoding='UTF-8').upper())