import {useState} from "react";

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab6Components/Input.jsx";
import Solution from "../components/Lab6Components/Solution.jsx";
import GraphComponent from "../components/Lab6Components/GraphComponent.jsx";


export default function Lab6() {

    const [answer, setAnswer] = useState({
        result: null,
        graphics: []
    });

    function sendRequest(inputs) {

        // Сначала очищаем текущее состояние графиков
        setAnswer({
            result: null,
            graphics: []
        });

        fetch('http://localhost:8000/lab6', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputs)
        }).then(response => {
            if (!response.ok) {
                return response.json().then(errorData => {
                    throw new Error(errorData.details || 'Произошла ошибка');
                });
            }
            return response.json()
        }).then(data => {
                console.log('Полученные данные:')
                console.log(data);

                // обработать результат
                setAnswer(() => ({
                    result: data.result,
                    graphics: data.graphics
                }));
            })
            .catch(error => {
                console.error('Error:', error);
                alert(`Ошибка: ${error.message}`);
            });

        console.log('Данные отправлены');
    }

    function formGraphicComponents() {
        if (answer.graphics.length === 0) {
            return null;
        } else {
            return (
                <>
                    {answer.graphics.map((methodGraph, index) => {
                        // Проверяем, что внутри объекта метода есть необходимые данные для построения графика
                        if (methodGraph.exact_x && methodGraph.exact_y && methodGraph.method_x && methodGraph.method_y) {
                            return (
                                <GraphComponent
                                    key={index}
                                    name={methodGraph.name}
                                    exactX={methodGraph.exact_x}
                                    exactY={methodGraph.exact_y}
                                    methodX={methodGraph.method_x}
                                    methodY={methodGraph.method_y}
                                />
                            );
                        }
                        return null; // Не отрисовывать компонент, если данные отсутствуют
                    })}
                </>
            );
        }
    }

    return (
        <>
            <MainTextComponent labName="Numerical solution of differential equations">Lab #6</MainTextComponent>
            <div className="flex flex-row gap-6 mx-6">
                <Input requestFunction={sendRequest}/>
                <Solution answer={answer}/>
            </div>
            <div className="flex flex-col mx-6 gap-6 mt-6">
                {/*<GraphComponent/>*/}
                {formGraphicComponents()}
            </div>
        </>
    );
}