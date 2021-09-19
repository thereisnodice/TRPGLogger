from nonebot.plugin import on, on_message, on_command
from nonebot.adapters.cqhttp import Bot, PrivateMessageEvent, GroupMessageEvent, Event
import nonebot

from .handle import *

command = on_command("log", priority=1)
logger = on_message(priority=1, block=False)
logger_ = on("message_sent", priority=1, block=False)


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
