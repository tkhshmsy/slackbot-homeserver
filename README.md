# slackbot-homeserver

slack-rtmbot as controller of my-home-server

## how do i itend to use this

for example,

- I speak to GoogleAssistant
- using IFTTT, IF GoogleAssistant THEN Slack
- slack-rtmbot recv message from IFTTT
- plugin(this project) kicks Chromecast / GoogleHome / ...

## setup

### install and execute

1. install requirements

    ```sh
    $ pipenv install
    ```

2. edit rtmbot.conf with SlackBOT's API-TOKEN

3. edit homeserver.ini with slack id etc.

4. exec.

    ```sh
    $ rtmbot
    ```

### daemonize

```sh
$ sudo cp slackbot-homeserver.systemd.service /usr/lib/systemd/system
$ sudo systemctl daemon-reload
$ sudo systemctl status slackbot-homeserver.systemd.servie
$ sudo systemctl start slackbot-homeserver.systemd.servie
```

all right, then

```sh
$ sudo systemctl enable slackbot-homeserver.systemd.servie
```

## commands for bot

this bot will recognize commands with JSON format.

ex.  

~~~sh
    {
        "command" : "play",
        "url" : "http://....."
    }
~~~

## depends

- <https://github.com/slackapi/python-rtmbot>
- <https://github.com/balloob/pychromecast>

## author

- tkhshmsy@gmail.com

## license

- MIT