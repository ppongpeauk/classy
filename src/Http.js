import React from 'react';

class Http {
    constructor() {
        this.http = new XMLHttpRequest();
    }
    get_contents(url) {
        this.http.open("GET", url);
        this.http.send();
        this.http.onreadystatechange = (e) => {
            return http.responseText;
          }
    }
}