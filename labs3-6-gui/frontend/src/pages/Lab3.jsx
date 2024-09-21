import {useState} from "react";

import ChoiceFactory from "../components/Lab3Components/ChoiceFactory.jsx";
import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab3Components/Input.jsx";
import Solution from "../components/Lab3Components/Solution.jsx";

export default function Lab3() {

    // Состояние для выбора уравнения и метода интегрирования
    const [choice, setChoice] = useState({
        equation: 'x^2',
        method: 'rectangle-left'
    }); // ['x^2', 'sin(x)', '1/x']

    // Состояние для ввода данных
    const [inputData, setInputData] = useState({
        a: null,
        b: null,
        eps: null,
        n: null
    });

    // Состояние для подсказок
    const [tips, setTips] = useState({
        a: false,
        b: false,
        eps: false,
        n: false
    });

    // Состояние для ответа
    const [answer, setAnswer] = useState({
        square: null,
        parts: null,
        inaccuracy: null
    });


    // Функция для сохранения выбора уравнения и метода интегрирования
    function handleChangeChoice(param, value) {
        setChoice({...choice, [param]: value});
    }

    // Функция для сохранения ввода из полей ввода
    function handleChangeInputData(param, value) {
        let numericValue = parseFloat(value.replace(',', '.').replace(/\s+/g, ''));
        setInputData(prevInputData => ({
            ...prevInputData,    // Сохраняем все предыдущие значения
            [param]: numericValue // Обновляем конкретное поле
        }));
    }

    // Валидация введенных данных
    function validateInput() {
        let isValid = true;
        // Сбрасываем все подсказки
        setTips(prevTips => ({
            ...prevTips,
            a: false,
            b: false,
            eps: false,
            n: false
        }));

        if (choice.equation == null || choice.method == null) {
            console.log('Выберите уравнение и метод интегрирования');
            if (isValid === true) {
                isValid = false;
            }
        }
        if (typeof inputData.a !== 'number' || isNaN(inputData.a)) {
            console.log('Ошибка: "a" должно быть числом.');
            if (isValid === true) {
                isValid = false;
            }
            setTips(prevTips => ({...prevTips, a: true}));
        }

        if (typeof inputData.b !== 'number' || isNaN(inputData.b)) {
            console.log('Ошибка: "b" должно быть числом.');
            if (isValid === true) {
                isValid = false;
            }
            setTips(prevTips => ({...prevTips, b: true}));
        }

        // Проверка eps
        if (typeof inputData.eps !== 'number' || isNaN(inputData.eps) || inputData.eps < 0 || inputData.eps > 1) {
            console.log('Ошибка: "eps" должно быть числом в диапазоне от 0 до 1 включительно.');
            if (isValid === true) {
                isValid = false;
            }
            setTips(prevTips => ({...prevTips, eps: true}));
        }

        // Проверка n
        if (typeof inputData.n !== 'number' || isNaN(inputData.n) || inputData.n < 4 || !Number.isInteger(inputData.n)) {
            console.log('Ошибка: "n" должно быть положительным целым числом, не меньше 4');
            if (isValid === true) {
                isValid = false;
            }
            setTips(prevTips => ({...prevTips, n: true}));
        }

        // Если все проверки прошли успешно
        return isValid;
    }

    // Запрос на сервер
    function solveClick() {
        console.log(choice);
        console.log(inputData);

        if (!validateInput()) return;

        fetch('http://localhost:8000/lab3', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                choice: choice,
                inputData: inputData
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setAnswer(prevState => ({
                    ...prevState,
                    square: data.square,
                    parts: data.parts,
                    inaccuracy: data.inaccuracy
                }));

            })
            .catch(error => {
                console.error('Error:', error)
            });
    }

    return (
        <>
            <MainTextComponent labName="Numerical integration">Lab #3</MainTextComponent>
            <div className="flex flex-row flex-wrap gap-6 justify-start mx-6">
                {/* Left side */}
                <div className="flex flex-col gap-6 md:w-1/3 w-full">
                    {/*Choice Factory*/}
                    <ChoiceFactory onChangeChoice={handleChangeChoice}/>

                    {/*Inputs*/}
                    <Input
                        data={inputData} tips={tips} onChange={handleChangeInputData} solveClick={solveClick}/>
                </div>

                {/* Right side */}
                <Solution choice={choice} data={inputData} answer={answer}/>
            </div>
        </>
    );
}