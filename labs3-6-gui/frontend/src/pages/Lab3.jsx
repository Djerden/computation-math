import {useState} from "react";

import ChoiceFactory from "../components/Lab3Components/ChoiceFactory.jsx";
import MainTextComponent from "../components/MainTextComponent.jsx";
import Input from "../components/Lab3Components/Input.jsx";
import Solution from "../components/Lab3Components/Solution.jsx";
import BenderGif from "../components/Lab3Components/BenderGif.jsx";

export default function Lab3() {

    const [choice, setChoice] = useState({
        equation: null,
        method: null
    }); // ['x^2', 'sin(x)', '1/x'
    const [inputData, setInputData] = useState({
        a: 0,
        b: 0,
        eps: 0,
        n: 0
    });
    const [answer, setAnswer] = useState('Answer will be here');
    const [isBender, setIsBender] = useState(false); // [true, false

    function handleChangeChoice(param, value) {
        setChoice({...choice, [param]: value});
    }

    function handleChangeInputData(param, value) {
        setInputData({...inputData, [param]: value});
    }

    function validateInput() {

        // сделать прроверку данных
        return true;
    }


    // Запрос на сервер
    function solveClick() {
        console.log(choice);
        console.log(inputData);
        if (!validateInput()) {
            console.log('Данные неполны или некорректны');
            return;
        }
        fetch('http://localhost:8000/lab3', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                choice: choice,
                inputData: inputData
            })
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setAnswer(data.answer);

            })
            .catch(error => {
                console.error('Error:', error)
            });
        if (!isBender) setIsBender(true);
    }

    return (
        <>
            <MainTextComponent labName="Numerical integration">Lab #3</MainTextComponent>
            <div className="flex flex-row flex-wrap gap-6 justify-start mx-6">
                {/* Left side */}
                <div className="flex flex-col gap-6 md:w-1/3 w-full">
                    {/*Choice Factory*/}
                    <ChoiceFactory onChangeChoice={handleChangeChoice}/>

                    {/*Inputs*/}
                    <Input
                        onChange={handleChangeInputData} solveClick={solveClick}/>
                </div>

                {/* Right side */}
                <Solution answer={answer}/>
                {isBender ? <BenderGif /> : null}
            </div>
        </>
    );
}