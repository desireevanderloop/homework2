\# Homework 2 Report



\## 1. Business Use Case

The prototype demonstrates an AI-assisted content analysis pipeline suited for a university communications or academic research office. The four capabilities — multimodal image analysis, text summarization, semantic similarity scoring, and function calling — support a workflow where large volumes of unstructured content are automatically triaged, summarized, and routed for human review.



\## 2. Model Selection: Why Claude

I chose Anthropic's claude-opus-4-5 out of genuine curiosity — I wanted to explore how a different frontier model approached these tasks and what the developer experience felt like end to end. Claude performed well across all four tasks with a single unified API for images, text, and tool use. The one limitation is the absence of a native embeddings endpoint; semantic similarity was handled by prompting the model directly instead of using true vector embeddings.



\## 3. Baseline vs. Final Prompt Design

\*\*Part 1 - Image Analysis:\*\*

\- Baseline: "What is in this image?" → vague one-sentence response

\- Final: "Describe what you see in this image in detail." → structured breakdown of the JHU Blue Jay mascot



\*\*Part 2 - Text Summarization:\*\*

\- Baseline: "Summarize this." → paragraph nearly as long as the original

\- Final: "Please summarize the following text in 3 bullet points." → concise, well-formatted output



\*\*Part 3 - Semantic Similarity:\*\*

\- Baseline: "Are these sentences similar?" → yes/no with no quantification

\- Final: "Rate similarity on a scale of 0 to 1 and explain your reasoning." → numeric scores with justification



\## 4. Prototype Limitations

The semantic similarity scoring relies on the model's judgment rather than true vector embeddings, meaning scores are not reproducible in a strict statistical sense. The image analysis has no safeguards against adversarial imagery. The function-calling implementation does not actually execute the called function or handle downstream errors. API credentials are stored in a local .env file, which is not suitable for cloud deployment without secrets management.



\## 5. Deployment Recommendation

This workflow is not ready for unsupervised production deployment but shows promise as a human-in-the-loop tool. I would recommend a limited pilot under these conditions: (1) all outputs are reviewed by staff before any action is taken, (2) semantic similarity is replaced with a proper embeddings model, (3) credentials are managed through a secrets manager, and (4) a feedback loop is established to refine prompts over time.

