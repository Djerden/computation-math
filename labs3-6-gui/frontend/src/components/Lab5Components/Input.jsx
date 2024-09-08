import {useState} from "react";

export default function Input() {

    const [inputMethod, setInputMethod] = useState("hand");

    const handPage = (
        <div>
            <h2>Enter the X coordinates separated by a space</h2>
            <input className="border border-black rounded px-2 py-1" type="number" step="1"/>
            <h2>Enter the Y coordinates separated by a space</h2>
            <input className="border border-black rounded px-2 py-1" type="number" step="1"/>
        </div>
    )

    const functionPage = (
        <div>
            <h2>Select a function</h2>
            <p className="space-x-2">
                <input
                    type="radio"
                    name="function"
                    value=""
                    defaultChecked
                    onChange={() => {
                    }}/>
                <label>func 1</label>
            </p>
            <p className="space-x-2">
                <input
                    type="radio"
                    name="function"
                    value=""
                    onChange={() => {
                    }}/>
                <label>func 2</label>
            </p>
            <p className="space-x-2">
                <input
                    type="radio"
                    name="function"
                    value=""
                    onChange={() => {
                    }}/>
                <label>func 3</label>
            </p>
            <h2>Enter the beginning of the interval</h2>
            <input className="border border-black rounded px-2 py-1" type="number" step="1"/>
            <h2>Enter the end of the interval</h2>
            <input className="border border-black rounded px-2 py-1" type="number" step="1"/>
            <h2>Enter the number of points</h2>
            <input className="border border-black rounded px-2 py-1" type="number" step="1"/>
        </div>
    );

    const filePage = (
        <div>
            <input type="file"
                   accept=".txt"
                   onChange={() => {
                   }}
            />
        </div>
    );

    function changeInputMethod(event) {
        setInputMethod(() => (event.target.value))
    }

    function renderInputMethod() {
        switch (inputMethod) {
            case 'hand':
                return handPage;
            case 'function':
                return functionPage;
            case 'file':
                return filePage;
            default:
                return null;
        }
    }

    return (
        <div>
            {/* Right side */}
            <div className="flex flex-col bg-white rounded p-6 gap-4">
                <div className="gap-2">
                    <h2>Select the data entry method:</h2>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="input-choice"
                            value="hand" // hand page
                            defaultChecked
                            onChange={changeInputMethod}/>
                        <label>Entering points</label>
                    </p>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="input-choice"
                            value="function" // function page
                            onChange={changeInputMethod}/>
                        <label>By function</label>
                    </p>
                    <p className="space-x-2">
                        <input
                            type="radio"
                            name="input-choice"
                            value="file" // file page
                            onChange={changeInputMethod}/>
                        <label>From file</label>
                    </p>
                </div>
                <div className="">
                    {renderInputMethod()}
                </div>
                <div className="gap-2">
                    <h2>Enter the value of the interpolation point:</h2>
                    <input className="border border-black rounded px-2 py-1" type="number" step="1"/>
                </div>
            </div>
            <div className="flex flex-row items-center bg-custom-644e5b p-6 text-white rounded-b">
                <button
                    className="bg-black px-6 w-full rounded hover:bg-neutral-700"
                    onClick={() => {}}
                >Solve
                </button>
            </div>

        </div>
    );
}