import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def convert_units(value, from_unit, to_unit):
    """Функция конвертации"""
    if from_unit == 'C' and to_unit == 'F':
        return value * 9 / 5 + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5 / 9
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'F' and to_unit == 'K':
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value - 273.15) * 9 / 5 + 32
    elif from_unit == to_unit:
        return value


def perform_conversion():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        if not from_unit or not to_unit:
            raise ValueError("Выберите единицы измерения.")
        result = convert_units(value, from_unit, to_unit)
        label_result.config(text=f"Результат: {result:.5f} {to_unit}")
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))


# Создание окна
root = tk.Tk()
root.title("Конвертер единиц")

# Поле для ввода значения
tk.Label(root, text="Введите значение:").grid(row=0, column=0, padx=10, pady=10)
entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1, padx=10, pady=10)

# Выбор единиц "из"
tk.Label(root, text="Из:").grid(row=1, column=0, padx=10, pady=10)
combo_from = ttk.Combobox(root, values=['C', 'F', 'K'])
combo_from.grid(row=1, column=1, padx=10, pady=10)

# Выбор единиц "в"
tk.Label(root, text="В:").grid(row=2, column=0, padx=10, pady=10)
combo_to = ttk.Combobox(root, values=['C', 'F', 'K'])
combo_to.grid(row=2, column=1, padx=10, pady=10)

# Кнопка для выполнения конвертации
btn_convert = tk.Button(root, text="Конвертировать", command=perform_conversion)
btn_convert.grid(row=3, column=0, columnspan=2, pady=10)

# Результат
label_result = tk.Label(root, text="Результат:")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Запуск приложения
root.mainloop()
