export default function Solution({answer}) {

    function prepareAnswer() {
        const isNotEmpty = (obj) => Object.keys(obj).length > 0;

        const result = []

        const formatObject = (obj) => {
            return Object.entries(obj)
                .map(([key, value]) => `${key}: ${value}`)
                .join('\n'); // Преобразуем объект в строку "ключ: значение"
        };

        if (isNotEmpty(answer.linear)) {
            result.push(`Линейная:\n${formatObject(answer.linear)}`);
        }

        if (isNotEmpty(answer.square)) {
            result.push(`Квадратичная:\n${formatObject(answer.square)}`);
        }

        if (isNotEmpty(answer.cubic)) {
            result.push(`Кубическая:\n${formatObject(answer.cubic)}`);
        }

        if (isNotEmpty(answer.exp)) {
            result.push(`Экспоненциальная:\n${formatObject(answer.exp)}`);
        }

        if (isNotEmpty(answer.logarithm)) {
            result.push(`Логарифмическая:\n${formatObject(answer.logarithm)}`);
        }

        if (isNotEmpty(answer.power)) {
            result.push(`Степенная:\n${formatObject(answer.power)}`);
        }
        // Если result пустой, возвращаем пустую строку
        return result.length > 0 ? result.join('\n\n') : '';
    }

    let result = prepareAnswer();
    // Если результат пустой, присваиваем "Answer will be here"
    result = result || "Answer will be here";

    function saveAnswerAsFile(fileName) {

        const blob = new Blob([result], {type: 'text/plain'});

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
                value={result}>
            </textarea>
            <button
                className="bg-white text-black px-4 py-2 rounded hover:bg-neutral-300"
                onClick={() => {saveAnswerAsFile('lab4_results.txt')}}
            >
                Save to
            </button>
        </div>
    );
}