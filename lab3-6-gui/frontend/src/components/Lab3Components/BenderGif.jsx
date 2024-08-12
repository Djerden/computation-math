import benderGif from "../../assets/bender.gif";

export default function BenderGif() {
    return (
        <div className="flex flex-col justify-center items-center flex-grow">
            <img className=" h-full" src={benderGif} alt="bender gif"/>
        </div>
    );
}