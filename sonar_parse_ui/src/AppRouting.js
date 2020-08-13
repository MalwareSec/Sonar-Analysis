import React from 'react';
import { Route, Switch, withRouter, Redirect } from "react-router-dom";
import Home from "./app/route-home/Home";
import NotFound from "./app/core/NotFound";

function AppRouting(props) {
    return (
        <Switch>  
            <Route exact path="/">
                <Redirect to="/home" />
            </Route>
            <Route exact path="/home" render={ () => <Home {...props} objui={props.objUI}/> }/>
            <Route component={NotFound}/>
        </Switch> 
    )
}

export const AppRouter = withRouter(AppRouting);

