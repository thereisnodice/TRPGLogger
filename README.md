# TRPG Logger

*基于 [NoneBot2](https://github.com/nonebot/nonebot2) 和 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的 QQ 跑团记录记录器*

[![License](https://img.shields.io/github/license/thereisnodice/TRPGLogger)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.7.3+-blue.svg)
![NoneBot Version](https://img.shields.io/badge/nonebot-2.0.0.a11+-red.svg)
![PyPI Version](https://img.shields.io/pypi/v/nonebot-plugin-trpglogger.svg)

用来记录跑团记录的 NoneBot2 插件。

## 安装

### 使用 nb-cli（推荐）  

```bash
nb plugin install nonebot_plugin_trpglogger
```

### 使用 poetry

```bash
poetry add nonebot_plugin_trpglogger
```

## 开始使用

`.log on` 开始记录

`.log off` 停止记录

**一个群同一时间段不能存在两个记录！**

## TODO

- [ ] 暂停记录
- [ ] 多开记录
