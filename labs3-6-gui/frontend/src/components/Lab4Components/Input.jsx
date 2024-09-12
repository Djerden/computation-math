import {useState} from 'react'

export default function Input({pairs, setPairs, sendRequest}) {

    const [inputValues, setInputValues] = useState(Array(12).fill("")); // Временное состояние для ввода

    console.log(pairs)
    console.log(inputValues)
    // Массив для элементов ввода
    const inputs = Array.from({length: 12}, (_, i) => i + 1);

    function transformInput(input) {
        // Разбиваем строку на части по любому количеству пробелов
        const [x, y] = input.trim().replace(',', '.').split(/\s+/).map(Number);
        // вернем обьект { x: x, y: y }
        return {x, y};
    }

    // функция сохранения значений из ввода в состояние
    function handlePairChange(index, value) {
        setInputValues((prevState) => {
            const updatedValues = [...prevState];
            updatedValues[index] = value;
            return updatedValues;
        })

        setPairs((prevPairs) => {
            const updatedPairs = [...prevPairs];
            updatedPairs[index] = transformInput(value);
            return updatedPairs;
        });
    }

    // функция для загрузки и чтения файла
    function handleFileChange(event) {

        clearButton();

        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {

            const text = e.target.result;
            const lines = text.split('\n').filter(line => line.trim() !== ""); // Игнорируем пустые строки

            // Проверка, что файл содержит хотя бы одну строку
            if (lines.length === 0) {
                alert("Файл пустой или не содержит валидных данных.");
                return;
            }

            setTimeout(() => {
                const newInputValues = Array(12).fill(""); // Заново создаем массив
                const newPairs = Array(12).fill({x: null, y: null}); // Заново создаем массив
                let invalidDataFound = false; // Флаг для обнаружения некорректных данных



                lines.forEach((line, index) => {
                    const [x, y] = line.trim().replace(',', '.').split(/\s+/).map(Number);
                    // Проверяем, что обе части являются числами
                    if (!isNaN(x) && !isNaN(y)) {
                        // Сохраняем значения в состояния
                        newInputValues[index] = `${x} ${y}`;
                        newPairs[index] = {x, y};
                    } else {
                        invalidDataFound = true; // Некорректные данные найдены
                    }
                });

                // Если были найдены некорректные данные, выбрасываем alert
                // Если были найдены некорректные данные, выбрасываем alert, но продолжаем
                if (invalidDataFound) {
                    alert("Некоторые строки содержат некорректные данные и были отброшены.");
                }

                // Обновляем состояния новыми значениями
                setInputValues(newInputValues);
                setPairs(newPairs);
            }, 0); // Таймаут 0 мс, чтобы дождаться завершения обновления состояний
        }

        reader.onerror = function () {
            alert("Ошибка при чтении файла.");
        };

        reader.readAsText(file);
    }

    function validateInput() {
        // Фильтруем пары, где x и y не null и не NaN
        const validPairs = pairs.filter(pair => pair.x !== null && pair.y !== null && !isNaN(pair.x) && !isNaN(pair.y));

        // Проверяем, что количество пар от 8 до 12
        if (validPairs.length < 8 || validPairs.length > 12) {
            alert("Количество валидных пар должно быть от 8 до 12.");
            return false;
        }

        return true; // Если все проверки пройдены
    }

    function solveClick() {
        // Если валидация не пройдена, выходим из функции
        if (!validateInput()) {
            return;
        }

        // Фильтруем массив, удаляя элементы, где x или y равны null или NaN
        const filteredPairs = pairs.filter(pair => pair.x !== null && pair.y !== null && !isNaN(pair.x) && !isNaN(pair.y));

        // Отправляем новый массив в sendRequest
        sendRequest(filteredPairs);
    }

    function clearButton() {
        // Сбрасываем inputValues в массив пустых строк
        setInputValues(Array(12).fill(""));

        // Сбрасываем pairs в массив объектов с x и y равными null
        setPairs(Array(12).fill({x: null, y: null}));
    }

    return (
        <div className="flex flex-col">
            <div className="flex flex-col bg-white text-black p-6 gap-2 rounded-t">
                <h1 className="text-2xl font-bold">Pairs Factory</h1>
                <h2>Enter pair x and y (use space)</h2>

                <div className="flex flex-col gap-2">
                    {inputs.map((num, index) => (
                        <p className="flex flex-row gap-1" key={num}>
                            <label className="flex flex-col justify-center w-6 text-right">{num}</label>
                            <input
                                className={`w-2/3 border border-black rounded px-2 py-1`}
                                type="text"
                                placeholder="x y"
                                value={inputValues[index]}
                                onChange={(e) => handlePairChange(index, e.target.value)}
                            />
                        </p>
                    ))}
                </div>
                <button
                    className="bg-black px-6 w-full rounded hover:bg-neutral-700 text-white"
                    onClick={clearButton}
                >Очистить
                </button>
            </div>
            <div className="flex flex-row items-center bg-custom-644e5b p-6 text-white rounded-b">
                <input type="file"
                       accept=".txt"
                       onChange={handleFileChange}
                />
                <button
                    className="bg-black px-6 w-full rounded hover:bg-neutral-700"
                    onClick={solveClick}
                >Solve
                </button>
            </div>
        </div>
    );
}