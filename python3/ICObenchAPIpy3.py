import requests
import json
import hmac
import hashlib
import base64


class IcoBench:
    icoBenchApi = {
        "ICOBENCH_PRIVATE_KEY": "xxxxxx",
        "ICOBENCH_PUBLIC_KEY": "xxxxxx",
        "API_URL": "https://icobench.com/api/v1/"
    }

    @classmethod
    def sendIcoBenchRequest(cls, queryParams=(), pathParams={}, data=()):
        hash = hmac.new(cls.icoBenchApi["ICOBENCH_PRIVATE_KEY"].encode('utf-8'), ''.encode('utf-8'), hashlib.sha384)

        dataJSON = json.dumps(data)
        hash.update(dataJSON.encode('utf-8'))
        sign = hash.digest()
        sign = base64.b64encode(sign)

        request_headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-ICObench-Key': cls.icoBenchApi["ICOBENCH_PUBLIC_KEY"],
            'X-ICObench-Sig': sign
        }

        url = cls.icoBenchApi["API_URL"];
        for val in pathParams:
            url = url + val + "/"
        if all(queryParams) and url.endswith('/'):
            url = url[:-1]
        dataJSON = json.dumps(data)

        response = requests.post(url=url, params=queryParams, data=dataJSON, headers=request_headers)
        return response.json()

    @classmethod
    def getIcos(cls, queryParams=(), pathParams=["icos", "all"], data=()):
        return IcoBench.sendIcoBenchRequest(queryParams=queryParams, pathParams=pathParams, data=data)

    @classmethod
    def getIco(cls, queryParams=(), pathParams=["ico", "1"], data=()):
        return IcoBench.sendIcoBenchRequest(queryParams=queryParams, pathParams=pathParams, data=data)

    @classmethod
    def getOther(cls, queryParams=(), pathParams=["other", "stats"], data=()):
        return IcoBench.sendIcoBenchRequest(queryParams=queryParams, pathParams=pathParams, data=data)

    @classmethod
    def getPeople(cls, queryParams=(), pathParams=["people", "registered"], data=()):
        return IcoBench.sendIcoBenchRequest(queryParams=queryParams, pathParams=pathParams, data=data)

    @classmethod
    def getFilters(cls, queryParams=(), pathParams=["icos", "filters"], data=()):
        return IcoBench.sendIcoBenchRequest(queryParams=queryParams, pathParams=pathParams, data=data)



print(IcoBench.getIcos())
print(IcoBench.getIcos(pathParams=["icos","trending"]))
print(IcoBench.getIco(pathParams=["ico","2"]))
print(IcoBench.getOther())
print(IcoBench.getPeople())
print(IcoBench.getFilters())
print(IcoBench.getIcos(queryParams=(), pathParams=["icos","all"], data={'search': 'DMarket'}))
print(IcoBench.getIcos(queryParams=(), pathParams=["icos","all"], data={"orderDesc":"rating","status":"active"}))