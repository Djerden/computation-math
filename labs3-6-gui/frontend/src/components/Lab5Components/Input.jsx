import {useState} from "react";

export default function Input({requestFunction}) {

    const [inputMethod, setInputMethod] = useState("hand");

    const [handData, setHandData] = useState({
        x: [],
        y: []
    });
    const [handDataInputs, setHandDataInputs] = useState({
        x: '',
        y: ''
    });

    const [functionData, setFunctionData] = useState({
        function: 'sin(x)',
        a: null,
        b: null,
        points: null
    });
    const [functionDataInputs, setFunctionDataInputs] = useState({
        function: 'sin(x)',
        a: '',
        b: '',
        points: ''
    });

    const [fileData, setFileData] = useState({
        x: [],
        y: []
    });
    const [fileDataInputs, setFileDataInputs] = useState({
        x: '',
        y: ''
    });

    const [interpolationPoint, setInterpolationPoint] = useState(null);
    const [interpolationPointInput, setInterpolationPointInput] = useState('');



    function changeInputMethod(event) {
        setInputMethod(() => (event.target.value))
    }

    function renderInputMethod() {
        switch (inputMethod) {
            case 'hand':
                return handPage;
            case 'function':
                return functionPage;
            case 'file':
                return filePage;
            default:
                return null;
        }
    }

    // функция для загрузки и чтения файла
    function handleFileChange(event) {

        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {

            const text = e.target.result;
            const lines = text.split('\n').filter(line => line.trim() !== ""); // Разбиваем файл по строкам и убираем пустые строки

            // Проверка, что в файле есть хотя бы две строки для X и Y
            if (lines.length < 2) {
                alert("The file must contain at least two lines: one for X and one for Y");
                return;
            }

            // Разбиваем строки по пробелам и преобразуем в массивы чисел
            const xValues = lines[0].trim().replace(',', '.').split(/\s+/).map(Number); // X координаты
            const yValues = lines[1].trim().replace(',', '.').split(/\s+/).map(Number); // Y координаты

            // Проверяем, что обе строки содержат одинаковое количество значений
            if (xValues.length !== yValues.length) {
                alert("The X and Y lines must contain the same number of values");
                return;
            }

            // Проверка, что все элементы являются числами
            const invalidX = xValues.some(value => isNaN(value));
            const invalidY = yValues.some(value => isNaN(value));

            if (invalidX || invalidY) {
                alert("Some values in the X or Y strings are not numbers");
                return;
            }

            // Обновляем состояния: fileData и fileDataInputs
            setFileData({
                x: xValues,
                y: yValues
            });

            setFileDataInputs({
                x: lines[0].trim(),
                y: lines[1].trim()
            });

        }
        reader.onerror = function () {
            alert("Error reading the file");
        };

        reader.readAsText(file);
    }

    function clearButton() {
        // Очищаем общие состояния для interpolationPoint и interpolationPointInput
        setInterpolationPoint(null);
        setInterpolationPointInput('');

        // Очищаем данные в зависимости от метода ввода (inputMethod)
        if (inputMethod === "file") {
            setFileData({ x: [], y: [] });
            setFileDataInputs({ x: '', y: '' });
        } else if (inputMethod === "hand") {
            setHandData({ x: [], y: [] });
            setHandDataInputs({ x: '', y: '' });
        } else if (inputMethod === "function") {
            setFunctionData({
                function: 'sin(x)', // Сброс функции к значению по умолчанию
                a: null,
                b: null,
                points: null
            });
            setFunctionDataInputs({
                function: 'sin(x)',
                a: '',
                b: '',
                points: ''
            });
        }
    }

    function validateInputs() {
        if (inputMethod === "hand") {
            // Проверяем ручной ввод
            if (handData.x.length === 0 || handData.y.length === 0) {
                alert("Please enter valid X and Y coordinates for manual input.");
                return false;
            }

            if (handData.x.some(isNaN) || handData.y.some(isNaN)) {
                alert("Manual input contains non-numeric values.");
                return false;
            }

            if (handData.x.length !== handData.y.length) {
                alert("The number of X and Y coordinates must be equal.");
                return false;
            }
        } else if (inputMethod === "function") {
            // Проверяем ввод по функции
            if (functionData.a === null || functionData.b === null || functionData.points === null) {
                alert("Please enter valid values for the function inputs.");
                return false;
            }

            if (isNaN(functionData.a) || isNaN(functionData.b) || isNaN(functionData.points)) {
                alert("Function inputs must be valid numbers.");
                return false;
            }

            if (functionData.a >= functionData.b) {
                alert("The start of the interval (a) must be less than the end (b).");
                return false;
            }

            if (functionData.points <= 0) {
                alert("The number of points must be a positive integer.");
                return false;
            }
        } else if (inputMethod === "file") {
            // Проверяем ввод из файла
            if (fileData.x.length === 0 || fileData.y.length === 0) {
                alert("Please upload a file with valid X and Y coordinates.");
                return false;
            }

            if (fileData.x.some(isNaN) || fileData.y.some(isNaN)) {
                alert("File input contains non-numeric values.");
                return false;
            }

            if (fileData.x.length !== fileData.y.length) {
                alert("The number of X and Y coordinates in the file must be equal.");
                return false;
            }
        }

        // Проверяем значение интерполяционной точки
        if (interpolationPoint === null || isNaN(interpolationPoint)) {
            alert("Please enter a valid interpolation point.");
            return false;
        }

        // Если все проверки пройдены
        return true;
    }

    function solveClick() {
        // валидация и преобразование данных
        if (!validateInputs()) {
            return;
        }
        console.log('Валидация пройдена')
        // Создаем объект data
        const data = {
            interpolationPoint,  // Добавляем interpolationPoint в любом случае
        };

        // В зависимости от inputMethod добавляем соответствующие данные
        if (inputMethod === "hand") {
            data.x = handData.x;
            data.y = handData.y;
        } else if (inputMethod === "function") {
            const func = functionData.function;  // 'sin' или 'cos'
            const a = parseFloat(functionData.a);  // Начало интервала
            const b = parseFloat(functionData.b);  // Конец интервала
            const points = parseInt(functionData.points);  // Количество точек

            // Проверка значений a, b и points
            if (isNaN(a) || isNaN(b) || isNaN(points)) {
                console.error('The values of a, b and the number of points must be numbers');
                return;
            }

            // Проверка корректности интервала и количества точек
            if (b <= a) {
                console.error('The value of b must be greater than a');
                return;
            }
            if (points <= 1) {
                console.error('The number of points must be greater than 1');
                return;
            }

            // Ограничение максимального числа точек
            const MAX_POINTS = 1000;
            if (points > MAX_POINTS) {
                console.error(`Количество точек не должно превышать ${MAX_POINTS}`);
                return;
            }

            // Проверка функции
            if (func !== 'sin(x)' && func !== 'cos(x)') {
                console.error('Поддерживаются только функции sin и cos');
                return;
            }

            // Проверка точки интерполяции
            if (interpolationPoint < a || interpolationPoint > b) {
                console.error('Точка интерполяции должна находиться в пределах интервала');
                alert('The interpolation point must be within the interval')
                return;
            }

            // Вычисление шагового интервала
            const step = (b - a) / (points - 1);
            const x = [];
            const y = [];

            // Вычисление точек x и соответствующих y
            for (let i = 0; i < points; i++) {
                const xi = a + i * step;  // Точка x
                x.push(xi);

                // Вычисление соответствующего значения y
                if (func === 'sin(x)') {
                    y.push(Math.sin(xi));
                } else if (func === 'cos(x)') {
                    y.push(Math.cos(xi));
                }
            }

            // Добавление данных в объект data
            data.x = x;
            data.y = y;
        } else if (inputMethod === "file") {
            data.x = fileData.x;
            data.y = fileData.y;
        }

        console.log('Данные для отправки:')
        console.log(data)
        requestFunction(data);
    }


    function changeHandData(param, event) {
        const value = event.target.value;

        if (param === 'x') {
            // Обновляем состояние для input и преобразуем строку в массив чисел
            setHandDataInputs({ ...handDataInputs, x: value });
            const xArray = value.split(/\s+/).filter(Boolean).map(Number); // Разделяем строку по любым пробельным символам
            setHandData({ ...handData, x: xArray });
        } else if (param === 'y') {
            // Обновляем состояние для input и преобразуем строку в массив чисел
            setHandDataInputs({ ...handDataInputs, y: value });
            const yArray = value.split(/\s+/).filter(Boolean).map(Number); // Разделяем строку по любым пробельным символам
            setHandData({ ...handData, y: yArray });
        }
    }

    const handPage = (
        <div className="flex flex-col gap-2">
            <div className="flex flex-col">
                <h2><b>Enter the X coordinates (use space):</b></h2>
                <input
                    className="border border-black rounded px-2 py-1"
                    type="text"
                    value={handDataInputs.x}
                    onChange={(event) => changeHandData('x', event)}
                />
            </div>
            <div className="flex flex-col">
                <h2><b>Enter the Y coordinates (use space):</b></h2>
                <input
                    className="border border-black rounded px-2 py-1"
                    type="text"
                    value={handDataInputs.y}
                    onChange={(event) => changeHandData('y', event)}
                />
            </div>
        </div>
    )

    function changeFunctionData(param, event) {
        const value = event.target.value;

        if (param === 'function') {
            setFunctionData({...functionData, function: value})
            setFunctionDataInputs({ ...functionDataInputs, function: value });
        } else if (param === 'a') {
            // Проверка на валидность числа для 'a'
            if (isNaN(Number(value))) {
                return;
            }
            setFunctionData({ ...functionData, a: Number(value) });
            setFunctionDataInputs({ ...functionDataInputs, a: value });
        } else if (param === 'b') {
            // Проверка на валидность числа для 'b'
            if (isNaN(Number(value))) {
                return;
            }
            setFunctionData({ ...functionData, b: Number(value) });
            setFunctionDataInputs({ ...functionDataInputs, b: value });
        } else if (param === 'points') {
            // Проверка на валидность числа для 'points'
            if (isNaN(Number(value))) {
                return;
            }
            setFunctionData({ ...functionData, points: Number(value) });
            setFunctionDataInputs({ ...functionDataInputs, points: value });
        }
    }

    const functionPage = (
        <div className="flex flex-col">
            <h2><b>Select a function</b></h2>
            <p className="space-x-2">
                <input
                    type="radio"
                    name="function"
                    value="sin(x)"
                    checked={functionDataInputs.function === 'sin(x)'}
                    onChange={(event) => changeFunctionData('function', event)}/>
                <label>sin(x)</label>
            </p>
            <p className="space-x-2">
                <input
                    type="radio"
                    name="function"
                    value="cos(x)"
                    checked={functionDataInputs.function === 'cos(x)'}
                    onChange={(event) => changeFunctionData('function', event)}/>
                <label>cos(x)</label>
            </p>
            <div className="flex flex-col gap-2">
                <div className="flex flex-col">
                    <h2><b>Enter beginning of the interval:</b></h2>
                    <input
                        className="border border-black rounded px-2 py-1"
                        type="number"
                        step="1"
                        value={functionDataInputs.a}
                        onChange={(event) => changeFunctionData('a', event)}
                    />
                </div>
                <div className="flex flex-col">
                    <h2><b>Enter end of the interval:</b></h2>
                    <input
                        className="border border-black rounded px-2 py-1"
                        type="number"
                        step="1"
                        value={functionDataInputs.b}
                        onChange={(event) => changeFunctionData('b', event)}
                    />
                </div>
                <div className="flex flex-col">
                    <h2><b>Enter number of points:</b></h2>
                    <input
                        className="border border-black rounded px-2 py-1"
                        type="number"
                        step="1"
                        value={functionDataInputs.points}
                        onChange={(event) => changeFunctionData('points', event)}
                    />
                </div>
            </div>
        </div>
    );

    const filePage = (
        <div className="flex flex-col gap-2">
            <div className="flex flex-col">
                <h2><b>X coordinates:</b></h2>
                <input
                    className="border border-black rounded px-2 py-1"
                    type="text"
                    value={fileDataInputs.x}
                    readOnly/>
            </div>
            <div className="flex flex-col">
                <h2><b>Y coordinates:</b></h2>
                <input
                    className="border border-black rounded px-2 py-1"
                    type="text"
                    value={fileDataInputs.y}
                    readOnly/>
            </div>
            <div>
                <h2><b>Select a file:</b></h2>
                <input type="file"
                       accept=".txt"
                       onChange={handleFileChange}
                />
            </div>
        </div>
    );

    function changeInterpolationPoint(event) {
        const value = event.target.value;

        // Преобразуем введенное значение в число с плавающей точкой
        const floatValue = parseFloat(value.replace(',', '.')); // Заменяем запятую на точку, если пользователь использует запятую

        if (isNaN(floatValue)) {
            // Если введено не число — устанавливаем null
            setInterpolationPoint(null);
        } else {
            // Если значение является числом, обновляем состояние
            setInterpolationPoint(floatValue);
        }

        // В любом случае обновляем строковое значение для отображения в инпуте
        setInterpolationPointInput(value);
    }

    return (
        <div>
            <div className="flex flex-col bg-white rounded p-6 gap-3">
                <h1 className="text-2xl font-bold">Input</h1>
                <div className="gap-2">
                    <h2><b>Select the data entry method:</b></h2>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="input-choice"
                            value="hand" // hand page
                            checked={inputMethod === "hand"}
                            onChange={changeInputMethod}/>
                        <label>Entering points</label>
                    </p>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="input-choice"
                            value="function" // function page
                            onChange={changeInputMethod}
                            checked={inputMethod === "function"}/>
                        <label>By function</label>
                    </p>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="input-choice"
                            value="file" // file page
                            onChange={changeInputMethod}
                            checked={inputMethod === "file"}/>
                        <label>From file</label>
                    </p>
                </div>
                <hr className="border-0 h-0.5 bg-black my-1"/>
                <div className="min-w-[300px] min-h-[260px]">
                    {renderInputMethod()}
                </div>
                <hr className="border-0 h-0.5 bg-black my-1"/>
                <div className="flex flex-col gap-2">
                    <h2><b>Enter value of the interpolation point:</b></h2>
                    <input
                        className="border border-black rounded px-2 py-1"
                        type="number"
                        step="1"
                        value={interpolationPointInput}
                        onChange={changeInterpolationPoint}
                    />
                </div>
                <div>
                    <button
                        className="bg-black px-6 rounded hover:bg-neutral-700 text-white"
                        onClick={clearButton}
                    >Clear
                    </button>
                </div>
            </div>
            <div className="flex flex-row items-center bg-custom-644e5b p-6 text-white rounded-b">
                <button
                    className="bg-black px-6 w-full rounded hover:bg-neutral-700"
                    onClick={solveClick}
                >Solve
                </button>
            </div>
        </div>
    );
}