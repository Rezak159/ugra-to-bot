from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from typing import Callable, Dict, Any, Awaitable, Optional
from datetime import datetime, timedelta

from aiogram.enums import ChatMemberStatus

import dbtools

CHAT_LIST = [-5060610445]
MEMBERSHIP_TTL = timedelta(minutes=20)


def _should_skip_check(user: Dict[str, Any]) -> bool:
    if not user:
        return False

    if not user.get("is_member"):
        return False

    last_checked = user.get("last_checked")
    if not last_checked:
        return False

    try:
        last_checked_dt = datetime.fromisoformat(last_checked)
    except (TypeError, ValueError):
        return False

    return datetime.now() - last_checked_dt < MEMBERSHIP_TTL


async def check_user_in_group(bot, user_id, username: Optional[str] = None):
    user = dbtools.get_user(user_id)
    if not user and username:
        dbtools.add_user(user_id, username)
        user = dbtools.get_user(user_id)

    if _should_skip_check(user):
        return True

    try:
        is_member = False
        for chat_id in CHAT_LIST:
            member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)

            # Проверяем статус пользователя
            if member.status in [
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.CREATOR,
                ChatMemberStatus.ADMINISTRATOR
            ]:
                is_member = True
                break

        if user:
            dbtools.set_member_status(user_id, is_member)

        return is_member
    except Exception as e:
        print(f"Ошибка при проверке: {e}")
        return bool(user and user.get("is_member"))

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

        chat = event.message.chat if event.message else None
        if not chat or chat.type != 'private':
            await event.answer('Бот доступен только в личных сообщениях', show_alert=True)
            return

        username = event.from_user.username or event.from_user.full_name or "Unknown"
        is_member = await check_user_in_group(bot, user_id, username)

        if not is_member:
            text = '❌ У вас нет доступа'
            await event.answer(text, show_alert=True)
            return
            
        # ОБЯЗАТЕЛЬНО вызвать, чтобы продолжить обработку
        result = await handler(event, data)
        
        # Код ПОСЛЕ вызова handler выполнится после хэндлера
        return result
