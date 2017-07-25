# Notificator
Post a message on slack after the command exists.

## Requirement
- Python3.5 or more


## Usage
```
$ notificate "echo "aaa"" --channel test
aaa
$ notificate "./run.py" --channel notification --user yukke42
...
```

For more information, see `notificate --help`


## Installation
```bash
$ git clone https://github.com/yukke42/Notificator
```


## Settings
```
$ cp config.ini.sample config.ini
$ echo "alias notificate='python3 $(pwd)/notificate.py'" >> ~/.bash_aliases
$ source ~/.bash_aliases
```
Add your [Slack Web API Token](https://api.slack.com/web) to `config.ini`


## Author

[@yukke_42](https://twitter.com/yukke_42)


## License

[MIT](https://github.com/yukke42/Notificator/blob/master/LICENSE)
