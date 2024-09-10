import {useEffect, useRef} from "react";
import Desmos from 'desmos';



export default function GraphComponent({answer}) {

    // Поиск границ для фокусировки десмоса
    function findMinMax(pairs) {

        if (pairs && pairs.length > 0) {
            // Инициализируем минимальные и максимальные значения первыми элементами массива
            let minX = pairs[0][0];
            let maxX = pairs[0][0];
            let minY = pairs[0][1];
            let maxY = pairs[0][1];

            // Проходим по массиву и находим минимальные и максимальные значения
            pairs.forEach(pair => {
                const [x, y] = pair;

                if (x < minX) minX = x;
                if (x > maxX) maxX = x;

                if (y < minY) minY = y;
                if (y > maxY) maxY = y;
            });
            return { minX, maxX, minY, maxY };
        }
        // Если массив пустой, возвращаем границы по умолчанию
        return { minX: -10, maxX: 10, minY: -10, maxY: 10 };
    }
    const borders = findMinMax(answer.pairs);

    // преобразование точек для десмоса
    function formatPointsForDesmos(pairs) {
        // Проверяем, что массив существует и не пустой
        if (pairs && pairs.length > 0) {
            return pairs.map(pair => `(${pair[0]},${pair[1]})`).join(',');
        }
        return '';  // Возвращаем пустую строку, если массив пустой
    }
    const points = formatPointsForDesmos(answer.pairs);

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

            // Установка границ окна по x и y
            calculatorInstanceRef.current.setMathBounds({
                left: borders.minX - 1,  // x от -1
                right: borders.maxX + 1,  // x до 5
                bottom: borders.minY - 1,  // y от -3
                top: borders.maxY + 1  // y до 6
            });

            calculatorInstanceRef.current.setExpression({
                id: 'points',
                latex: points  // формат LaTeX для координат точек
            });

            // Проверка и отрисовка линейной функции
            if (Object.keys(answer.linear).length !== 0) {
                const linearFunction = answer.linear.approximating_function.split('=')[1].trim();
                calculatorInstanceRef.current.setExpression({ id: 'graph1', latex: linearFunction });
            }

            // Проверка и отрисовка квадратной функции
            if (Object.keys(answer.square).length !== 0) {
                const squareFunction = answer.square.approximating_function.split('=')[1].trim();
                calculatorInstanceRef.current.setExpression({ id: 'graph2', latex: squareFunction });
            }

            // Проверка и отрисовка кубической функции
            if (Object.keys(answer.cubic).length !== 0) {
                const cubicFunction = answer.cubic.approximating_function.split('=')[1].trim();
                calculatorInstanceRef.current.setExpression({ id: 'graph3', latex: cubicFunction });
            }

            // Проверка и отрисовка экспоненциальной функции
            if (Object.keys(answer.exp).length !== 0) {
                const expFunction = answer.exp.approximating_function.split('=')[1].trim();
                calculatorInstanceRef.current.setExpression({ id: 'graph4', latex: expFunction });
            }

            // Проверка и отрисовка логарифмической функции
            if (Object.keys(answer.logarithm).length !== 0) {
                const logarithmFunction = answer.logarithm.approximating_function.split('=')[1].trim();
                calculatorInstanceRef.current.setExpression({ id: 'graph5', latex: logarithmFunction });
            }

            // Проверка и отрисовка степенной функции
            if (Object.keys(answer.power).length !== 0) {
                const powerFunction = answer.power.approximating_function.split('=')[1].trim();
                calculatorInstanceRef.current.setExpression({ id: 'graph6', latex: powerFunction });
            }
        }
    }, [answer]);

    return (
        <div className="flex p-6 bg-custom-314455 rounded">
            <div ref={calculatorRef} style={{ width: '100%', height: '400px' }}></div>
        </div>
    );
}