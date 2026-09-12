from datetime import date


# Данные плановой работы
work_name = "Плановое техническое обслуживание сервера"
work_date = date(2026, 9, 20)
work_duration = 3
work_status = "Запланирована"
is_approved = True


def get_work_status(status):
    """Определяет текущий статус плановой работы."""
    if status == "Запланирована":
        return "Работа запланирована"
    elif status == "Выполняется":
        return "Работа выполняется"
    elif status == "Завершена":
        return "Работа завершена"
    else:
        return "Неизвестный статус"


def check_approval(approved):
    """Проверяет согласование плановой работы."""
    if approved:
        return "Работа согласована"
    else:
        return "Работа не согласована"


def check_duration(duration):
    """Проверяет длительность плановой работы."""
    if duration <= 0:
        return "Ошибка: длительность должна быть больше 0 часов"
    elif duration <= 4:
        return "Продолжительность работы допустима"
    else:
        return "Работа длительная, требуется дополнительное согласование"


print("=== Сервис управления плановыми работами ===")
print(f"Работа: {work_name}")
print(f"Дата выполнения: {work_date}")
print(f"Продолжительность: {work_duration} ч.")
print(f"Статус: {get_work_status(work_status)}")
print(f"Согласование: {check_approval(is_approved)}")
print(f"Проверка длительности: {check_duration(work_duration)}")