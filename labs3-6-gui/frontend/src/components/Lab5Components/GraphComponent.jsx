import {useEffect, useRef} from "react";
import Desmos from 'desmos';



export default function GraphComponent({name, inter_point, interpolation_nodes, x, y}) {

    const calculatorRef = useRef(null);
    const calculatorInstanceRef = useRef(null);

    // Функция для вычисления минимальных и максимальных значений x и y
    const calculateBounds = (xNodes, yNodes) => {
        const minX = Math.min(...xNodes);
        const maxX = Math.max(...xNodes);
        const minY = Math.min(...yNodes);
        const maxY = Math.max(...yNodes);
        return { minX, maxX, minY, maxY };
    };

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


            // Сортировка x и соответствующая перестановка y
            const combined = x.map((value, index) => ({ xValue: value, yValue: y[index] }));

            // Сортируем по значениям x
            combined.sort((a, b) => a.xValue - b.xValue);

            // Получаем отсортированные массивы x и y
            const sortedX = combined.map(item => item.xValue);
            const sortedY = combined.map(item => item.yValue);

            // Далее используйте отсортированные x и y
            const xValues = sortedX.join(', ');
            const yValues = sortedY.join(', ');

            console.log(xValues)
            console.log(yValues)

            // Устанавливаем выражение для построения линии по точкам
            calculatorInstanceRef.current.setExpression({
                id: 'graph_line',
                latex: `y = ([${xValues}], [${yValues}])`,
                color: Desmos.Colors.GREEN,  // Цвет линии
                points: false,  // Убираем отображение точек
                lines: true
            });

            // Отрисовка точек из interpolation_nodes
            if (interpolation_nodes && interpolation_nodes.length === 2) {
                const [xNodes, yNodes] = interpolation_nodes;
                if (xNodes.length > 0 && yNodes.length > 0 && xNodes.length === yNodes.length) {
                    const points = xNodes.map((xVal, idx) => `(${xVal}, ${yNodes[idx]})`).join(', ');
                    calculatorInstanceRef.current.setExpression({
                        id: 'interpolation_points',
                        latex: `\\left[ ${points} \\right]`,
                        color: Desmos.Colors.BLUE,  // Цвет точек — синий
                        pointStyle: Desmos.Styles.POINT,  // Стиль точек
                        pointSize: 5  // Размер точек
                    });

                    // Вычисляем границы графика на основе точек из interpolation_nodes
                    const borders = calculateBounds(xNodes, yNodes);

                    // Установка границ окна по x и y
                    calculatorInstanceRef.current.setMathBounds({
                        left: borders.minX - 1,  // x от (минимум - 1)
                        right: borders.maxX + 1,  // x до (максимум + 1)
                        bottom: borders.minY - 1,  // y от (минимум - 1)
                        top: borders.maxY + 1  // y до (максимум + 1)
                    });
                }
            }

            // Отрисовка точки из inter_point
            if (inter_point && inter_point.length === 2) {
                const [xPoint, yPoint] = inter_point;
                calculatorInstanceRef.current.setExpression({
                    id: 'single_point',
                    latex: `(${xPoint}, ${yPoint})`,
                    color: Desmos.Colors.RED,  // Цвет точки — красный
                    pointStyle: Desmos.Styles.POINT,  // Стиль точки
                    pointSize: 5  // Размер точки
                });
            }

        }
    }, []);

    return (
        <div className="flex flex-col p-6 bg-custom-314455 rounded">
            <h1 className="text-white">{name}</h1>
            <div ref={calculatorRef} style={{ width: '100%', height: '400px' }}></div>
        </div>
    );
}