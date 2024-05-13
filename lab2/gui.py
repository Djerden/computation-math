import flet as ft
import numpy as np
import matplotlib.pyplot as plt

CARD_BG_COLOR = ft.colors.GREY_900
CARD_WIDTH = 500
CARD_HEIGHT = 350

# Данные первой карточки
step_counter = 0
equation_type_choice = 0
equation = 0
method = 0

def choose_equation(x):
    if equation_type_choice == 0:
        if equation == 0:
            return 2*x**3 + 4*x**2 + 5*x + 15
        elif equation == 1:
            return 3*x**2 + 5*x + 4
        elif equation == 2:
            return 1 - 3*x + np.sin(x)
    else: 
        return 0
    # дописать для системы уравнений

# Данные второй карточки
a = 0
b = 0
eps = 0

def main(page: ft.page):
    page.theme_mode = 'dark'
    # 1 карточка - выбор уравнения и метода 
    
    def choose_button_click(event):
        global step_counter, equation_type_choice, equation, method
        
        if step_counter < len(step) - 1:
            step_counter += 1
        else:
            return
        
        if step_counter == 1:
            if equation_type_choice == 0:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(equation_single)])
                radio_group.value = equation
            else:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(equation_system)])
                radio_group.value = equation
        elif step_counter == 2:
            if equation_type_choice == 0:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(method_single)])
                radio_group.value = method
            else:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(method_system)])
                radio_group.value = method

        step_text.value = step[step_counter]
        first_card.update()

    def back_button_click(event):
        global step_counter, equation_type_choice, equation, method
        if step_counter > 0:
            step_counter -= 1
        else:
            return
        
        if step_counter == 0:
            radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(equation_type)])
            radio_group.value = equation_type_choice
        elif step_counter == 1:
            if equation_type_choice == 0:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(equation_single)])
                radio_group.value = equation
            else:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(equation_system)])
                radio_group.value = equation
        elif step_counter == 2:
            if equation_type_choice == 0:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(method_single)])
                radio_group.value = method
            else:
                radio_group.content = ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(method_system)])
                radio_group.value = method

        step_text.value = step[step_counter]
        first_card.update()
    
    def radio_group_change(event):
        global step_counter, equation_type_choice, equation, method
        if step_counter == 0:
            equation_type_choice = event.control.value
        elif step_counter == 1:
            equation = event.control.value
        elif step_counter == 2:
            method = event.control.value
    
    step = ["Choose the equation type:", "Choose the equation:", "Choose the method:"]
    equation_type = ["single", "system"]
    equation_single = ["2*x^3 + 4*x^2 + 5*x + 15", "3*x^2 + 5*x + 4", "1 - 3*x + sin(x)"]
    equation_system = ["система 1", "система 2", "система 3"]
    method_single = ["Newhon", "Chorde", "Simple iteration"]
    method_system = ["Simple iteration"]

    step_text = ft.Text(value=step[0])
    radio_group = ft.RadioGroup(content=ft.Column([ft.Radio(value=index, label=i) for index, i in enumerate(equation_type)]), value=0, on_change=radio_group_change)

    choose_button = ft.ElevatedButton(text='Choose', on_click=choose_button_click)
    back_button = ft.ElevatedButton(text='Back', on_click=back_button_click)
    buttons_row = ft.Row([back_button, choose_button], alignment=ft.MainAxisAlignment.CENTER)

    first_card = ft.Card(content=ft.Column([
        ft.Text(value='Choice Factory'), 
        ft.Column([step_text, radio_group]), 
        buttons_row
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), width=CARD_WIDTH, height=CARD_HEIGHT, color=CARD_BG_COLOR)


    # 2 карточка - ввод данных
    def solve_button_click(event):
        global a, b, eps
        a = float(a_imp.value)
        b = float(b_imp.value)
        eps = eps_imp.value

        x = np.linspace(a, b, 100)
        y = choose_equation(x)
        # Построение графика
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label="2*x^3 + 4*x^2 + 5*x + 15")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the function')
        plt.legend()
        plt.grid(True)

        # Сохранение графика в файл
        plt.savefig('graph.png')

        # Закрытие графика
        plt.close()

        graph.src = 'graph.png'
    
    a_imp = ft.TextField(label='a', width=150, height=50)
    b_imp = ft.TextField(label='b', width=150, height=50)
    eps_imp = ft.TextField(label='eps', width=150, height=50)

    choose_file_button = ft.ElevatedButton(text='Choose file')
    save_to_button = ft.ElevatedButton(text='Save to')
    solve_button = ft.ElevatedButton(text='Solve', on_click=solve_button_click)

    second_card = ft.Card(content=ft.Column([
        ft.Text(value='Enter a, b, and epsilon'), 
        ft.Row([a_imp, b_imp, eps_imp], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([choose_file_button, save_to_button, solve_button], alignment=ft.MainAxisAlignment.CENTER)
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), width=CARD_WIDTH, height=CARD_HEIGHT, color=CARD_BG_COLOR)
    
    
    # 3 карточка - вывод графика

    graph = ft.Image(src=f"/xoma.jpg", width=450, height=300, fit=ft.ImageFit.CONTAIN)
    third_card = ft.Card(content=ft.Column([
        ft.Text(value='Graph'), 
        graph
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), width=CARD_WIDTH, height=CARD_HEIGHT, color=CARD_BG_COLOR)
    
    
    # 4 карточка - вывод решения

    fourth_card = ft.Card(content=ft.Column([
        ft.Text(value='Results')
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER), width=CARD_WIDTH, height=CARD_HEIGHT, color=CARD_BG_COLOR)
   
    #добавление на старницу
    page.add(ft.Column([ft.Row([first_card, third_card], alignment=ft.MainAxisAlignment.CENTER), 
                        ft.Row([second_card, fourth_card], alignment=ft.MainAxisAlignment.CENTER)], 
                        alignment=ft.CrossAxisAlignment.CENTER))
    
if __name__ == "__main__":
    ft.app(target=main)








     # def button_click(event):
    #     radio_group.clean()
    #     radios = ["1", "2", "3", "4", "5"]
    #     radio_group.content = ft.Column([ft.Radio(value=i, label=i) for i in radios])
    #     radio_group.update()


    # button = ft.ElevatedButton(text='Catch me!', on_click=button_click)

    # radio_group = ft.RadioGroup(content=ft.Column([ft.Radio(value='0', label='Radio 1'), 
    #                                     ft.Radio(value='1', label='Radio 2'), 
    #                                     ft.Radio(value='2', label='Radio 3')]), value='1')

    # page.add(ft.Container(content=ft.Column([ft.Text(value='Catch me if you can!'), 
    #                                         radio_group,
    #                                         button]), bgcolor='black', width=200, height=200, alignment=ft.alignment.center))