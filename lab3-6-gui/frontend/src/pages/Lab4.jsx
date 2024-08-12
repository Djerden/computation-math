import {useRef, useEffect} from "react";

import MainTextComponent from "../components/MainTextComponent.jsx";
import Input from "../components/Lab4Components/Input.jsx";
import FileInputAndSolve from "../components/Lab4Components/FileInputAndSolve.jsx";
import GraphComponent from "../components/Lab4Components/GraphComponent.jsx";
import Solution from "../components/Lab4Components/Solution.jsx";

export default function Lab4() {

    return (
        <>
            <MainTextComponent labName="Function approximation">Lab #4</MainTextComponent>
            <div className="flex flex-row flex-wrap gap-6 justify-start mx-6">

                {/*LeftSide*/}
                <div className="flex flex-col gap-6">
                    {/*Input*/}
                    <Input />
                    {/*FileInput and Solve*/}
                    <FileInputAndSolve />
                </div>

                {/*RightSide*/}
                <div className="flex flex-col gap-6 rounded w-1/2">
                    {/*График*/}
                    <GraphComponent />

                    {/*Решение*/}
                    <Solution />
                </div>
            </div>
        </>
    );
}