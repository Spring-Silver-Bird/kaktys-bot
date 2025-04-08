from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from services.services import execute_command

# Инициализируем роутер уровня модуля
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

# Этот хэндлер срабатывает на команду /kaktyc.pc.vpn.full
# которая включает или выключает маршрутизацию для kaktyc.pc
@router.message(Command(commands='kaktyc_pc_vpn_full'))
async def process_kaktyc_command(message: Message):

    execute_command('/system script run kaktyc.pc.vpn.full')
    await message.answer(text=['Команда отправлена'])


# Этот хэндлер срабатывает на команду /katya.pc.vpn.full
# которая включает или выключает маршрутизацию для kaktyc.pc
@router.message(Command(commands='katya_pc_vpn_full'))
async def process_katya_command(message: Message):
    execute_command('/system script run katya.pc.vpn.full')
    await message.answer(text=['Команда отправлена'])

