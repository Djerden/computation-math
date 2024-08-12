import {useEffect, useRef} from "react";
import Desmos from 'desmos';



export default function GraphComponent() {

    const calculatorRef = useRef(null);

    useEffect(() => {
        const calculator = Desmos.GraphingCalculator(calculatorRef.current, {
            keypad: false,  // Убирает виртуальную клавиатуру, если это необходимо
        });

        // Пример добавления уравнения
        calculator.setExpression({ id: 'graph1', latex: 'y=x^2' });

        // Очистка после размонтирования компонента
        return () => calculator.destroy();
    }, []);


    return (
        <div className="flex p-6 bg-custom-314455 rounded">
            <div ref={calculatorRef} style={{ width: '100%', height: '400px' }}></div>
        </div>
    );
}