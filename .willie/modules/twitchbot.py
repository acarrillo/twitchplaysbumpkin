import willie

@willie.module.rule('([^\s]+)')
def helloworld(bot, trigger):
    cmd = trigger.bytes.decode(encoding='UTF-8')
    bot.say("Executing " + cmd)

    if cmd == "forward":
        forward

