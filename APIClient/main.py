import requests
import json


class APIClient:
    def __init__(self,base_url):
        self.base_url=base_url
        self.session=requests.session()
        self.session.headers.update(
            {
                'Content-Type':'application/json',
                'Accept':'application/json'
            }
        )

    def handle_response(self,response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print("HTTP Error:{}".format(e))
            print("Response text:{}".format(response.text))
            raise 
        except json.JSONDecoderError:
            print("Error occurred while json decodding")
            return response.text
    
    def create_resource(self,endpoint,data):
        url=self.base_url+'/'+endpoint 
        response=self.session.post(url,json=data)
        return self.handle_response(response)


    def get_resource(self,endpoint,resource_id:str=None):
        url=self.base_url+'/'+endpoint
        if resource_id:
            url=url + '/' + resource_id
        response=self.session.get(url)
        return self.handle_response(response)

    def delete_resource(self,endpoint,resource_id:str):
        url=self.base_url+'/'+endpoint+'/'+resource_id 
        response = self.session.delete(url)
        return self.handle_response(response)

    def update_resource(self,endpoint,resource_id:str,data):
        url=self.base_url+'/'+endpoint+'/'+resource_id
        response=self.session.put(url,json=data)
        return self.handle_response(response)

    def patch_resource(self,endpoint,resource_id,data):
        url=self.base_url+'/'+endpoint+'/'+resource_id
        response=self.session.patch(url,json=data)
        return self.handle_response(response)
    

def main():
    base_url="https://jsonplaceholder.typicode.com"
    api_client = APIClient(base_url)

    data={
        'name':'sandeep',
        'job':'flipkart',
        'id':'1996'
    }
    resp=api_client.create_resource('posts',data)
    print(resp)
    

    resp=api_client.get_resource('posts','1')
    print(resp)

    resp=api_client.update_resource('posts','1',data)
    print(resp)
    

    resp=api_client.delete_resource('posts','1')
    print(resp)

    resp=api_client.patch_resource('posts','1',data)
    print(resp)

    
    
    


    



if __name__ == '__main__':
    main()
