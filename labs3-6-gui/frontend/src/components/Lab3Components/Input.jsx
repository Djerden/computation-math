import Tip from "../common/Tip.jsx";

export default function Input({data, tips, onChange, solveClick}) {

    // Сделать валидацию полей
    function handleFileChange(event) {
        const file = event.target.files[0];
        const reader = new FileReader();

        reader.onload = function (e) {
            const text = e.target.result;
            const lines = text.split('\n');
            lines.forEach(line => {
               const [key, value] = line.trim().split(/\s+/);
                if (['a', 'b', 'eps', 'n'].includes(key)) {
                    onChange(key, value);
                }
            });
        }
        reader.readAsText(file);
    }


    return (
        <div className="flex flex-col bg-custom-644e5b rounded p-6 gap-2 text-white">

            <h2>Enter the range, inaccuracy and value of partition number of interval</h2>

            <div className="flex flex-col space-y-2 text-black">
                <div className="flex flex-col">
                    <input
                        className="px-2 py-1 rounded"
                        type="number"
                        placeholder="enter a"
                        value={isNaN(data.a) ? '' : (data.a ?? '')}
                        onChange={(event) => onChange('a', event.target.value)}/>
                    {tips.a ? <Tip>a должно быть числом</Tip> : null}
                </div>
                <div className="flex flex-col">
                    <input
                        className="px-2 py-1 rounded"
                        type="number"
                        placeholder="enter b"
                        value={isNaN(data.b) ? '' : (data.b ?? '')}
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
                        value={isNaN(data.eps) ? '' : (data.eps ?? '')}
                        onChange={(event) => onChange('eps', event.target.value)}/>
                    {tips.eps ? <Tip>eps должно быть числом в диапазоне от 0 до 1 включительно</Tip> : null}
                </div>
                <div className="flex flex-col">
                    <input
                        className="px-2 py-1 rounded"
                        type="number"
                        placeholder="enter n"
                        min="0"
                        value={isNaN(data.n) ? '' : (data.n ?? '')}
                        onChange={(event) => onChange('n', event.target.value)}/>
                    {tips.n ? <Tip>n должно быть положительным целым числом, не меньше 4</Tip> : null}
                </div>
            </div>
            <div className="flex flex-row justify-between items-center mt-6">
                <input
                    type="file"
                    accept=".txt"
                    onChange={handleFileChange}/>

                <button className="bg-black text-white px-6 w-full rounded hover:bg-neutral-700"
                        onClick={solveClick}>
                    Solve
                </button>
            </div>
        </div>
    );
}