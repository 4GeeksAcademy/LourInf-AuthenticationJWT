import React, { useContext, useState } from "react";
import { Navigate } from "react-router-dom";

export const Dashboard = () => {
    const { store, actions } = useContext(Context);

    const handleLogout = () => {
        actions.logout();
    };

    // //store.isLoggedIn == true -> esta logeado por lo tanto puede ver el dashboard
    // //store.isLoggedIn == false -> no esta logeado por lo tanto no puede ver el dashboard y lo llevo al login
    return (
        <div>
            {store.isLoggedIn ? (
                <>
                    <h1>Dashboard</h1>
                    <p>Welcome, {store.userFullName}!</p>
                    {/* Add your dashboard content here */}
                    <button onClick={handleLogout}>Logout</button>
                </>
            ) : (
                <>
                    <Navigate to="/login" /> {/* Redirect to login if not logged in */}
                </>
            )}
        </div>
    );
};