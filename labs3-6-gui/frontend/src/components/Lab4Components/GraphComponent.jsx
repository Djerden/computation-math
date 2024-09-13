import {useEffect, useRef} from "react";
import Desmos from 'desmos';



export default function GraphComponent({answer}) {

    const calculatorRef = useRef(null);
    const calculatorInstanceRef = useRef(null);
    const expressionIds = useRef([]);


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

    // преобразование точек для десмоса
    function formatPointsForDesmos(pairs) {
        // Проверяем, что массив существует и не пустой
        if (pairs && pairs.length > 0) {
            return pairs.map(pair => `(${pair[0]},${pair[1]})`).join(',');
        }
        return '';  // Возвращаем пустую строку, если массив пустой
    }

    // преобразование аппроксимирующих функций
    function getApproximationFunctions() {
        let result = [];
        if (answer.functions.length > 0) {
            const array = answer.functions;
            array.forEach((approximation) => {
                const element = [];

                // Проверяем оба условия
                if (!approximation.name || !approximation.function) {
                    return;  // Пропускаем итерацию, если хотя бы одно из условий не выполнено
                }

                // Если оба условия выполнены, добавляем элементы
                element.push(approximation.name);
                element.push(approximation.function);

                // добавляем в итоговый ответ
                result.push(element);
            })
        }
        return result;
    }

    // Параметры для графика
    const functions = getApproximationFunctions();
    const borders = findMinMax(answer.pairs);
    const points = formatPointsForDesmos(answer.pairs);

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

            // Проверяем, что массив не пуст
            if (functions.length > 0) {
                functions.forEach((expression, index) => {
                    const [label, latex] = expression; // Извлекаем label и latex
                    const id = `graph${index + 1}`;
                    calculatorInstanceRef.current.setExpression({
                        id: id,    // Уникальный id для каждого графика
                        latex: latex,               // Математическое выражение
                        showLabel: true,            // Отображать лейбл
                        label: label,             // Лейбл для графика
                        labelSize: 'medium',        // Размер лейбла
                        labelOrientation: 'above'   // Ориентация лейбла
                    });

                    // Сохраняем ID выражения
                    expressionIds.current.push(id);
                });
            }
        }
    }, [answer]);

    return (
        <div className="flex p-6 bg-custom-314455 rounded">
            <div ref={calculatorRef} style={{ width: '100%', height: '400px' }}></div>
        </div>
    );
}