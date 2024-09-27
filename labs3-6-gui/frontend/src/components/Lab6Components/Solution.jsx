import {useEffect, useRef} from "react";

export default function Solution({answer}) {

    const textareaRef = useRef(null);  // Создаём реф для textarea

    const result = answer?.result || 'Answer will be here';  // Безопасная проверка, чтобы result был всегда строкой


    useEffect(() => {
        // Устанавливаем прокрутку в начало при изменении ответа
        if (textareaRef.current) {
            textareaRef.current.scrollTop = 0;
        }
    }, [result]);  // Этот эффект срабатывает каждый раз, когда обновляется `answer`

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
        <div className="flex flex-col bg-custom-314455 text-white p-6 gap-2 rounded w-full">
            <h1 className="text-2xl">Solution</h1>
            <textarea
                className="px-2 py-1 resize-none h-full rounded w-full text-black"
                style={{ fontFamily: 'monospace', whiteSpace: 'pre' }}
                readOnly
                ref={textareaRef}
                value={result}
                wrap="off">
            </textarea>
            <button
                className="bg-white text-black px-4 py-2 rounded hover:bg-neutral-300"
                onClick={() => {saveAnswerAsFile('lab6_results.txt')}}
            >
                Save to
            </button>
        </div>
    );
}