from dataclasses import dataclass
from environs import Env


'''@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных'''


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class SshConfig:
    ssh_host: str
    ssh_port: str
    ssh_username: str
    ssh_password: str


@dataclass
class Config:
    tg_bot: TgBot
#    db: DatabaseConfig
    ssh_con: SshConfig





def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        ssh_con=SshConfig(
            ssh_host=env('SSH_HOST'),
            ssh_port=env('SSH_PORT'),
            ssh_username=env('SSH_USERNAME'),
            ssh_password=env('SSH_PASSWORD')
        )
    )
config = load_config()

'''print('BOT_TOKEN:', config.tg_bot.token)
print('ADMIN_IDS:', config.tg_bot.admin_ids)
print()
print('SSH_HOST:', config.ssh_con.ssh_host)
print('SSH_PORT:', config.ssh_con.ssh_port)
print('SSH_USERNAME:', config.ssh_con.ssh_username)
print('SSH_PASSWORD:', config.ssh_con.ssh_password)'''
