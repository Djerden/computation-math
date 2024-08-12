import {useRef, useEffect, useState} from "react";
import Desmos from 'desmos';

import MainTextComponent from "../components/MainTextComponent.jsx";

export default function Lab5() {

    const calculatorRef = useRef(null);
    const [calculator, setCalculator] = useState(null);
    const [points, setPoints] = useState([[1, 2], [2, 4]]);
    const [degree, setDegree] = useState(1);

    useEffect(() => {
        const calc = Desmos.GraphingCalculator(calculatorRef.current, {
            keypad: false,
        });

        setCalculator(calc);

        // Устанавливаем начальные точки
        calc.setExpression({
            type: 'table',
            columns: [
                {
                    latex: 'x',
                    values: points.map(point => point[0]),
                },
                {
                    latex: 'y',
                    values: points.map(point => point[1]),
                },
            ],
        });


        return () => calc.destroy();
    }, [points]);

    const addPoint = () => {
        const newPoints = [...points, [3 ** degree, 9 ** degree]];
        setPoints(newPoints);
        if (calculator) {
            calculator.setExpression({
                type: 'table',
                columns: [
                    {
                        latex: 'x',
                        values: newPoints.map(point => point[0]),
                    },
                    {
                        latex: 'y',
                        values: newPoints.map(point => point[1]),
                    },
                ],
            });
        }
        setDegree(degree + 1);
    };


    return (
        <>
            <MainTextComponent labName="Function interpolation">Lab #5</MainTextComponent>
            <div className="flex flex-col justify-center items-center">
                <div ref={calculatorRef} style={{width: '50%', height: '500px'}}></div>
                <button onClick={addPoint}>Add point</button>
            </div>

        </>
    );
}