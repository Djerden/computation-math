import {useState} from 'react'

export default function Input({pairs, setPairs, sendRequest}) {

    const [inputValues, setInputValues] = useState(Array(12).fill("")); // Временное состояние для ввода


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
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {

            const text = e.target.result;
            const lines = text.split('\n').filter(line => line.trim() !== ""); // Игнорируем пустые строки

            const newInputValues = [...inputValues];
            const newPairs = [...pairs];

            lines.forEach((line, index) => {
                const [x, y] = line.trim().replace(',', '.').split(/\s+/).map(Number);
                // Проверяем, что обе части являются числами
                if (!isNaN(x) && !isNaN(y)) {
                    // Сохраняем значения в состояния
                    newInputValues[index] = `${x} ${y}`;
                    newPairs[index] = {x, y};
                }
            });

            // Обновляем состояния
            setInputValues(() => newInputValues);
            setPairs(() => newPairs);
        }
        reader.readAsText(file);
    }

    function validateInput() {
        return true;
    }

    function solveClick() {
        if (!validateInput()) {
            return
        }
        sendRequest()
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