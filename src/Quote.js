import react from 'react';

class Quote extends react.Component {
    constructor() {
        super();
        this.state = {
            "data": {
                "_id": "",
                "tags": ["famous-quotes"],
                "content": "",
                "author": "",
                "length": 0
            }
        };
        this.fetchQuote();
    }
    fetchQuote() {
        fetch('https://api.quotable.io/random?maxLength=128?tags=famous-quotes')
            .then(response => response.json())
            .then(data => {
                this.setState(() => ({
                    data: data
                }));
            });
    }
    render() {
        return (
            
            <div>
                <p><b>"{this.state.data.content}"</b> -{this.state.data.author}</p>
            </div>
        )
    }
}

export default Quote;