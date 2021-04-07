import nonebot

try:
    from .cqhttp import *
except:
    nonebot.logger.warning("Could not found CQHTTP Adapter !")

try:
    from .mirai import *
except:
    nonebot.logger.warning("Could not found MIRAI Adapter !")
