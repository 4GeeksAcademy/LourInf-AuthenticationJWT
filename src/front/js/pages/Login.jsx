import React, { useContext, useState } from "react";

export const Login = () => {
    const { store, actions } = useContext(Context);
    const [email, setEmail] = useState("test@example.com")
    const [password, setPassword] = useState("test")

    const handleOnClick = async () => {
        const url = "https://probable-space-winner-g9456w5ggq53w55j-3001.app.github.dev"; 
        const options = {
            method: "POST",
            body: JSON.stringify({username:email, password:password}),
            headers: {
                "Content-Type": "application/json"
            }

        }
        const response = await fetch(url, options);
        console.log(response);
            const data = await response.json()
            localStorage.setItem("token",data.access_token);
            console.log(data)
        }
        console.log(response.status, response.statusText);


        return (
            <div>
                {store.isLoggedIn ? (
                    navigate('/dashboard')
                ) : (
                    <div>
                        <h1>Login</h1>
                        {/* 1. form with at least 2 inputs (email and password)
                            2. control those inputs with onChange and useState
                        */}
                        <label>Email:</label>
                        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} />
                        <label>Password:</label>
                        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                        <button onClick={handleOnClick}>Log in</button>
                    </div>
                )}
            </div>
        );