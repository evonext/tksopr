import tkinter as tk
from tkinter import messagebox

def calculate_resistance():
    try:
        r1 = float(entry_r1.get())
        r2 = float(entry_r2.get())
        if r1 <= 0 or r2 <= 0:
            raise ValueError("Resistance values must be positive.")
        total_resistance = 1 / (1 / r1 + 1 / r2)
        entry_total_resistance.delete(0, tk.END)
        entry_total_resistance.insert(0, f"{total_resistance:.2f}")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

def clear_entries():
    entry_r1.delete(0, tk.END)
    entry_r2.delete(0, tk.END)
    entry_total_resistance.delete(0, tk.END)

# Создаем главное окно
root = tk.Tk()
root.title("Вычисление сопротивления электрической цепи")

# Создаем и размещаем виджеты
label_prompt = tk.Label(root, text="Введите исходные данные:")
label_prompt.grid(row=0, column=0, columnspan=2, pady=10)

label_r1 = tk.Label(root, text="Величина первого сопротивления (Ом) ->")
label_r1.grid(row=1, column=0, padx=10, pady=5)
entry_r1 = tk.Entry(root)
entry_r1.grid(row=1, column=1, padx=10, pady=5)

label_r2 = tk.Label(root, text="Величина второго сопротивления (Ом) ->")
label_r2.grid(row=2, column=0, padx=10, pady=5)
entry_r2 = tk.Entry(root)
entry_r2.grid(row=2, column=1, padx=10, pady=5)

label_total_resistance = tk.Label(root, text="Сопротивление цепи (Ом) ->")
label_total_resistance.grid(row=3, column=0, padx=10, pady=5)
entry_total_resistance = tk.Entry(root)
entry_total_resistance.grid(row=3, column=1, padx=10, pady=5)

button_calculate = tk.Button(root, text="Выполнить", command=calculate_resistance)
button_calculate.grid(row=4, column=0, padx=10, pady=10)

button_clear = tk.Button(root, text="Очистить", command=clear_entries)
button_clear.grid(row=4, column=1, padx=10, pady=10)

# Запуск основного цикла
root.mainloop()
