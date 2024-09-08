export default function Solution({answer}) {

    const linear = `Линейная:\n${JSON.stringify(answer.linear)}`;
    const square = `Квадратичная:\n${JSON.stringify(answer.square)}`;
    const cubic = `Кубическая:\n${JSON.stringify(answer.cubic)}`;
    const exp = `Экспоненциальная:\n${JSON.stringify(answer.exp)}`;
    const logarithm = `Логарифмическая:\n${JSON.stringify(answer.logarithm)}`;
    const power = `Степенная:\n${JSON.stringify(answer.power)}`;

    const text = linear + '\n' + square + '\n' + cubic + '\n' + exp + '\n' + logarithm + '\n' + power;

    function saveAnswerAsFile(fileName) {

        const blob = new Blob([answer], {type: 'text/plain'});

        // создаем ссылку на скачивание
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = fileName;

        // Программно нажимаем на ссылку, чтобы инициировать скачивание
        link.click();

        // Освобождаем URL
        URL.revokeObjectURL(link.href)
    }

    return (
        <div className="flex flex-col bg-custom-314455 text-white p-6 gap-2 rounded h-full">
            <h1 className="text-2xl">Solution</h1>
            <textarea
                className="px-2 py-1 resize-none h-full rounded w-full text-black"
                readOnly
                value={text}>
            </textarea>
            <button
                className="bg-white text-black px-4 py-2 rounded hover:bg-neutral-300"
                onClick={() => {saveAnswerAsFile()}}
            >
                Save to
            </button>
        </div>
    );
}