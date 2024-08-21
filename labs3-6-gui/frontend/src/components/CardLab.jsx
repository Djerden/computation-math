import {useNavigate} from "react-router-dom";

export default function CardLab({path, title, image}) {

    const navigate = useNavigate();

    function handleClick() {
        navigate(path);
    }

    return (
        <button className="flex flex-col justify-center items-center bg-custom-314455 w-92 h-96 text-white p-4 rounded" onClick={handleClick}>
            <img className="h-full" src={image} alt="image lab"/>
            <span className="mt-2 font-bold text-xl ">{title}</span>
        </button>
    );
}