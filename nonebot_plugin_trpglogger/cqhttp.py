from nonebot.adapters.cqhttp import Bot, PrivateMessageEvent, GroupMessageEvent, Event

from .nb import *
from .handle import *


@command.handle()
async def _(bot: Bot, event: PrivateMessageEvent):
    await bot.send(event, "暂不支持记录私聊")


@command.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    group_id = event.group_id
    user_id = event.user_id
    time = event.time
    nickname = event.sender.nickname
    message = event.get_plaintext().strip()
    await bot.send(
        event,
        handle_command(
            group_id=group_id,
            user_id=user_id,
            time=time,
            nickname=nickname,
            message=message,
        ),
    )


@logger.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    group_id = event.group_id
    user_id = event.user_id
    time = event.time
    nickname = event.sender.nickname
    message = event.get_plaintext().strip()
    result = handle_logger(
        group_id=group_id,
        user_id=user_id,
        time=time,
        nickname=nickname,
        message=message,
    )
    if result:
        await bot.send(event, result)


@logger_.handle()
async def _(bot: Bot, event: Event):
    group_id = event.group_id
    user_id = event.sender["user_id"]
    time = event.time
    nickname = event.sender["nickname"]
    message = event.message[0]["data"]["text"]
    result = handle_logger(
        group_id=group_id,
        user_id=user_id,
        time=time,
        nickname=nickname,
        message=message,
    )
    if result:
        await bot.send(event, result)
