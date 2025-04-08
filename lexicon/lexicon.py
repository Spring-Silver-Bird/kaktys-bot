LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЯ микро-бот.! \n\n'
              'Я отправляю комманды на роутер microtic,'
              'к которому подключаюсь по SSH\n'
              'Для подробностей обратитесь к /help',
    '/help': 'Я очень умный бот! Но меня заставляют'
             'тыкать кнопочки и работать выключателем :(\n'
             'Я умею обрабатывать пока только две команды;\n'
             '/kaktyc_pc_vpn_full\n'
             '/katya_pc_vpn_full',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy',
    'kaktyc.pc.vpn.full': 'VPN на kaktyc.pc.vpn.full включен/выключен',
    'katya.pc.vpn.full': 'VPN на katya.pc.vpn.full включен/выключен'
}

LEXICON_COMMANDS_RU: dict[str, str] = {
    '/start': 'restart',
    '/help': 'info',
    '/kaktyc.pc.vpn.full': 'set full VPN for kaktyc_pc',
    '/katya.pc.vpn.full': 'set full VPN for katya_pc'
}