import React from 'react';
import './assets/main.css';
import './assets/bootstrap/css/bootstrap.min.css';
import OngoingClass from './OngoingClass';
import Quote from './Quote';
class Home extends React.Component {
    render() {
        return (
            <div id="main-container">
                <h1>good evening, <b>{this.props.name}</b>!</h1>
                <Quote/>
                <hr/>
                <OngoingClass/>
                <br/>
            </div>
        )
    }
}
export default Home;
