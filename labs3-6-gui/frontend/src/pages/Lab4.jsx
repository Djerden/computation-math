import {useState} from "react";

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab4Components/Input.jsx";
import GraphComponent from "../components/Lab4Components/GraphComponent.jsx";
import Solution from "../components/Lab4Components/Solution.jsx";

export default function Lab4() {

    const [pairs, setPairs] = useState(Array(12).fill({x: null, y: null}));
    const [answer, setAnswer] = useState({
        pairs: [],
        linear: {},
        square: {},
        cubic: {},
        exp: {},
        logarithm: {},
        power: {}
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
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setAnswer({
                    pairs: data.pairs,
                    linear: data.linear,
                    square: data.square,
                    cubic: data.cubic,
                    exp: data.exp,
                    logarithm: data.logarithm,
                    power: data.power
                });

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