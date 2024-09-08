import MainTextComponent from "../components/common/MainTextComponent.jsx";
import Input from "../components/Lab6Components/Input.jsx";
import Solution from "../components/Lab6Components/Solution.jsx";

export default function Lab6() {
    return (
        <>
            <MainTextComponent labName="Numerical solution of differential equations">Lab #6</MainTextComponent>
            <div className="flex flex-row gap-6 mx-6">
                <Input/>
                <Solution/>
            </div>
            <div>

            </div>
        </>
    );
}