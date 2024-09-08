import {useState} from "react";

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab4Components/Input.jsx";
import GraphComponent from "../components/Lab4Components/GraphComponent.jsx";
import Solution from "../components/Lab4Components/Solution.jsx";

export default function Lab4() {

    const [pairs, setPairs] = useState(Array(12).fill({x: null, y: null}));
    const [answer, setAnswer] = useState({
        linear: {},
        square: {},
        cubic: {},
        exp: {},
        logarithm: {},
        power: {}
    });

    function sendRequest() {
        console.log(pairs)
            // const filteredPairs = pairs.filter(pair => pair.x !== null && pair.y !== null);

        fetch('http://localhost:8000/lab4', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // body: JSON.stringify(filteredPairs)
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setAnswer({
                    linear: data.linear,
                    square: data.square,
                    cubic: data.cubic,
                    exp: data.exp,
                    logarithm: data.logarithm,
                    power: data.power
                });

            })
            .catch(error => {
                console.error('Error:', error)
            });
    }

    return (
        <>
            <MainTextComponent labName="Function approximation">Lab #4</MainTextComponent>
            <div className="flex flex-row flex-wrap gap-6 justify-start mx-6">

                {/*LeftSide: Input, Choose file and button Solve*/}
                <Input pairs={pairs} setPairs={setPairs} sendRequest={sendRequest}/>

                {/*RightSide*/}
                <div className="flex flex-col gap-6 rounded flex-grow">

                    {/*График*/}
                    <GraphComponent answer={answer}/>

                    {/*Решение*/}
                    <Solution answer={answer}/>
                </div>
            </div>
        </>
    );
}