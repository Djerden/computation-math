import {useEffect, useRef} from "react";
import Desmos from 'desmos';



export default function GraphComponent({answer}) {

    // преобразование точек для десмоса

    // преобразование функций для десмоса



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

            calculatorInstanceRef.current.setExpression({
                id: 'points',
                latex: '({1},{2}),({2},{4}),({3},{6}),({4},{8})'  // формат LaTeX для координат точек
            });

            if (Object.keys(answer.linear).length !== 0) {
                calculatorInstanceRef.current.setExpression({ id: 'graph1', latex: answer.linear.approximating_function});
                calculatorInstanceRef.current.setExpression({ id: 'graph2', latex: answer.square.approximating_function});
                calculatorInstanceRef.current.setExpression({ id: 'graph3', latex: answer.cubic.approximating_function});
                calculatorInstanceRef.current.setExpression({ id: 'graph4', latex: answer.exp.approximating_function});
                calculatorInstanceRef.current.setExpression({ id: 'graph5', latex: answer.logarithm.approximating_function});
                calculatorInstanceRef.current.setExpression({ id: 'graph6', latex: answer.power.approximating_function});
            }
        }
    }, [answer]);

    return (
        <div className="flex p-6 bg-custom-314455 rounded">
            <div ref={calculatorRef} style={{ width: '100%', height: '400px' }}></div>
        </div>
    );
}