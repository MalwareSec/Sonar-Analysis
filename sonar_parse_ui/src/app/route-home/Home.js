import React, { useState, useEffect, useCallback } from 'react'; 
import Banner from "../core/banner/Banner";
import Search from "../core/search/Search";
import "./Home.scss";

function Home(props) {
    const [records, setRecords] = useState([]);

    useEffect(() => {
        const handleRecords = (records) => {
            setRecords(records);
        };

        const clearRecords = () => {
            setRecords([]);
        }

        props.objUI["update_records"] = handleRecords
        props.objUI["clear_records"] = clearRecords
        
      }, [props.objUI]);

    return (
        <div className="page-body">
            <Banner title="Sonar Parse Dashboard" objui={props.objUI}/>
            <div className="stream-container"> 
                <Search objui={props.objUI}/>
                { records &&
                    records.map((record, index) => {
                        return(
                            <div className="stream-widget"  key={ index }>
                               <div><pre>{ JSON.stringify(record, null, 2) }</pre></div>
                            </div>
                        )
                })}
            </div>
        </div>
    )
}

export default Home;