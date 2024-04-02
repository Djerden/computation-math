import flet as ft 

# константы для цвета 
PAGE_COLOR = ft.colors.PINK_50
TEXT_COLOR = ft.colors.PINK_400
CONTEINER_BG_COLOR = ft.colors.PINK_100

# константы для размеры шрифта
TEXT_MAIN_SIZE = 30
MAIN_TEXT_CONTAINER_SIZE = 20
TEXT_CONTAINER_SIZE = 20

# константы для размера контейнеров
CONTAINER_WIDTH = 500
CONTAINER_HEIGHT = 600


def main(page: ft.Page):

    # page parameters 
    page.title = "PowSolver"
    page.bgcolor = PAGE_COLOR
    
    # page.theme_mode = "dark"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 

    # Header 
    page.controls.append(ft.Text(value="PowSolve", color=TEXT_COLOR, size=TEXT_MAIN_SIZE, weight=ft.FontWeight.BOLD))

# Left side
    # обьявления переменных (компонентов)
    label_style_for_radio = ft.TextStyle(color=TEXT_COLOR)

    def equation_type_radio_click(): 
        pass

    equation_type_radio = ft.RadioGroup(content=ft.Column([
    ft.Radio(value="0", label="Single", active_color=TEXT_COLOR, label_style=label_style_for_radio),
    ft.Radio(value="1", label="System", active_color=TEXT_COLOR, label_style=label_style_for_radio)]), on_change=equation_type_radio_click) # реализовать функцию, которая вызывается, когда происходит смена режима

    def method_type_radio_click():
        pass

    method_type_radio = ft.RadioGroup(content=ft.Column([
    ft.Radio(value="0", label="Newhon", active_color=TEXT_COLOR, label_style=label_style_for_radio),
    ft.Radio(value="1", label="Chorde", active_color=TEXT_COLOR, label_style=label_style_for_radio), 
    ft.Radio(value="2", label="Simple iteration (for single)", active_color=TEXT_COLOR, label_style=label_style_for_radio),
    ft.Radio(value="3", label="Simple iteration (for system)", active_color=TEXT_COLOR, label_style=label_style_for_radio)]), on_change=method_type_radio_click)

    def equation_radio_click():
        pass

    equation_radio = ft.RadioGroup(content=ft.Column([
    ft.Radio(value="0", label="какое-то уравнение", active_color=TEXT_COLOR, label_style=label_style_for_radio),
    ft.Radio(value="1", label="какое-то уравнение", active_color=TEXT_COLOR, label_style=label_style_for_radio), 
    ft.Radio(value="2", label="какое-то уравнение", active_color=TEXT_COLOR, label_style=label_style_for_radio),
    ft.Radio(value="3", label="какое-то уравнение", active_color=TEXT_COLOR, label_style=label_style_for_radio)]), on_change=equation_radio_click)


    #Формирование левой колонки
    left_column = ft.Column([
        ft.Text(value="ChoiceFactory", color=TEXT_COLOR, size=MAIN_TEXT_CONTAINER_SIZE), 
        
        #Место для radio кнопок
        ft.Text(value="Choose the equation type:", color=TEXT_COLOR, size=TEXT_CONTAINER_SIZE),
        equation_type_radio, 
        ft.Text(value="Choose the method:", color=TEXT_COLOR, size=TEXT_CONTAINER_SIZE),
        method_type_radio, 
        ft.Text(value="Choose the equation:", color=TEXT_COLOR, size=TEXT_CONTAINER_SIZE),
        equation_radio,
    ])
    left_container = ft.Container(content=left_column, bgcolor=CONTEINER_BG_COLOR, alignment=ft.alignment.center, width=CONTAINER_WIDTH, height=CONTAINER_HEIGHT)


# Right side 
    # обьявление переменных (компонентов)
    graph = ft.Image(src=f"/xoma.jpg", width=450, height=250, fit=ft.ImageFit.CONTAIN)
    
    # Формирование правой колонки
    
    # Часть с графиком  
    right_top_column = ft.Column([
        ft.Text(value="Graph", color=TEXT_COLOR, size=MAIN_TEXT_CONTAINER_SIZE),
        graph
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    # Часть с вводом
    inp_width = 150
    inp_height = 50
    inp_hint_style = ft.TextStyle(color=TEXT_COLOR)

    # поля ввода 
    a_inp = ft.TextField(label="a", width=inp_width, height=inp_height, color=TEXT_COLOR, border_color=TEXT_COLOR, label_style=inp_hint_style)
    b_inp = ft.TextField(label="b", width=inp_width, height=inp_height, color=TEXT_COLOR, border_color=TEXT_COLOR, label_style=inp_hint_style)
    eps_inp = ft.TextField(label="epsilon", width=inp_width, height=inp_height, color=TEXT_COLOR, border_color=TEXT_COLOR, label_style=inp_hint_style)

    def solve_button_click():
        pass

    right_bottom_column = ft.Column([
        ft.Text(value="Please, enter the values a, b, and epsilon", color=TEXT_COLOR, size=MAIN_TEXT_CONTAINER_SIZE),
        # Поля для ввода
        
        ft.Row([
            a_inp,
            b_inp,
            eps_inp 
        ], alignment=ft.MainAxisAlignment.CENTER), 

        # Button Solve
        ft.ElevatedButton(text="Solve", color=TEXT_COLOR, bgcolor=PAGE_COLOR, width=100, on_click=solve_button_click) # Реализовать метод, который вызовется при нажатии 
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    

    right_top_container = ft.Container(content=right_top_column, bgcolor=CONTEINER_BG_COLOR, alignment=ft.alignment.center, width=500, height=300)
    right_bottom_container = ft.Container(content=right_bottom_column, bgcolor=CONTEINER_BG_COLOR, alignment=ft.alignment.center, width=500, height=290)

    #правый обьединяющий контейнер
    right_container = ft.Container(content=ft.Column([right_top_container, right_bottom_container]), alignment=ft.alignment.center, width=CONTAINER_WIDTH, height=CONTAINER_HEIGHT)

    
    
    page.add(ft.Row([left_container, right_container], alignment=ft.MainAxisAlignment.CENTER))
    page.update()

ft.app(target=main)
