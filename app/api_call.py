import requests
import time

from app.api_handler import FileMananger

fm = FileMananger()

class GitHubAPI:
    def __init__(self, config):
        self.config = config
        self.headers = {
            "Accept":"application/vnd.github+json",
            "Authorization":f"bearer{config['GITHUB_API_TOKEN']}",
            "X-GitHub-Api-Version":"2022-11-28"
        }

    def request_api(self,request_url):
        print(f"requesting url:{request_url}")
        response = requests.get(request_url,headers=self.headers)
        return response.json()
    

    def get_pull_request_pages(self, repo_detail):
        pr_page_link = f"https://api.github.com/repos/{repo_detail['REPO_OWNER']}/{repo_detail['REPO_NAME']}/pulls?state=all&per_page=100"
        
        first_pr_page = pr_page_link + "&page=1"
        response = self.request_api(first_pr_page)
        num_pages = -(-response[0]['number'] // 100)

        return [pr_page_link + f"&page={page_num}" for page_num in range(1, num_pages + 1)]
    
    def fetch_repository_pr_data(self,repo_detail):
        pr_pages = self.get_pull_request_pages(repo_detail)
        pr_data = []

        for pr_page in pr_pages:
            pr_data += self.request_api(pr_page)
            time.sleep(int(self.config["REQUEST_TIME_INTERVAL"]))

            print(f"number of PRs: {len(pr_data)}")
            return FileMananger.write_to_file(pr_data,self.config["RAW_DATA_PATH"],"pr_data","json")
        

    def update_pull_request_page(self, repo_detail):
        pr_page_like = f"https://api.github.com/repos/{repo_detail['REPO_OWNER']}/{repo_detail['REPO_NAME']}/pulls?state=all&per_page=100&sort=update&direction=desc"
        
        first_pr_page = pr_page_like + "&page=1"
        response = self.request_api(first_pr_page)
        
        print(f"number of PRs: {len(response)}")
        return fm.write_to_file(response,self.config['RAW_DATA_PATH'],"updated_pr_data",'json')
    