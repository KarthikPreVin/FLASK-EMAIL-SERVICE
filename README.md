- clone repo
- create a .env in root folder as

```
MAIL_USERNAME = "email_address@gmail.com"
MAIL_PASSWORD = "your_app_password(refer below for how to generate app password)"
```

go to [Account Security](https://myaccount.google.com/security) of your Sender mail account
turn on 2 step verification
go to [App password](https://myaccount.google.com/apppasswords) and generate new app password. copy the 16 character string and paste in MAIL_PASSWORD alue in .env (password shud be 16 digits with no spaces).