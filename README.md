\# Homework 2 - Generative AI API Exploration



\## Overview

This project explores the Anthropic Claude API using Python, demonstrating four key AI capabilities.



\## Setup

1\. Clone this repository

2\. Install dependencies: `pip install -r requirements.txt`

3\. Create a `.env` file with your API key: `ANTHROPIC\_API\_KEY=your-key-here`



\## Files

\- `part1\_image.py` - Multimodal image analysis using Claude

\- `part2\_summarize.py` - Text summarization using Claude

\- `part3\_similarity.py` - Semantic similarity comparison using Claude

\- `part4\_functions.py` - Function calling/tool use with Claude



\## Results



\### Part 1: Multimodal Image Analysis

Sent a JHU Blue Jay mascot image to Claude. The model accurately identified it as the Johns Hopkins University mascot, describing its colors, clothing, and pose in detail.



\### Part 2: Text Summarization

Provided a paragraph about Johns Hopkins University. Claude summarized it into 3 concise bullet points covering its founding, reputation, and academic achievements.



\### Part 3: Semantic Similarity

Compared sentence pairs:

\- "The cat sat on the mat" vs "A feline rested on a rug" → Score: 0.95 (highly similar)

\- "The cat sat on the mat" vs "The stock market crashed today" → Score: 0.0-0.05 (not similar)



\### Part 4: Function Calling

Defined a `get\_weather` tool. When asked about Tokyo's weather, Claude correctly identifie

