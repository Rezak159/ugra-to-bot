from aiogram import BaseMiddleware
from aiogram.types import Message, Update, CallbackQuery
from typing import Callable, Dict, Any, Awaitable

from aiogram.enums import ChatMemberStatus

CHAT_LIST = [-5060610445]

async def check_user_in_group(bot, user_id):
    try:
        for chat_id in CHAT_LIST:
            member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)

            # Проверяем статус пользователя
            if member.status in [
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.CREATOR, 
                ChatMemberStatus.ADMINISTRATOR
            ]:
                print(f'member.status: {member.status}')
                return True
        return False
    except Exception as e:
        print(f"Ошибка при проверке: {e}")
        return False

class Middleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # Код ДО вызова handler выполнится перед хэндлером
        bot = data['bot']
        user_id = event.from_user.id

        print(f'id: {user_id}')
        
        is_member = await check_user_in_group(bot, user_id)

        if not is_member:
            text = '❌ У вас нет доступа'
            await event.answer(text, show_alert=True)
            return
            
        # ОБЯЗАТЕЛЬНО вызвать, чтобы продолжить обработку
        result = await handler(event, data)
        
        # Код ПОСЛЕ вызова handler выполнится после хэндлера
        return result
