from nonebot.adapters.mirai import Bot, GroupMessage, FriendMessage

from .nb import *
from .handle import *

@command.handle()
async def _(bot: Bot, event: FriendMessage):
    await bot.send(event, "暂不支持记录私聊")

@command.handle()
async def _(bot: Bot, event: GroupMessage):
    group_id = event.sender.group.id
    user_id = event.sender.id
    nickname = event.sender.name
    message = event.get_plaintext().strip()
    await bot.send(
        event,
        handle_command(
            group_id=group_id,
            user_id=user_id,
            time=int(time.time()),
            nickname=nickname,
            message=message,
        ),
    )


@logger.handle()
async def _(bot: Bot, event: GroupMessage):
    group_id = event.sender.group.id
    user_id = event.sender.id
    nickname = event.sender.name
    message = event.get_plaintext().strip()
    result = handle_logger(
        group_id=group_id,
        user_id=user_id,
        time=int(time.time()),
        nickname=nickname,
        message=message,
    )
    if result:
        await bot.send(event, result)


@logger_.handle()
async def _(bot: Bot, event: GroupMessage):
    group_id = event.sender.group.id
    user_id = event.sender.id
    nickname = event.sender.name
    message = event.get_plaintext().strip()
    result = handle_logger(
        group_id=group_id,
        user_id=user_id,
        time=int(time.time()),
        nickname=nickname,
        message=message,
    )
    if result:
        await bot.send(event, result)
