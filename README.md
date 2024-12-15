# Comment & Journal (CJ)

## Overview

**Comment and Journal (CJ)** is a web application that analyzes YouTube comments to provide sentiment insights and a brief description of the corresponding video. The application employs advanced machine learning techniques, specifically transformers and artificial neural networks (ANNs), to accurately assess the emotional tone of comments and summarize video content.

## Features

- **Sentiment Analysis**: Classifies comments into positive, negative, and neutral categories, helping users understand the overall sentiment of audience reactions.
- **Video Description**: Retrieves and displays a concise description of the YouTube video using an API, enhancing user context.
- **Interactive Visualizations**: Utilizes Altair for intuitive visual representations of sentiment data, allowing users to easily interpret results.
- **Real-time Progress Indicators**: Provides feedback during data processing, enhancing user experience and engagement.

## Technologies Used

- **Streamlit**: A framework for building interactive web applications rapidly and efficiently.
- **Pandas**: For data manipulation and analysis, particularly in handling and processing comment data.
- **Altair**: A statistical visualization library used to create interactive charts for sentiment analysis results.
- **YouTube API**: To fetch comments and metadata associated with YouTube videos.
- **Machine Learning Techniques**: 
  - **Transformers**: Employed for natural language processing tasks, specifically for classifying comment sentiments using Hugging Face's Transformers library.
  - **Artificial Neural Networks (ANN)**: Used to further enhance the accuracy of sentiment classification.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RijoSLal/cj.git
    cd cj
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Access the application via the provided local URL in your web browser.
2. Input the desired YouTube video link into the designated input box.
3. Click the "Analyze" button to process the comments and display the sentiment analysis results.
4. Review the interactive charts and the brief video description presented.

## Code Structure

- **cj.py**: The main script containing the Streamlit application interface and functionalities.
- **model.py**: Implements the machine learning models and functions for analyzing comments.
- **yt_api.py**: Facilitates interactions with the YouTube API to retrieve video comments.
- **transcript.py**: Connects to an API to obtain video descriptions for context.

## Machine Learning Details

### Sentiment Analysis

The sentiment analysis feature employs state-of-the-art transformer models to classify comments based on emotional tone. The models have been trained on large twitter datasets, allowing them to generalize well across various comment types.

### Model Architecture

- **Transformers**: Utilized for natural language processing tasks, specifically fine-tuned for sentiment classification using Hugging Face's Transformers.
- this transforer is pretrained to improve sentiment prediction accuracy, allowing for nuanced understanding of comment sentiments.

## Contributions

Contributions to the project are welcome. If you would like to contribute, please fork the repository and submit a pull request.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Altair](https://altair-viz.github.io/)
- [YouTube API](https://developers.google.com/youtube/v3)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Gemini API](https://yourgeminiapi.com/)

