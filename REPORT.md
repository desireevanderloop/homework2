\# Homework 2 Report



\## 1. Business Use Case

This prototype demonstrates an AI-assisted text summarization pipeline for a university communications office. Staff receive large volumes of articles, reports, and emails daily and need quick summaries to prioritize their reading. The workflow takes unstructured text as input and produces a structured 3-bullet-point summary, reducing the time staff spend on manual reading and triage.



\## 2. Model Selection: Why Claude

I chose Anthropic's claude-opus-4-5 out of genuine curiosity. Rather than defaulting to another model, I wanted to explore how Claude approached these tasks and what the developer experience felt like end to end. In practice, Claude performed well across all four tasks with a single unified API for images, text, and tool use. Instruction-following was strong - the model reliably produced concise, accurately formatted bullet points without requiring extensive prompt engineering. The one limitation is the absence of a native embeddings endpoint; semantic similarity was handled by prompting the model directly instead of using true vector embeddings, which is less rigorous for production use.



\## 3. Baseline vs. Final Prompt Design



\*\*Part 1 - Image Analysis:\*\*

\- Baseline: "What is in this image?" - produced a vague, one-sentence response

\- Revision 1: "Describe this image." - slightly more detail but still unstructured

\- Final: "Describe what you see in this image in detail." - produced a structured breakdown covering body, coloring, clothing, pose, and background



\*\*Part 2 - Text Summarization:\*\*

\- Baseline: "Summarize this." - returned a paragraph nearly as long as the original

\- Revision 1: "Summarize this in bullet points." - produced bullets but inconsistent count

\- Final: "Please summarize the following text in 3 bullet points." - consistently produced exactly 3 concise, well-formatted points



\*\*Part 3 - Semantic Similarity:\*\*

\- Baseline: "Are these sentences similar?" - returned yes/no with no quantification

\- Revision 1: "How similar are these sentences?" - returned vague qualitative answers

\- Final: "Rate the semantic similarity on a scale of 0 to 1 and explain your reasoning." - produced numeric scores with clear justification



\## 4. Prototype Limitations

The semantic similarity scoring relies on the model's judgment rather than true vector embeddings, meaning scores are not reproducible in a strict statistical sense and could vary between runs. The summarization prototype has no safeguards against misleading or adversarial input text, and the model could produce confidently incorrect summaries for highly technical or domain-specific content outside its training data. The app stores the API key in a local .env file, which is not suitable for shared or cloud-deployed environments without proper secrets management. All outputs should be reviewed by a human before any action is taken.



\## 5. Deployment Recommendation

This workflow is not ready for unsupervised production deployment but shows genuine promise as a human-in-the-loop tool. I would recommend a limited pilot under the following conditions: (1) all model outputs are reviewed by staff before any action is taken, (2) semantic similarity is replaced with a proper embeddings model for reproducibility, (3) API credentials are managed through a secrets manager, and (4) a feedback loop is established so that staff corrections are used to refine prompts over time. Under these conditions, the workflow could meaningfully reduce manual effort while keeping a human accountable for final decisions.

