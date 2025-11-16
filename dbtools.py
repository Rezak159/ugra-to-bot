import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any


DB_FILE = "data/users.json"


def _ensure_db_exists():
    """Проверяет наличие папки data и файла базы данных"""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)


def _load_db() -> Dict[str, Dict[str, Any]]:
    """Загружает данные из JSON файла с обработкой ошибок"""
    try:
        _ensure_db_exists()
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        print(f"Ошибка: некорректный JSON в {DB_FILE}. Инициализирую пустую БД.")
        return {}
    except IOError as e:
        print(f"Ошибка чтения файла {DB_FILE}: {e}")
        return {}


def _save_db(data: Dict[str, Dict[str, Any]]) -> bool:
    """Сохраняет данные в JSON файл с обработкой ошибок"""
    try:
        _ensure_db_exists()
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Ошибка записи в файл {DB_FILE}: {e}")
        return False


def add_user(tg_id: int, username: str) -> bool:
    """
    Добавляет нового пользователя в БД
    
    Args:
        tg_id: Telegram ID пользователя
        username: Никнейм пользователя
        
    Returns:
        True если пользователь добавлен/обновлен, False если произошла ошибка
    """
    try:
        if not isinstance(tg_id, int) or tg_id <= 0:
            print(f"Ошибка: некорректный Telegram ID: {tg_id}")
            return False
        
        if not isinstance(username, str) or not username.strip():
            print(f"Ошибка: некорректное имя пользователя: {username}")
            return False
        
        data = _load_db()
        tg_id_str = str(tg_id)
        now = datetime.now().isoformat()
        
        if tg_id_str not in data:
            data[tg_id_str] = {
                "tg_id": tg_id,
                "username": username.strip(),
                "registration_date": now,
                "last_request_date": now,
                "is_member": False,
                "last_checked": now
            }
        else:
            # Обновляем существующего пользователя
            data[tg_id_str]["username"] = username.strip()
            data[tg_id_str]["last_request_date"] = now
        
        return _save_db(data)
    except Exception as e:
        print(f"Ошибка при добавлении пользователя {tg_id}: {e}")
        return False


def get_user(tg_id: int) -> Optional[Dict[str, Any]]:
    """
    Получает данные пользователя по ID
    
    Args:
        tg_id: Telegram ID пользователя
        
    Returns:
        Словарь с данными пользователя или None если пользователь не найден
    """
    try:
        if not isinstance(tg_id, int) or tg_id <= 0:
            print(f"Ошибка: некорректный Telegram ID: {tg_id}")
            return None
        
        data = _load_db()
        return data.get(str(tg_id))
    except Exception as e:
        print(f"Ошибка при получении пользователя {tg_id}: {e}")
        return None


def update_last_request(tg_id: int) -> bool:
    """
    Обновляет дату последнего запроса пользователя
    
    Args:
        tg_id: Telegram ID пользователя
        
    Returns:
        True если обновлено успешно, False если пользователь не найден или ошибка
    """
    try:
        if not isinstance(tg_id, int) or tg_id <= 0:
            print(f"Ошибка: некорректный Telegram ID: {tg_id}")
            return False
        
        data = _load_db()
        tg_id_str = str(tg_id)
        
        if tg_id_str not in data:
            print(f"Пользователь {tg_id} не найден в БД")
            return False
        
        data[tg_id_str]["last_request_date"] = datetime.now().isoformat()
        return _save_db(data)
    except Exception as e:
        print(f"Ошибка при обновлении последнего запроса для {tg_id}: {e}")
        return False


def update_last_checked(tg_id: int) -> bool:
    """
    Обновляет дату последней проверки статуса пользователя
    
    Args:
        tg_id: Telegram ID пользователя
        
    Returns:
        True если обновлено успешно, False если пользователь не найден или ошибка
    """
    try:
        if not isinstance(tg_id, int) or tg_id <= 0:
            print(f"Ошибка: некорректный Telegram ID: {tg_id}")
            return False
        
        data = _load_db()
        tg_id_str = str(tg_id)
        
        if tg_id_str not in data:
            print(f"Пользователь {tg_id} не найден в БД")
            return False
        
        data[tg_id_str]["last_checked"] = datetime.now().isoformat()
        return _save_db(data)
    except Exception as e:
        print(f"Ошибка при обновлении последней проверки для {tg_id}: {e}")
        return False


def set_member_status(tg_id: int, is_member: bool) -> bool:
    """
    Устанавливает статус членства пользователя
    
    Args:
        tg_id: Telegram ID пользователя
        is_member: Статус членства (True/False)
        
    Returns:
        True если установлено успешно, False если пользователь не найден или ошибка
    """
    try:
        if not isinstance(tg_id, int) or tg_id <= 0:
            print(f"Ошибка: некорректный Telegram ID: {tg_id}")
            return False
        
        if not isinstance(is_member, bool):
            print(f"Ошибка: is_member должен быть булевым значением")
            return False
        
        data = _load_db()
        tg_id_str = str(tg_id)
        
        if tg_id_str not in data:
            print(f"Пользователь {tg_id} не найден в БД")
            return False
        
        data[tg_id_str]["is_member"] = is_member
        data[tg_id_str]["last_checked"] = datetime.now().isoformat()
        return _save_db(data)
    except Exception as e:
        print(f"Ошибка при установке статуса членства для {tg_id}: {e}")
        return False


def get_all_users() -> List[Dict[str, Any]]:
    """
    Получает всех пользователей из БД
    
    Returns:
        Список словарей с данными пользователей
    """
    try:
        data = _load_db()
        return list(data.values())
    except Exception as e:
        print(f"Ошибка при получении всех пользователей: {e}")
        return []


def get_members() -> List[Dict[str, Any]]:
    """
    Получает всех пользователей со статусом is_member=True
    
    Returns:
        Список словарей с данными членов
    """
    try:
        data = _load_db()
        return [user for user in data.values() if user.get("is_member", False)]
    except Exception as e:
        print(f"Ошибка при получении членов: {e}")
        return []


def delete_user(tg_id: int) -> bool:
    """
    Удаляет пользователя из БД
    
    Args:
        tg_id: Telegram ID пользователя
        
    Returns:
        True если пользователь удален, False если не найден или ошибка
    """
    try:
        if not isinstance(tg_id, int) or tg_id <= 0:
            print(f"Ошибка: некорректный Telegram ID: {tg_id}")
            return False
        
        data = _load_db()
        tg_id_str = str(tg_id)
        
        if tg_id_str not in data:
            print(f"Пользователь {tg_id} не найден в БД")
            return False
        
        del data[tg_id_str]
        return _save_db(data)
    except Exception as e:
        print(f"Ошибка при удалении пользователя {tg_id}: {e}")
        return False


def user_exists(tg_id: int) -> bool:
    """
    Проверяет наличие пользователя в БД
    
    Args:
        tg_id: Telegram ID пользователя
        
    Returns:
        True если пользователь существует, False в противном случае
    """
    try:
        if not isinstance(tg_id, int) or tg_id <= 0:
            return False
        
        data = _load_db()
        return str(tg_id) in data
    except Exception as e:
        print(f"Ошибка при проверке наличия пользователя {tg_id}: {e}")
        return False


def get_user_count() -> int:
    """
    Получает количество пользователей в БД
    
    Returns:
        Количество пользователей
    """
    try:
        data = _load_db()
        return len(data)
    except Exception as e:
        print(f"Ошибка при подсчете пользователей: {e}")
        return 0


def get_members_count() -> int:
    """
    Получает количество членов в БД
    
    Returns:
        Количество членов (is_member=True)
    """
    try:
        data = _load_db()
        return sum(1 for user in data.values() if user.get("is_member", False))
    except Exception as e:
        print(f"Ошибка при подсчете членов: {e}")
        return 0


