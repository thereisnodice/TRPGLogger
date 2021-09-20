# TRPG Logger

*基于 [nonebot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 QQ 跑团记录记录器*

[![License](https://img.shields.io/github/license/thereisnodice/TRPGLogger)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7.3+-blue.svg)
![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0.a11+-red.svg)
![Pypi Version](https://img.shields.io/pypi/v/nonebot-plugin-trpglogger.svg)

用来记录跑团记录的 nonebot2 插件，与 <https://logpainter.kokona.tech> 配合使用。

*移植自 [Dice-Developer-Team/TrpgLogger](https://github.com/Dice-Developer-Team/TrpgLogger)*

### 安装

* 使用 nb-cli（推荐）  

```bash
nb plugin install nonebot_plugin_trpglogger
```

* 使用 poetry

```bash
poetry add nonebot_plugin_trpglogger
```

### 开始使用

`.log on` 开始记录

`.log off` 停止记录

**一个群同一时间段不能存在两个记录！**

### TO DO

- [ ] 暂停记录
- [ ] 多开记录

<details>
<summary>展开更多</summary>

### 原理

与 [Dice-Developer-Team/TrpgLogger](https://github.com/Dice-Developer-Team/TrpgLogger) 一样，使用 AWS S3 进行储存（目前为了与 Logpainter 对接，是直接用溯洄的公共 bucket ）。

### Bug

- [x] go-cqhttp 无法记录机器人本身发出的消息（即无法记录掷骰）  
    **请确保 go-cqhttp 的 `enable_self_message` 设置为 true**
- [ ] 在记录时间超过 24 小时后，如果上传文件失败会阻塞线程  
    **如何解决:** 待定

</details>
