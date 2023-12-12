# sample

DockerでGUIを利用したアプリを動かすテスト。
Seleniumでのスクレイピングを行うサンプル。
といっても以下を行うだけであり、動作確認が主目的。

- トップページを開く
- リストを作成する
- csvに保存する
- リスト項目の1つに遷移する

## 実行方法

```shell
docker run -it
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /mnt/wslg:/mnt/wslg \
  -e DISPLAY=$DISPLAY \
  -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  -e XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
  -e PULSE_SERVER=$PULSE_SERVER \
  <image_name>:latest
```

例:
```shell
docker run -it
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /mnt/wslg:/mnt/wslg \
  -e DISPLAY=$DISPLAY \
  -e WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
  -e XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
  -e PULSE_SERVER=$PULSE_SERVER \
  selenium_sample001:latest
```

## 利用方法

- docker build: `docker build -t <image_name> .`
- 例: `docker build -t selenium_sample001 .`