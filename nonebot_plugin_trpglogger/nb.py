from nonebot.plugin import on, on_message, on_command

command = on_command("log", priority=1)
logger = on_message(priority=1, block=False)
logger_ = on("message_sent", priority=1, block=False)
