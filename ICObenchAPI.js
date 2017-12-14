const request = require('request');
const CryptoJS = require('crypto-js');

class ICObench {
    constructor(){
        this.publicKey = "";
        this.privateKey = "";
        this.apiUrl = 'https://icobench.com/api/v1/';
    }

    get(action, callback, data = {}) {
        let dataJSON = JSON.stringify(data);

        let sign = CryptoJS.HmacSHA384(dataJSON, this.privateKey);
        sign = CryptoJS.enc.Base64.stringify(sign);

        request.post(this.apiUrl + action, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-ICObench-Key': this.publicKey,
                'X-ICObench-Sig': sign,
            },
            forever: true,
            json: data
        }, function (error, response, body){
            console.log(body);
        });
    }
}

let test = new ICObench();

test.get("icos/trending", (data) => {console.log(data)});
