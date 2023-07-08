"""

A simple library designed to help you utilize Discord's OAuth2.

Ever wanted to be able to make your own "Continue with Discord" button? Well, we're here for ya!

Tested only with framework Flask, though it will probably work with any as long as it is correctly configured.

-------------------------------

MIT License

Copyright (c) 2022 - 2023 ItsTato

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

class DiscordOAuth2:
    def __init__(self,fqdn:str="http://127.0.0.1",port:int=80,client_id:int=0,client_secret:str="",redirect_endpoint:str="/auth/response",scopes:list=["identify"]) -> None:
        import requests
        self.__requests = requests
        self.fqdn:str = fqdn
        self.port:int = port
        self.client_id:int = client_id
        self.client_secret:str = client_secret
        self.redirect_endpoint:str = redirect_endpoint
        self.__api_url:str = "https://discord.com/api"
        self.__token_url:str = f"{self.__api_url}/oauth2/token"
        self.scopes:list = scopes

    def patch_url(url:str) -> str:
        return url.replace(":","%3A").replace("/","%2F")

    def formatScopes(self) -> str:
        final:str = ""
        for i, scope in enumerate(self.scopes):
            if i != 0:
                final = f"{final}%20{scope}"
            else:
                final = scope

    def getRedirectUri(self) -> str:
        suffix:str = f":{self.port}" if not self.port == 80 else ""
        return f"{self.fqdn}{suffix}{self.redirect_endpoint}"

    def getLoginUrl(self) -> str:
        formatted_scopes:str = self.formatScopes()
        return f"{self.__api_url}/oauth2/authorize?client_id={self.client_id}&redirect_uri={self.getRedirectUri()}&response_type=code&scope={formatted_scopes}"

    def getAccessToken(self,code:str) -> str:
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.getRedirectUri(),
            "scope": self.formatScopes()
        }
        access_token:str = self.__requests.post(url=self.__token_url,data=payload).json()
        return access_token.get("access_token")

    def getUserJson(self,access_token:str) -> dict:
        url:str = f"{self.__api_url}/users/@me"
        bearer = f"Bearer {access_token}"
        headers = {
            "Authorization": bearer
        }
        user_object:dict = self.__requests.get(url=url,headers=headers).json()
        return user_object
