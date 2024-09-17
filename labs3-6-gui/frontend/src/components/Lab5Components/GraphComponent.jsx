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
            // Очистить предыдущие выражения
            calculatorInstanceRef.current.setExpressions([]);

            // Проходим по каждому графику из answer.graphs
            answer.graphs.forEach((graph, index) => {
                // Проверяем, что массивы x и y не пустые
                if (graph.x.length > 0 && graph.y.length > 0) {
                    // Преобразуем данные x и y в строку списков для построения линии
                    const xValues = graph.x.join(',');
                    const yValues = graph.y.join(',');

                    // Устанавливаем выражение для линии на графике
                    calculatorInstanceRef.current.setExpression({
                        id: `graph${index + 1}`,
                        latex: `\\operatorname{polygon}\\left( [${xValues}], [${yValues}] \\right)`,
                        color: Desmos.Colors.BLUE,
                        lineStyle: Desmos.Styles.SOLID,
                        points: false  // Убираем точки, оставляем только линию
                    });
                }
            });
        }
    }, [answer]);

    return (
        <div className="flex flex-col p-6 bg-custom-314455 rounded">
            <h1 className="text-white">{name}</h1>
            <div ref={calculatorRef} style={{ width: '100%', height: '400px' }}></div>
        </div>
    );
}