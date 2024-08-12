export default function Input({answer}) {

    return (
        <div className="flex flex-col bg-custom-314455 rounded p-6 gap-2 md:w-1/3 w-full ">
            <h1 className="text-2xl font-bold text-white">Solution</h1>
            <textarea
                className="px-2 py-1 resize-none h-full rounded w-full"
                readOnly
                value={answer}>
            </textarea>
            <button className="bg-white text-black px-4 py-2 rounded hover:bg-neutral-300">Save to</button>
        </div>
    );
}