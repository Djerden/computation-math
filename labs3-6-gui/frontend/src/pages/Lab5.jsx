import {useState} from "react";

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab5Components/Input.jsx";
import Solution from "../components/Lab5Components/Solution.jsx"
import GraphComponent from "../components/Lab5Components/GraphComponent.jsx";


export default function Lab5() {

    const [answer, setAnswer] = useState({
        result: "answer will be here",
        graphs: []
    });

    function sendRequest(dataInput) {

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
                setAnswer({result: data.result, graphs: data.graphs})
            })
            .catch(error => {
                console.error('Error:', error);
                alert(`Ошибка: ${error.message}`);
            });
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
                <GraphComponent name="Метод Лагранжа" answer={answer}/>
                {/*<GraphComponent name="Метод Ньютона с конечными разностями"/>*/}
                {/*<GraphComponent name="Метод Бесселя"/>*/}
            </div>
        </>
    );
}