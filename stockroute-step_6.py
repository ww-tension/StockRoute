# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: StockRoute
def delete_record(record_id, confirm=False):
    if not confirm:
        print(f"Удаление записи {record_id} отменено (требуется флаг подтверждения).")
        return False
    
    try:
        # Имитация удаления из БД или структуры данных
        # Замените на реальный вызов функции удаления вашего проекта StockRoute
        deleted = _remove_from_storage(record_id) 
        
        if deleted:
            print(f"Запись {record_id} успешно удалена.")
            return True
        else:
            print(f"Ошибка: запись с ID {record_id} не найдена или недоступна для удаления.")
            return False
            
    except Exception as e:
        print(f"Произошла ошибка при удалении записи {record_id}: {e}")
        return False

def _remove_from_storage(record_id):
    """Внутренняя функция-заглушка. Замените на реальную логику удаления."""
    # Пример структуры данных для демонстрации (удаление из списка)
    if hasattr(delete_record, '_storage'):
        delete_record._storage = [item for item in delete_record._storage if item['id'] != record_id]
        return True
    return False

# Инициализация хранилища для тестирования (если файл запускается напрямую)
if __name__ == "__main__":
    # Пример данных для теста
    test_data = [
        {"id": 1, "type": "transfer", "status": "completed"},
        {"id": 2, "type": "checkpoint", "status": "active"}
    ]
    
    # Привязка хранилища к функции (для демонстрации работы без глобальных переменных)
    delete_record._storage = test_data
    
    print("=== Тестирование удаления ===")
    print(f"Текущие записи: {delete_record._storage}")
    
    # Попытка удалить без подтверждения
    result1 = delete_record(2, confirm=False)
    print(f"Результат попытки 1 (без подтверждения): {result1}")
    
    # Успешное удаление с подтверждением
    result2 = delete_record(2, confirm=True)
    print(f"Результат попытки 2 (с подтверждением): {result2}")
    
    print(f"Оставшиеся записи: {delete_record._storage}")
