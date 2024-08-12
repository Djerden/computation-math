export default function Input() {
    return (
        <div className="flex flex-col bg-white text-black p-6 gap-2 rounded">
            <h1 className="text-2xl font-bold">Pairs Factory</h1>
            <h2>Enter pair x and y (use space)</h2>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;1</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;2</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;3</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;4</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;5</label>
                <input className="w-2/3 bg-neutral-200 border border-black rounded px-2" type="text"
                       placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;6</label>
                <input className="w-2/3 bg-neutral-200 border border-black rounded px-2" type="text"
                       placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;7</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;8</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>&nbsp;&nbsp;9</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>10</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>11</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
            <p className="flex flex-row gap-1">
                <label>12</label>
                <input className="w-2/3" type="text" placeholder="x y"/>
            </p>
        </div>
    );
}