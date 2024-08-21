import Tip from "../Tip";

export default function Input({tips, onChange, solveClick}) {

    // Сделать валидацию полей


    return (
        <div className="flex flex-col bg-custom-644e5b rounded p-6 gap-2 text-white">

            <h2>Enter the range, inaccuracy and value of partition number of interval</h2>

            <div className="flex flex-col space-y-2 text-black">
                <div className="flex flex-col">
                    <input
                        className="px-2 py-1 rounded"
                        type="number"
                        placeholder="enter a"
                        onChange={(event) => onChange('a', event.target.value)}/>
                    {tips.a ? <Tip>a должно быть числом</Tip> : null}
                </div>
                <div className="flex flex-col">
                    <input
                        className="px-2 py-1 rounded"
                        type="number"
                        placeholder="enter b"
                        onChange={(event) => onChange('b', event.target.value)}/>
                    {tips.b ? <Tip>b должно быть числом</Tip> : null}
                </div>
                <div className="flex flex-col">
                    <input
                        className="px-2 py-1 rounded "
                        type="number"
                        placeholder="enter eps"
                        min="0"
                        max="1"
                        step="0.1"
                        onChange={(event) => onChange('eps', event.target.value)}/>
                    {tips.eps ? <Tip>eps должно быть числом в диапазоне от 0 до 1 включительно</Tip> : null}
                </div>
                <div className="flex flex-col">
                    <input
                        className="px-2 py-1 rounded"
                        type="number"
                        placeholder="enter n"
                        min="0"
                        onChange={(event) => onChange('n', event.target.value)}/>
                    {tips.n ? <Tip>n должно быть положительным числом</Tip> : null}
                </div>
            </div>
            <div className="flex flex-row justify-between items-center mt-6">
                <input
                    type="file"
                    accept=".txt"/>
                <button className="bg-black text-white px-6 w-full rounded hover:bg-neutral-700"
                        onClick={solveClick}>
                    Solve
                </button>
            </div>
        </div>
    );
}