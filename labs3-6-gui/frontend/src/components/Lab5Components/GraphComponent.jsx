import {useEffect, useRef} from "react";
import Desmos from 'desmos';



export default function GraphComponent({name, answer}) {

    const calculatorRef = useRef(null);
    const calculatorInstanceRef = useRef(null);

    useEffect(() => {
        calculatorInstanceRef.current = Desmos.GraphingCalculator(calculatorRef.current, {
            keypad: false,  // Убирает виртуальную клавиатуру, если это необходимо
            settingsMenu: false,
            zoomButtons: false,
            expressionsCollapsed: true
        });

        // Очистка после размонтирования компонента,
        // когда компонент перестает отображаться на экране,
        // например, при переходе на другой экран или закрытии окна.
        return () => {
            if (calculatorInstanceRef.current) {
                calculatorInstanceRef.current.destroy();
            }
        };
    }, []);

    // блок для обновления функций, чтобы не пересоздавать обьект калькулятора
    useEffect(() => {
        if (calculatorInstanceRef.current) {
            calculatorInstanceRef.current.setExpression({ id: 'graph1', latex: 'y=x^2' });
            // тут расписать для ответ калькулятора
            //
            //
            //
            //
            calculatorInstanceRef.current.setExpression
        }
    }, [answer]);

    return (
        <div className="flex flex-col p-6 bg-custom-314455 rounded">
            <h1 className="text-white">{name}</h1>
            <div ref={calculatorRef} style={{ width: '100%', height: '400px' }}></div>
        </div>
    );
}