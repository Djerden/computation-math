import {useState} from "react";

export default function Input({requestFunction}) {

    const [inputs, setInputs] = useState({
        y0: '',
        x0: '',
        xn: '',
        h: '',
        eps: '',
        function: "y' = x^2 - 2y"
    });

    function changeInputs(key, value) {
        if (!(key in inputs)) {
            return;
        }
        setInputs((prevState) => ({
            ...prevState,
            [key]: value
        }));
    }

    function isValidInputs(data) {
        const { y0, x0, xn, h, eps } = data;

        // Проверяем, что все поля (кроме function) являются числами или null
        if (y0 === null || x0 === null || xn === null || h === null || eps === null) {
            alert('Все поля должны быть заполнены.');
            return false;
        }

        // Проверяем, что все поля (кроме function) являются числами
        if (isNaN(y0) || isNaN(x0) || isNaN(xn) || isNaN(h) || isNaN(eps)) {
            alert('Все поля должны быть числовыми значениями, кроме поля function.');
            return false;
        }

        // Проверяем условия
        if (eps < 0 || eps > 1) {
            alert('Значение eps должно быть в диапазоне от 0 до 1.');
            return false;
        }

        if (h <= 0) {
            alert('Значение h должно быть положительным.');
            return false;
        }

        if (x0 >= xn) {
            alert('Значение x0 должно быть меньше значения xn.');
            return false;
        }

        return true;
    }

    function solveClick() {

        const data = {
            y0: inputs.y0.trim() ? Number(inputs.y0.replace(',', '.')) : null,
            x0: inputs.x0.trim() ? Number(inputs.x0.replace(',', '.')) : null,
            xn: inputs.xn.trim() ? Number(inputs.xn.replace(',', '.')) : null,
            h: inputs.h.trim() ? Number(inputs.h.replace(',', '.')) : null,
            eps: inputs.eps.trim() ? Number(inputs.eps.replace(',', '.')) : null,
            function: inputs.function // Оставляем как строку
        };
        console.log(data)

        if (!isValidInputs(data)) {
            console.log('Некорректный ввод')
            return;
        }

        requestFunction(data)
    }

    return (
        <div className="flex flex-col">
            <div className="flex flex-col bg-white rounded p-6 gap-4">
                <div className="flex flex-col gap-1 min-w-[300px]">
                    <h1 className="text-2xl font-bold">Input</h1>
                    <h2><b>Enter the initial condition:</b></h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="y0"
                        value={inputs.y0}
                        onChange={(e) => {
                            changeInputs('y0', e.target.value)
                        }}
                    />
                    <h2><b>Enter the differentiation interval:</b></h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="x0"
                        value={inputs.x0}
                        onChange={(e) => {
                            changeInputs('x0', e.target.value)
                        }}
                    />
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="xn"
                        value={inputs.xn}
                        onChange={(e) => {
                            changeInputs('xn', e.target.value)
                        }}
                    />
                    <h2><b>Enter the step value:</b></h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="h"
                        value={inputs.h}
                        onChange={(e) => {
                            changeInputs('h', e.target.value)
                        }}
                    />
                    <h2><b>Enter the accuracy:</b></h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="eps"
                        value={inputs.eps}
                        onChange={(e) => {
                            changeInputs('eps', e.target.value)
                        }}
                    />
                </div>
                <div>
                    <h2><b>Select a function:</b></h2>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="equation"
                            value="y' = x^2 - 2y"
                            checked={inputs.function === "y' = x^2 - 2y"}
                            onChange={(e) => {changeInputs('function', e.target.value)}}/>
                        <label>y' = x^2 - 2y</label>
                    </p>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="equation"
                            value="y' = y + (1+x) * y^2"
                            checked={inputs.function === "y' = y + (1+x) * y^2"}
                            onChange={(e) => {changeInputs('function', e.target.value)}}/>
                        <label>y' = y + (1+x) * y^2</label>
                    </p>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="equation"
                            value="y' = 2x - 3y"
                            checked={inputs.function === "y' = 2x - 3y"}
                            onChange={(e) => {changeInputs('function', e.target.value)}}/>
                        <label>y' = 2x - 3y</label>
                    </p>
                </div>
            </div>
            <div>
                <div className="flex flex-row items-center bg-custom-644e5b p-6 text-white rounded-b">
                    <button
                        className="bg-black px-6 w-full rounded hover:bg-neutral-700"
                        onClick={solveClick}
                    >Solve
                    </button>
                </div>
            </div>
        </div>
    );
}