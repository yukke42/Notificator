# Notificator
slackに処理の終了を通知


## 設定
```bash
$ ./install.sh
# zsh を利用しているなら
$ source ~/.zsh_aliases
# bash を利用しているなら
$ source ~/.bash_aliases
```
`config.ini`に
- Slack web API Toekn [参考](http://qiita.com/9en/items/23eb3762a9df2c29e812#%E3%83%88%E3%83%BC%E3%82%AF%E3%83%B3%E3%81%AE%E5%8F%96%E5%BE%97%E6%96%B9%E6%B3%95)
- 通知するチャンネル
- 通知相手のユーザー

を設定する

## 使用方法
エイリアスとして登録される。
```bash
$ notificate echo "aaaaa"
$ notificate ./tweet.py
```

## 注意
設定値ファイルに間違いがあったとしてもHTTP POSTでは検知できていない。
正しく送信できていないときは設定値を確認する。
