import {useEffect, useRef} from "react";
import Desmos from 'desmos';

export default function GraphComponent({name, exactX, exactY, methodX, methodY}) {

    const calculatorRef = useRef(null);
    const calculatorInstanceRef = useRef(null);
    const expressionIds = useRef([]);

    // Функция для вычисления минимумов и максимумов
    function calculateBounds(xData, yData) {
        const minX = Math.min(...xData);
        const maxX = Math.max(...xData);
        const minY = Math.min(...yData);
        const maxY = Math.max(...yData);

        return { minX, maxX, minY, maxY };
    }

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

            // Удаляем предыдущие выражения
            expressionIds.current.forEach(id => {
                calculatorInstanceRef.current.removeExpression({ id });
            });
            expressionIds.current = []; // Очищаем список ID

            // Рассчитываем границы для методичных данных
            const methodBounds = calculateBounds(methodX, methodY);
            const exactBounds = calculateBounds(exactX, exactY);

            // Определяем общие минимумы и максимумы для обеих серий данных
            const borders = {
                minX: Math.min(methodBounds.minX, exactBounds.minX),
                maxX: Math.max(methodBounds.maxX, exactBounds.maxX),
                minY: Math.min(methodBounds.minY, exactBounds.minY),
                maxY: Math.max(methodBounds.maxY, exactBounds.maxY)
            };

            // Установка границ окна по x и y
            calculatorInstanceRef.current.setMathBounds({
                left: borders.minX,    // x от (минимум)
                right: borders.maxX,   // x до (максимум)
                bottom: borders.minY,  // y от (минимум)
                top: borders.maxY      // y до (максимум)
            });

            // Далее используйте отсортированные x и y
            const xValues = methodX.join(', ');
            const yValues = methodY.join(', ');

            // Устанавливаем выражение для построения линии по точкам
            calculatorInstanceRef.current.setExpression({
                id: 'method',
                latex: `y = ([${xValues}], [${yValues}])`,
                color: Desmos.Colors.RED,  // Цвет линии
                points: false,  // Убираем отображение точек
                lines: true
            });

            const xExact = exactX.join(', ');
            const yExact = exactY.join(', ');

            // Устанавливаем выражение для построения линии по точкам
            calculatorInstanceRef.current.setExpression({
                id: 'exact sol',
                latex: `y = ([${xExact}], [${yExact}])`,
                color: Desmos.Colors.BLUE,  // Цвет линии
                points: false,  // Убираем отображение точек
                lines: true
            });

        }
    }, []);

    return (
        <div className="flex flex-col p-6 bg-custom-314455 rounded">
            <h1 className="text-white">{name}</h1>
            <div ref={calculatorRef} style={{width: '100%', height: '400px'}}></div>
        </div>
    );
}