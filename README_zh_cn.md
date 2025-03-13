# PlayerInfo-MCDR
在MCDR中获取玩家的详细信息，支持安装了Geyser+Floodgate的互通服务器。

注意：插件的工作严重依赖于MCDR从服务端日志中解析的信息，因此使用前请确保你的服务端处理器有在正确工作。

## 前置、依赖及限制条件
- Geyser+Floodgate（基岩版玩家相关）支持需要服务端安装相关插件

- 要兼容聊天修改类插件，必须使用支持BukkitAPI的服务端，安装BukkitChatManager并启用该插件的兼容模式

- Geyser独立版兼容性未知，后续将进行测试

## 功能
- 玩家档案信息查询
> `!!pinfo query <uuid|player_name>`

- 提供玩家信息获取接口
> 作为API

## 集成
- 基于`server/usercache.json`的UUID查询功能，可优先从本地匹配信息，速度更快
> 在线查询仅使用官方接口，后续将支持外置皮肤站

- 基于`./permission.yml`，判断玩家（名）是否属于服务器成员
> 依赖于服务端处理器正确解析玩家名

- 基于服务端命令`list`的返回结果，精准识别在线玩家列表
> 使用Rcon响应速度更快，同时使用`geyser list`检测使用基岩版客户端的玩家列表

