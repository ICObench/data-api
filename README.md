# ICObench Data API

ICObench Data API allows you to get various information and data from the platform including ICO listings, ratings, and stats.

## Getting Started

To use the ICObench Data API you need to have both "Private Key" and "Public Key".
- Public Key is used to identify the API user and is sent via request header as "X-ICObench-Key".
- Private Key is used to sign every request together with JSON. Both are hashed by HMAC SHA384, converted to base64 and sent via request header as "X-ICObench-Sig".

Please make sure to send data using POST method and from the IP that you have whitelisted in your API settings.

### How can I get the access?
You can request an access to API by following next steps:

- Register a new account [here](https://icobench.com/register)
- Request the API key [here](https://icobench.com/developers)

### Resources

- [ICObench API PHP Class](https://github.com/ICObench/data-api/blob/master/php/ICObenchAPI.php)
- [ICObench API JS Example](https://github.com/ICObench/data-api/blob/master/js/ICObenchAPI.js)
- [ICObench API Python Example](https://github.com/ICObench/data-api/blob/master/python/ICObenchAPI.py)
- [ICObench API Python3 Example](https://github.com/ICObench/data-api/blob/master/python3/ICObenchAPIpy3.py)
- [API documentation](https://icobench.com/developers)

## Authors

View list of [contributors](https://github.com/ICObench/data-api/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
