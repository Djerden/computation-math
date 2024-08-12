import {createBrowserRouter, RouterProvider} from "react-router-dom";

import Root from "./components/Root.jsx";
import Home from "./pages/Home.jsx";
import Lab3 from "./pages/Lab3.jsx";
import Lab4 from "./pages/Lab4.jsx";
import Lab5 from "./pages/Lab5.jsx";
import Lab6 from "./pages/Lab6.jsx";


function App() {

    const router = createBrowserRouter([
        {
            path: '/',
            element: <Root />,
            children: [
                {path: '/', element: <Home />},
                {path: '/lab3', element: <Lab3 />},
                {path: '/lab4', element: <Lab4 />},
                {path: '/lab5', element: <Lab5 />},
                {path: '/lab6', element: <Lab6 />},
            ]
        },
    ]);

    return (
        <RouterProvider router={router}/>
    )
}

export default App
