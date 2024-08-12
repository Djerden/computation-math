import {Link} from "react-router-dom";

import gitHubLogo from '../assets/github.png';

const hoverNavStyle = 'hover:text-white'

export default function Header() {
    return (
        <header className="flex flex-row justify-between items-center w-full py-4 px-6">
            <div className="flex flex-row items-center md:space-x-6 space-x-4">
                <a
                    className="text-3xl font-bold"
                    href="https://en.itmo.ru/">ITMO
                </a>
                <nav className="flex flex-row justify-center">
                    <ul className="flex flex-row md:space-x-2 space-x-1 md:text-xl text-base">
                        <li><Link
                            to="/"
                            className={hoverNavStyle}>
                            Home
                        </Link></li>
                        <li><Link
                            to="/lab3"
                            className={hoverNavStyle}>
                            Lab3
                        </Link></li>
                        <li><Link
                            to="/lab4"
                            className={hoverNavStyle}>
                            Lab4
                        </Link></li>
                        <li><Link
                            to="/lab5"
                            className={hoverNavStyle}>
                            Lab5
                        </Link></li>
                        <li><Link
                            to="/lab6"
                            className={hoverNavStyle}>
                            Lab6
                        </Link></li>
                    </ul>
                </nav>
            </div>

            <div>
                <a className="flex flex-row space-x-2" href="https://github.com/Djerden">
                    <img className="w-6" src={gitHubLogo} alt="github"/>
                    <span>Djerden</span>
                </a>
            </div>
        </header>
    );
}