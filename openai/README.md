# OpenAI API Example

This is a simple script that uses the OpenAI API to generate interesting facts about Jack Russell. The script uses the `openai` Python library to interact with the OpenAI API.

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key
- Using gpt-4o-mini model priced at $0.150 / 1M input tokens as per https://openai.com/api/pricing/


## Installation

1. Clone the repository or download the script.
2. Install the required Python packages using conda:   

   ```sh
    conda create -n openapi-api python=3.10
    ```

    ```sh
    conda activate openapi-api
    ```

    ```sh
    conda install openai
    ```

## Setup

1. Set your OpenAI API key as an environment variable:

    On Windows, use:

    ```sh
    set ACCESS_KEY='your-api-key-here'