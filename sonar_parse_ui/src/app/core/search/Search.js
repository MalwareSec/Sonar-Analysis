import React from 'react';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import './Search.scss';

const initialFormData = Object.freeze({
    search: ""
});

function Search(props) {
    const [formData, updateFormData] = React.useState(initialFormData);

    const handleChange = (e) => {
        updateFormData({
            ...formData,
            [e.target.name]: e.target.value.trim()
          });
    }

    const getNewRecords = async (e) => {
        e.preventDefault()
    
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        };

        const response = await fetch(`${props.objui.config.api_endpoint_records}`, requestOptions);
        if (!response.ok) {
            //catch error 
            console.log(response);
        } else {
            const response_json = await response.json();
            if (response_json["Records"].length > 0) {
                props.objui.update_records(response_json.Records);
            } else {
                props.objui.update_records(["No Records Found"]);
            }
        }
    }
    return (
            <Form>
                <Form.Group controlId="formSearch">
                    <Form.Label>Search Endpoint</Form.Label>
                    <Form.Control name="search" onChange={handleChange} type="text" placeholder="Enter Search Endpoint" />
                </Form.Group>
                <div className="button-container">
                    <Button variant="primary" onClick={(e) => {getNewRecords(e)}}>
                        Submit
                    </Button>
                    <Button variant="danger" onClick={(e) => {props.objui.clear_records(e);}}>
                        Clear
                    </Button>
                </div>
            </Form>
    );
}

export default Search;