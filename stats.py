import json
import os
from datetime import datetime, date, time, timedelta
from typing import Dict, Any, Optional
from zoneinfo import ZoneInfo

import dbtools

EKB_TZ = ZoneInfo("Asia/Yekaterinburg")
LOGS_DIR = "logs"
STATS_FILE = "data/stats.json"


def _ensure_dirs():
    os.makedirs(LOGS_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(STATS_FILE), exist_ok=True)


def _parse_dt(value: Optional[str]) -> Optional[datetime]:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=EKB_TZ)
    return dt.astimezone(EKB_TZ)


def log_request(user_id: int, username: str, action: str) -> None:
    """
    Логирует каждый запрос в файл logs/YYYY-MM-DD.log (Ekaterinburg TZ).
    """
    _ensure_dirs()
    now = datetime.now(EKB_TZ)
    record = {
        "ts": now.isoformat(),
        "user_id": user_id,
        "username": username,
        "action": action
    }
    log_path = os.path.join(LOGS_DIR, f"{now.strftime('%Y-%m-%d')}.log")
    try:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError as exc:
        print(f"Ошибка записи лога {log_path}: {exc}")


def _load_stats() -> Dict[str, Dict[str, Any]]:
    _ensure_dirs()
    if not os.path.exists(STATS_FILE):
        return {}
    try:
        with open(STATS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Ошибка чтения {STATS_FILE}: {exc}")
        return {}


def _save_stats(data: Dict[str, Dict[str, Any]]) -> None:
    _ensure_dirs()
    try:
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as exc:
        print(f"Ошибка записи {STATS_FILE}: {exc}")


def _count_requests_for_day(target: date) -> int:
    log_path = os.path.join(LOGS_DIR, f"{target.strftime('%Y-%m-%d')}.log")
    if not os.path.exists(log_path):
        return 0
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)
    except OSError as exc:
        print(f"Ошибка чтения {log_path}: {exc}")
        return 0


def finalize_day(target: Optional[date] = None) -> Dict[str, Any]:
    """
    Финализирует статистику за указанный день (по умолчанию - вчера, Ekaterinburg TZ).
    Возвращает рассчитанные метрики.
    """
    _ensure_dirs()
    if target is None:
        target = (datetime.now(EKB_TZ) - timedelta(days=1)).date()

    day_end = datetime.combine(target, time(23, 59, 59, 999999, tzinfo=EKB_TZ))
    active_1d_threshold = day_end - timedelta(days=1)
    active_7d_threshold = day_end - timedelta(days=7)

    users = dbtools.get_all_users()
    users_total = len(users)
    active_1d = 0
    active_7d = 0

    for user in users:
        last_req_raw = user.get("last_request_date")
        last_req = _parse_dt(last_req_raw)
        if not last_req:
            continue
        if last_req >= active_7d_threshold:
            active_7d += 1
            if last_req >= active_1d_threshold:
                active_1d += 1

    requests = _count_requests_for_day(target)

    stats_record = {
        "users_total": users_total,
        "requests": requests,
        "active_1d": active_1d,
        "active_7d": active_7d
    }

    stats = _load_stats()
    stats[target.isoformat()] = stats_record
    _save_stats(stats)

    return stats_record


if __name__ == "__main__":
    result = finalize_day()
    print(json.dumps(result, ensure_ascii=False, indent=2))
