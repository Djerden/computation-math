import {Link} from "react-router-dom";
import MainTextComponent from "../components/MainTextComponent.jsx";

const cardBlackStyle = "flex bg-custom-314455 text-white w-32 h-32 items-center justify-center"
const cardWhiteStyle = "flex bg-custom-97aabd text-black font-bold w-32 h-32 items-center justify-center";

export default function Home() {
    return (
        <>
            <MainTextComponent>Home</MainTextComponent>
            <section className="flex flex-col items-start gap-5 px-6">
                <div className="grid grid-cols-2 gap-4">
                    <div className={cardBlackStyle}>
                        <Link to="/lab3">Lab 3</Link>
                    </div>
                    <div className={cardWhiteStyle}>
                        <Link to="/lab4">Lab 4</Link>
                    </div>
                    <div className={cardWhiteStyle}>
                        <Link to="/lab5">Lab 5</Link>
                    </div>
                    <div className={cardBlackStyle}>
                        <Link to="/lab6">Lab 6</Link>
                    </div>
                </div>
            </section>
        </>
    );
}