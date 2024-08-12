import {useNavigate} from "react-router-dom";

export default function CardLab({ title, path, picture}) {

    const navigate = useNavigate();

    function handleClick() {
        navigate(path);
    }

    return (
        <button className="flex flex-col justify-center items-center text-white" onClick={handleClick}>
            <img src={picture} alt="picture"/>
            <span>{title}</span>
        </button>
    );
}