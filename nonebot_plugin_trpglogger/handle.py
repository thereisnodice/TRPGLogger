import time
from pathlib import Path

from .data import get_logger_time, is_logging, remove_logging, start_logging, stop_logging
from .upload import upload_file


async def handle_command(**kwargs):
    if kwargs["message"] == "on":
        if is_logging(kwargs["group_id"]):
            return "正在进行日志记录, 无法再次开始!"
        else:
            start_logging(kwargs["group_id"], kwargs["time"])
            return "开始日志记录"
    elif kwargs["message"] == "off":
        if is_logging(kwargs["group_id"]):
            stop_logging(kwargs["group_id"])
            return "正在上传文件，请稍等"
        else:
            return "没有已开始的日志记录!"
    else:
        return (
            "TRPGLogger 使用说明：\n" ".log on 开始记录\n" ".log off 停止记录\n" "一个群同一时间段不能存在两个记录！"
        )


async def handle_logger(**kwargs):
    file_path = (
        Path()
        / "data"
        / "trpglogger"
        / f"group_{kwargs['group_id']}_{get_logger_time(kwargs['group_id'])}.txt"
    )

    if is_logging(kwargs["group_id"]):
        with file_path.open("a+", encoding="utf-8") as f:
            f.write(
                f'{kwargs["nickname"]}({kwargs["user_id"]}) {time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(kwargs["time"]))}\n'
            )
            f.write(f'{kwargs["message"]}\n\n')
        if kwargs["time"] - get_logger_time(kwargs["group_id"]) > 60 * 60 * 24:
            stop_logging(kwargs["group_id"])
            return "已持续记录24小时，已自动停止记录并上传"
    else:
        if file_path.exists():
            await upload_file(file_path)
            file_path.unlink()
            remove_logging(kwargs["group_id"])
            return f"上传已完成，请访问 https://logpainter.trpgbot.com/#2-{file_path.name} 以查看记录"
        else:
            remove_logging(kwargs["group_id"])

