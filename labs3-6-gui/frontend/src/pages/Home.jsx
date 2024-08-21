import MainTextComponent from "../components/MainTextComponent.jsx";
import CardLab from "../components/CardLab.jsx";

import zombieGif from "../assets/zombie.gif";
import duckGif from "../assets/duck.gif";
import homerRunGif from "../assets/homer-run.gif";
import rickGif from "../assets/rick.gif";

export default function Home() {
    return (
        <>
            <MainTextComponent>Home</MainTextComponent>
            <section className="flex flex-col items-center gap-5 px-6">
                <div className="grid 2xl:grid-cols-4 lg:grid-cols-2 md:grid-cols-1 gap-4">

                    <CardLab path="/lab3" title="Lab 3" image={zombieGif} />
                    <CardLab path="/lab4" title="Lab 4" image={duckGif}/>
                    <CardLab path="/lab5" title="Lab 5" image={homerRunGif}/>
                    <CardLab path="/lab6" title="Lab 6" image={rickGif}/>

                </div>
            </section>
        </>
    );
}