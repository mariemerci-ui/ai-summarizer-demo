from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

# Example text
text = """
Artificial Intelligence is transforming industries by automating tasks,
enhancing decision-making, and enabling new innovations.
"""

# Generate summary
summary = summarizer(text, max_length=30, min_length=10, do_sample=False)

print("Input:", text)
print("Summary:", summary[0]['summary_text'])
