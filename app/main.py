import os
import asyncio
from api_handler import FileManange 

fm = FileManange()



class DataProcessor:
    def __init__(self, config,repo_details):
        self.config = config
        self.repo_details = repo_details

    def update_data(self):
        pass


async def main():
    config = fm.load_config(os.environ.get("PAT_CONFIG_FILE"))
    tasks = []
    for repo_details in config["REPO_DETAILS"]:
        processor = DataProcessor(config, repo_details)
        task = asyncio.create_task(processor.update_data())
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

    