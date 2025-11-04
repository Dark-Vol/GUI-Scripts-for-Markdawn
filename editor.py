# editor.py
import flet as ft

def main(page: ft.Page):
    # --- 1. Настройки окна ---
    page.title = "Flet Markdown Editor"
    page.window_width = 1200
    page.window_height = 800
    page.padding = 10
    
    # Устанавливаем светлую тему по умолчанию
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- 2. Логика приложения: обработчик событий ---
    def handle_text_change(e):
        """
        Вызывается при каждом изменении текста в поле ввода.
        Обновляет область предпросмотра.
        """
        preview_area.value = e.control.value
        page.update()

    # --- 3. Виджеты интерфейса ---
    input_field = ft.TextField(
        multiline=True,
        expand=True,
        min_lines=40,
        hint_text="Пишите ваш Markdown здесь...\n\n# Заголовок\n\n* Список\n* Элементов",
        # Убираем стандартную рамку для чистого вида
        border_color="transparent",
        on_change=handle_text_change,
    )

    preview_area = ft.Markdown(
        value="Здесь будет ваш **отформатированный** текст.",
        expand=True,
        # Выбираем тему для подсветки синтаксиса в блоках кода
        code_theme="atom-one-dark",
    )

    # --- 4. Сборка интерфейса ---
    app_layout = ft.Row(
        controls=[
            input_field,
            ft.VerticalDivider(),
            preview_area
        ],
        expand=True,
    )

    # --- 5. Добавляем все на страницу и обновляем ---
    page.add(app_layout)
    page.update()

# --- 6. Запуск приложения ---
if __name__ == "__main__":
    ft.app(target=main)
