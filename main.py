from jokeapi import Jokes # Import the Jokes class
import asyncio
import logging
from datetime import datetime
import aiohttp

# set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def print_joke():
    j = await Jokes()  # Initialise the class
    start_invoke_time = datetime.now()
    logging.info(" Joke API invocation STARTED.")
    joke = await j.get_joke()  # Retrieve a random joke
    end_invoke_time = datetime.now()
    duration = (end_invoke_time - start_invoke_time).total_seconds()
    logging.info(f" Joke API invocation ENDED. Took {duration:.3f}s")

    if joke["type"] == "single": # Print the joke
        print(joke["joke"])
    else:
        print(joke["setup"])
        print(joke["delivery"])

async def print_quote():
    quote_api = "https://zenquotes.io/api/"
    header = {"Accept": "application/json"}

    start_invoke_time = datetime.now()
    logging.info(" Quote API invocation STARTED.")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{quote_api}/random", headers=header) as response:
                data = await response.json()
                quote_text = data[00]["q"]
                author = data[00]["a"]
    except Exception as e:
        quote_text = f"Error: {e}"
        author = "Unknown"
    end_invoke_time = datetime.now()
    duration = (end_invoke_time - start_invoke_time).total_seconds()
    logging.info(f" Quote API invocation ENDED. Took {duration:.3f}s")
    logging.info(f"Quote: {quote_text} - Author: {author}")

async def main():
    logging.info(" Main execution STARTED.")
    
    # Create tasks for jokes and quotes
    tasks = [print_joke(), print_quote()]
    
    # Await all tasks concurrently
    await asyncio.gather(*tasks)
    
    logging.info(" Main execution ENDED.")

if __name__ == "__main__":
    asyncio.run(main())