export default function Input({choice, data, answer}) {

    const text = `S = ${answer.square}\nparts = ${answer.parts}\ninaccuracy = ${answer.inaccuracy}`

    function saveAnswerAsFile(fileName) {
        if (answer.square == null) {
            return;
        }

        let userChoice = `User choice:\nequation: ${choice.equation}\nmethod: ${choice.method}\n`
        let userInput = `User input:\na = ${data.a}\nb = ${data.b}\neps = ${data.eps}\nn = ${data.n}\n`
        let userAnswer = 'Answer:\n' + text

        const blob = new Blob([userChoice, '\n', userInput, '\n', userAnswer], {type: 'text/plain'});

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
        <div className="flex flex-col bg-custom-314455 rounded p-6 gap-2 md:w-1/3 w-full ">
            <h1 className="text-2xl font-bold text-white">Solution</h1>
            <textarea
                className="px-2 py-1 resize-none h-full rounded w-full"
                readOnly
                value={answer.square ? text : 'Answer will be here'}>
            </textarea>
                <button
                    onClick={() => {saveAnswerAsFile('lab3_results.txt')}}
                    className="bg-white text-black px-4 py-2 rounded hover:bg-neutral-300">
                    Save to
                </button>
        </div>
    );
}