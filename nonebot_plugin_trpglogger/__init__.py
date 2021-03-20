import time
import os

from nonebot.adapters import Event,Bot
from nonebot.adapters.cqhttp import PrivateMessageEvent,GroupMessageEvent
from nonebot.plugin import on,on_message

from .sqlite import is_logging,start_logging,stop_logging
from .s3 import upload_file

TRPGLogger=on_message(priority=1,block=False)
TRPGLogger_=on("message_sent",priority=1,block=False)

@TRPGLogger_.handle()
@TRPGLogger.handle()
async def _(bot: Bot, event: Event):
    message=get_message(event)
    if isinstance(event,GroupMessageEvent) and message[:4]=='.log':
        if message[4:].strip()=='on' or message[4:].strip()=='':
            if is_logging(event.group_id):
                await bot.send(event,"正在进行日志记录, 无法再次开始!")
            else:
                await bot.send(event,"开始日志记录")
                start_logging(event.group_id,event.time)
        elif message[4:].strip()=='off':
            file_path=os.path.join('data','trpglogger',f'group_{event.group_id}_{is_logging(event.group_id)}.txt')
            if is_logging(event.group_id):
                await bot.send(event,"正在上传文件，请稍等")
                upload_file(file_path,"dicelogger",os.path.basename(file_path))
                await bot.send(event,"上传已完成，请访问 https://logpainter.kokona.tech/?s3=" + f'group_{event.group_id}_{is_logging(event.group_id)}.txt'+"以查看记录")
                os.remove(file_path)
                stop_logging(event.group_id)
            else:
                await bot.send(event,"没有已开始的日志记录!")
    else:
        if isinstance(event,PrivateMessageEvent):
            return

        if is_logging(event.group_id):
            file_path=os.path.join('data','trpglogger',f'group_{event.group_id}_{is_logging(event.group_id)}.txt')
            with open(file_path,'a+',encoding='utf=8') as f:
                print(event.sender)
                f.write(f'{get_nickname(event)}({get_user_id(event)}) {time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(event.time))}\n')
                f.write(f'{message}\n\n')
            if event.time-is_logging(event.group_id)>60*60*24:
                await bot.send(event,"已持续记录24小时，已自动停止记录并上传")
                upload_file(file_path,"dicelogger",os.path.basename(file_path))
                await bot.send(event,"上传已完成，请访问 https://logpainter.kokona.tech/?s3=" + f'group_{event.group_id}_{is_logging(event.group_id)}.txt'+"以查看记录")
                os.remove(file_path)
                stop_logging(event.group_id)

def get_message(event: Event):
    try:
        return event.get_plaintext()
    except:
        return event.message[0]["data"]["text"]

def get_nickname(event: Event) -> str:
    try:
        return event.sender.nickname
    except:
        return event.sender["nickname"]

def get_user_id(event: Event):
    try:
        return event.sender.user_id
    except:
        return event.sender["user_id"]


