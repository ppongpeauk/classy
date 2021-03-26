import react from 'react';

class OngoingClass extends react.Component {
    constructor() {
        super();
        this.state = {
            "data": {
                "success": true,
                "isClassOngoing": true,
                "ongoingClass": {
                    "className": "default class",
                    "classInstructor": "sus",
                    "classMeetingLink": "https://google.com"
                },
            }
        };
        this.checkOngoingClass();
    }
    checkOngoingClass() {
        fetch('http://localhost:5124/v1/get-ongoing-class')
            .then(response => response.json())
            .then(data => {
                this.setState(() => ({
                    data: data
                }));
            });
        
    }
    render() {
        if(this.state.data.isClassOngoing === true) {
            let thumbnail;
            if (this.state.data.ongoingClass.thumbnail !== "") {
                thumbnail = <img src={this.state.data.ongoingClass.thumbnail} height="128" width="128" style={{margin: 4 + 'px'}} alt="Ongoing Class Thumbnail"/>
            }
            return (
                <div class="alert alert-dark" role="alert">
                    <h3>class in-session</h3>
                    <hr/>
                    <p>Your <b>{this.state.data.ongoingClass.className}</b> class with <b>{this.state.data.ongoingClass.classInstructor}</b> is currently in-session.</p>
                    <div/>
                    {thumbnail}
                    <br/>
                    <a href={this.state.data.ongoingClass.classMeetingLink}><b>click here to join the meeting.</b></a>
                </div>
            )
        }
        else {
            return (
                <div class="alert alert-dark" role="alert">
                    <h2>no class in-session</h2>
                </div>
            );
        }
    }
}

export default OngoingClass;