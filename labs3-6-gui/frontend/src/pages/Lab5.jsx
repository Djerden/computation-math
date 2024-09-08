import {useRef, useEffect, useState} from "react";
import Desmos from 'desmos';

import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab5Components/Input.jsx";
import Solution from "../components/Lab5Components/Solution.jsx"
import GraphComponent from "../components/Lab5Components/GraphComponent.jsx";

export default function Lab5() {


    return (
        <>
            <MainTextComponent labName="Function interpolation">Lab #5</MainTextComponent>
            <div className="flex flex-row gap-6 mx-6">
                {/*Right side*/}
                <Input />
                {/*Left Side*/}
                <Solution />
            </div>
            <div className="flex flex-col mx-6 gap-6 mt-6">
                <GraphComponent name="Метод Лагранжа"/>
                <GraphComponent name="Метод Ньютона с конечными разностями"/>
                <GraphComponent name="Метод Бесселя"/>
            </div>
        </>
    );
}