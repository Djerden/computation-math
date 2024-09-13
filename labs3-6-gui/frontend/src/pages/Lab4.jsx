import {useState} from "react";

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab4Components/Input.jsx";
import GraphComponent from "../components/Lab4Components/GraphComponent.jsx";
import Solution from "../components/Lab4Components/Solution.jsx";

export default function Lab4() {

    const [pairs, setPairs] = useState(Array(12).fill({x: null, y: null}));
    const [answer, setAnswer] = useState({
        pairs: [],
        functions: [],
        bestApprox: null
    });

    function sendRequest(filteredPairs) {
        console.log(filteredPairs)

        fetch('http://localhost:8000/lab4', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(filteredPairs)
        })
            .then(response => {

                if (!response.ok) {
                    return response.json().then(errorData => {
                        throw new Error(errorData.detail || 'Произошла ошибка');
                    });
                }
                return response.json()
            })
            .then(data => {
                console.log('Полученные данные:')
                console.log(data);

                setAnswer(data)
            })
            .catch(error => {
                console.error('Error:', error);
                alert(`Ошибка: ${error.message}`);
            });
    }
    return (
        <>
            <MainTextComponent labName="Function approximation">Lab #4</MainTextComponent>
            <div className="flex flex-col gap-6 mx-6">
                {/*Top*/}
                <div className="flex flex-row justify-center flex-wrap gap-6">

                    <Input pairs={pairs} setPairs={setPairs} sendRequest={sendRequest}/>

                    <div className="w-full md:w-auto flex-grow">
                        <Solution answer={answer}/>
                    </div>
                </div>

                {/*Bottom*/}
                <div>
                    <GraphComponent answer={answer}/>
                </div>
            </div>
        </>
    );
}