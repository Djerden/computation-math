export default function Solution({answer}) {
    return (
        <div className="flex flex-col bg-custom-314455 text-white p-6 gap-2 rounded">
            <h1 className="text-2xl">Solution</h1>
            <textarea
                className="px-2 py-1 resize-none h-full rounded w-full"
                readOnly
                value={answer}>
            </textarea>
            <button className="bg-white text-black px-4 py-2 rounded hover:bg-neutral-300">Save to</button>
        </div>
    );
}