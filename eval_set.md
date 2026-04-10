## Evaluation Set



## Case 1 - Normal Case

\*\*Input:\*\* "Johns Hopkins University is a private research university in Baltimore, Maryland. Founded in 1876, it was the first research university in the United States. It is known for its medical school, public health programs, and research output."

\*\*Expected output:\*\* 3 bullet points covering founding, location, and academic strengths.



## Case 2 - Normal Case

\*\*Input:\*\* "The university library system contains over 4 million volumes and provides access to thousands of online journals. Students and faculty can request materials from partner institutions through interlibrary loan."

\*\*Expected output:\*\* 3 bullet points summarizing library resources and access options.



## Case 3 - Edge Case (Very Short Input)

\*\*Input:\*\* "It rained today."

\*\*Expected output:\*\* Model should either produce a minimal summary or indicate there is not enough content to summarize meaningfully. Should not hallucinate additional details.



## Case 4 - Edge Case (Very Long Input)

\*\*Input:\*\* A multi-page academic article with complex terminology.

\*\*Expected output:\*\* Model should still produce exactly 3 bullet points without truncating mid-sentence or losing the main argument. Human review recommended to verify accuracy.



## Case 5 - Likely to Fail / Require Human Review

\*\*Input:\*\* "The Q3 financial report showed a 12% increase in revenue, a 3% decrease in operating costs, and flagged two compliance issues in the eastern region that require immediate attention."

\*\*Expected output:\*\* Model may oversimplify the compliance issues or miss the urgency. A human reviewer should verify that critical action items are not buried or lost in the summary.

