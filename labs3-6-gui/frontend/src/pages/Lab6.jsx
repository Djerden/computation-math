import {useState} from "react";

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab6Components/Input.jsx";
import Solution from "../components/Lab6Components/Solution.jsx";


export default function Lab6() {

    const [answer, setAnswer] = useState({
        result: 'answer will be here'
    });

    function sendRequest(inputs) {

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
                setAnswer(() => ({result: data}));
            })
            .catch(error => {
                console.error('Error:', error);
                alert(`Ошибка: ${error.message}`);
            });

        console.log('Данные отправлены');
    }

    return (
        <>
            <MainTextComponent labName="Numerical solution of differential equations">Lab #6</MainTextComponent>
            <div className="flex flex-row gap-6 mx-6">
                <Input requestFunction={sendRequest}/>
                <Solution answer={answer}/>
            </div>
            <div>

            </div>
        </>
    );
}