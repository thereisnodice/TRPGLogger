# TRPGLogger

*基于 [nonebot2](https://github.com/nonebot/nonebot2) 以及 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 QQ 跑团记录记录器*

[![License](https://img.shields.io/github/license/thereisnodice/TRPGLogger)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![NoneBot Version](https://img.shields.io/badge/nonebot-2+-red.svg)
![Pypi Version](https://img.shields.io/pypi/v/nonebot-plugin-trpglogger.svg)

用来记录跑团记录的 nonebot2 插件，与 https://logpainter.kokona.tech 配合使用

*移植自 [Dice-Developer-Team/TrpgLogger](https://github.com/Dice-Developer-Team/TrpgLogger)*

### 安装

* 使用nb-cli（推荐）  

```bash
nb plugin install nonebot_plugin_trpglogger
```

* 使用poetry

```bash
poetry add nonebot_plugin_trpglogger
```

### 开始使用

`.log on` 开始记录

`.log off` 停止记录

**一个群同一时间段不能存在两个记录且无法暂停！**

<details>
<summary>展开更多</summary>

### 原理

与 TrpgLogger 一样，使用 AWS S3 进行储存（目前是直接用溯洄的公共 bucket ）。

### Bug

- 无法记录机器人本身发出的消息（即无法记录掷骰）  
 **如何解决:** 等 nonebot2 更新 a11

</details>
