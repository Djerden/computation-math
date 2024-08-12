export default function MainTextComponent({children, labName}) {
    return (
        <div className="flex flex-col items-start px-6 mb-4">
            <h1 className="text-white font-bold text-6xl">{children}</h1>
            {labName && <h2 className="text-2xl text-white">{labName}</h2>}
        </div>
    );
}