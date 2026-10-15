# Docker 部署指南

本文档介绍如何使用 Docker 部署 PA Agent。

## 前提条件

- 已经安装 Docker 和 Docker Compose。
- 获取了项目的源码。

## 步骤

1. 在项目根目录下，确保有 `Dockerfile` 或 `docker-compose.yml` 等文件（如果在主分支中有相关 Docker 文件的话，可以直接使用；如果没有，你需要自己创建一个 Dockerfile）。

2. 如果你需要构建镜像，运行：
   ```bash
   docker build -t pa-agent .
   ```

3. 运行容器：
   ```bash
   docker run -d --name pa-agent-container pa-agent
   ```
   你可以使用 `-p` 映射端口，或 `-v` 挂载配置目录。

4. 如果有 Docker Compose，可以直接运行：
   ```bash
   docker-compose up -d
   ```

## 注意事项

- 请确保你的环境能够连接所需的 API，并配置了对应的环境变量和 `.env` 文件（或将其挂载进去）。
- 修改 `settings.json` 前，请了解是否需要重新启动容器使之生效。
