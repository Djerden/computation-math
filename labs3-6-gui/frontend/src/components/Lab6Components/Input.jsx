export default function Input() {
    return (
        <div className="flex flex-col">
            <div className="flex flex-col bg-white rounded p-6 gap-4">
                <div className="flex flex-col gap-1">
                    <h1 className="text-2xl font-bold">Input</h1>
                    <h2>Enter the initial condition:</h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="y0"
                        value=""
                        onChange={() => {
                        }}
                    />
                    <h2>Enter the differentiation interval:</h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="x0"
                        value=""
                        onChange={() => {
                        }}
                    />
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="xn"
                        value=""
                        onChange={() => {
                        }}
                    />
                    <h2>Enter the step value:</h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="h"
                        value=""
                        onChange={() => {
                        }}
                    />
                    <h2>Enter the accuracy:</h2>
                    <input
                        className={`border border-black rounded px-2 py-1`}
                        type="text"
                        placeholder="eps"
                        value=""
                        onChange={() => {
                        }}
                    />
                </div>
                <div>
                    <h2>Select a function</h2>
                    <p className="space-x-2">
                        <input type="radio" name="equation" value="y' = x^2 - 2y" defaultChecked onChange={() => {}}/>
                        <label>y' = x^2 - 2y</label>
                    </p>
                    <p className="space-x-2">
                    <input type="radio" name="equation" value="y' = y + (1+x) * y^2" onChange={() => {}}/>
                        <label>y' = y + (1+x) * y^2</label>
                    </p>
                    <p className="space-x-2">
                        <input type="radio" name="equation" value="y' = 2x - 3y" onChange={() => {}}/>
                        <label>y' = 2x - 3y</label>
                    </p>
                </div>
            </div>
            <div>
                <div className="flex flex-row items-center bg-custom-644e5b p-6 text-white rounded-b">
                    <button
                        className="bg-black px-6 w-full rounded hover:bg-neutral-700"
                        onClick={() => {
                        }}
                    >Solve
                    </button>
                </div>
            </div>
        </div>
    );
}