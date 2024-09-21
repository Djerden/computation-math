import {useState} from "react";

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab5Components/Input.jsx";
import Solution from "../components/Lab5Components/Solution.jsx"
import GraphComponent from "../components/Lab5Components/GraphComponent.jsx";


export default function Lab5() {

    const [answer, setAnswer] = useState({
        result: "answer will be here",
        graphs: [],
        interpolation_nodes: []
    });

    function sendRequest(dataInput) {

        // Сначала очищаем текущее состояние графиков
        setAnswer({
            result: "answer will be here",
            graphs: [], // Очищаем графики
            interpolation_nodes: []
        });

        fetch('http://localhost:8000/lab5', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataInput) // сюда положить данные
        })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(errorData => {
                        throw new Error(errorData.details || 'Произошла ошибка');
                    });
                }
                return response.json()
            })
            .then(data => {
                console.log('Полученные данные:')
                console.log(data);

                // обработать результат
                setAnswer({result: data.result, graphs: data.graphs, interpolation_nodes: data.interpolation_nodes})
            })
            .catch(error => {
                console.error('Error:', error);
                alert(`Ошибка: ${error.message}`);
            });
    }

    function formGraphicComponents() {
        if (answer.graphs.length === 0) {
            return null;
        } else {
            return (
                <>
                    {answer.graphs.map((methodGraph, index) => {
                        // Проверяем, что внутри объекта метода есть свойства x и y, и они не пустые
                        if (methodGraph.x && methodGraph.y && methodGraph.x.length > 0 && methodGraph.y.length > 0) {
                            return (
                                <GraphComponent
                                    key={index}
                                    name={methodGraph.name}
                                    inter_point={methodGraph.inter_point}
                                    interpolation_nodes={answer.interpolation_nodes}
                                    x={methodGraph.x}
                                    y={methodGraph.y}
                                />
                            );
                        }
                        return null; // Не отрисовывать компонент, если x и y пустые
                    })}
                </>
            );
        }
    }

    return (
        <>
            <MainTextComponent labName="Function interpolation">Lab #5</MainTextComponent>
            <div className="flex flex-row gap-6 mx-6">
                {/*Right side*/}
                <Input requestFunction={sendRequest}/>
                {/*Left Side*/}
                <Solution answer={answer}/>
            </div>
            <div className="flex flex-col mx-6 gap-6 mt-6">
                {formGraphicComponents()}
                {/*<GraphComponent name="Метод Лагранжа" answer={answer}/>*/}
                {/*<GraphComponent name="Метод Ньютона с конечными разностями"/>*/}
                {/*<GraphComponent name="Метод Бесселя"/>*/}
            </div>
        </>
    );
}