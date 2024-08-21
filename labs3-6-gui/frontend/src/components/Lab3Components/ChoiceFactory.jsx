import {useState} from "react";

export default function ChoiceFactory({onChangeChoice}) {
    // state vars
    const [isLeftPage, setIsLeftPage] = useState(true);

    // interface vars
    const leftPage = (
        <>
            <p className="space-x-2">
                <input type="radio" name="equation" value="x^2" defaultChecked onChange={handleChangeEquation}/>
                <label>x^2</label>
            </p>
            <p className="space-x-2">
                <input type="radio" name="equation" value="sin(x)" onChange={handleChangeEquation}/>
                <label>sin(x)</label>
            </p>
            <p className="space-x-2">
                <input type="radio" name="equation" value="1/x" onChange={handleChangeEquation}/>
                <label>1/x</label>
            </p>
        </>
    );

    const rightPage = (
        <>
            <p className="space-x-2">
                <input type="radio" name="method" value="rectangle-left" defaultChecked onChange={handleChangeMethod}/>
                <label>Rectangle (left)</label>
            </p>
            <p className="space-x-2">
                <input type="radio" name="method" value="rectangle-right" onChange={handleChangeMethod}/>
                <label>Rectangle (Right)</label>
            </p>
            <p className="space-x-2">
                <input type="radio" name="method" value="rectangle-middle" onChange={handleChangeMethod}/>
                <label>Rectangle (middle)</label>
            </p>
            <p className="space-x-2">
                <input type="radio" name="method" value="trapezoidal" onChange={handleChangeMethod}/>
                <label>Trapezoidal</label>
            </p>
            <p className="space-x-2">
                <input type="radio" name="method" value="simpson" onChange={handleChangeMethod}/>
                <label>Simpson</label>
            </p>
        </>
    );

    function handleChangeEquation(event) {
        onChangeChoice('equation', event.target.value);
    }

    function handleChangeMethod(event) {
        onChangeChoice('method', event.target.value);
    }

    function changePage() {
        if (isLeftPage) {
            setIsLeftPage(false);
        } else {
            setIsLeftPage(true);
        }
    }


    return (
        <div className="flex flex-col bg-white rounded p-6 gap-2">
            <h1 className="text-2xl font-bold">Choice Factory</h1>
            <h2>{isLeftPage ? 'Choose the equation:' : 'Choose the method:'}</h2>

            {isLeftPage ? leftPage : rightPage}

            <button className="bg-black text-white px-6 rounded hover:bg-neutral-700"
                    onClick={changePage}>
                {isLeftPage ? 'Next' : 'Back'}
            </button>
        </div>
    );
}