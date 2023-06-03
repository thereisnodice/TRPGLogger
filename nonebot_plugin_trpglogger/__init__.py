from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11.message import Message
from nonebot.plugin import PluginMetadata, on, on_command, on_message
from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    GroupMessageEvent,
    PrivateMessageEvent,
)

from .handle import *

__plugin_meta__ = PluginMetadata(
    name="跑团记录记录器",
    description="记录跑团记录并上传",
    usage="""log on 开始记录
log off 停止记录
一个群同一时间段不能存在两个记录！""",
    type="application",
    homepage="https://github.com/thereisnodice/TRPGLogger",
    supported_adapters={"~onebot.v11"},
)

command = on_command("log", priority=1)
logger = on_message(priority=1, block=False)
logger_ = on("message_sent", priority=1, block=False)


@command.handle()
async def _(bot: Bot, event: PrivateMessageEvent):
    await bot.send(event, "暂不支持记录私聊")


@command.handle()
async def _(bot: Bot, event: GroupMessageEvent, command_arg: Message = CommandArg()):
    group_id = event.group_id
    user_id = event.user_id
    time = event.time
    nickname = event.sender.nickname
    message = str(command_arg)
    await bot.send(
        event,
        await handle_command(
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
    result = await handle_logger(
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
    if event.message_type == "group":  # type: ignore
        event.post_type = "message"
        event_ = GroupMessageEvent.parse_obj(event.dict())
        event.post_type = "message_sent"
        group_id = event_.group_id
        user_id = event_.user_id
        time = event.time
        nickname = event_.sender.nickname
        message = event_.get_plaintext().strip()
        result = await handle_logger(
            group_id=group_id,
            user_id=user_id,
            time=time,
            nickname=nickname,
            message=message,
        )
        if result:
            await bot.send(event, result)
