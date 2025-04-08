from logging import Logger

import paramiko
from config_data.config import load_config
import logging
config = load_config()


logger2: Logger = logging.getLogger(__name__)
logger2.setLevel(logging.INFO)

# Подключение к MikroTik через SSH
def connect_to_mikrotik(config):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print('BOT_TOKEN:', config.tg_bot.token)
    print('ADMIN_IDS:', config.tg_bot.admin_ids)
    print()
    print('SSH_HOST:', config.ssh_con.ssh_host)
    print('SSH_PORT:', config.ssh_con.ssh_port)
    print('SSH_USERNAME:', config.ssh_con.ssh_username)
    print('SSH_PASSWORD:', config.ssh_con.ssh_password)


    logger2.info('Подключаемся по SSH...')
    ssh.connect(config.ssh_con.ssh_host,
                username=config.ssh_con.ssh_username,
                password=config.ssh_con.ssh_password)
    return ssh


# Выполнение команды на MikroTik
def execute_command(command):
    logger2.info('Настраиваем SSH соединение...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logger2.info('Подключаемся по SSH...')
    ssh.connect(config.ssh_con.ssh_host,
                username=config.ssh_con.ssh_username,
                password=config.ssh_con.ssh_password,
                look_for_keys=False)
    ssh.exec_command(command)
    return 'Команда отправлена'

