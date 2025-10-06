# LangGraph Sequential Workflow — Learning Project
## Overview

This repository showcases my learning journey with LangGraph, where I explored how to design sequential AI workflows using modular, prompt-driven nodes.

The main focus of this project is a text-processing workflow built with prompt chaining that performs:

Summarization — Generates a concise, faithful summary of any passage while preserving tone and meaning.

Keyword Extraction — Identifies key terms and phrases that hold the core meaning of the text, avoiding common or filler words.

Through this project, I learned how LangGraph enables the construction of connected reasoning steps, where each node performs a specific LLM-driven task and passes its results to the next — forming a smooth, end-to-end AI workflow.

## Tech Stack

🧩 LangGraph – Sequential and agentic workflow framework for LLMs

⚡ FastAPI – Lightweight backend for serving the workflow as an API

🧠 Gemini (Google Gen AI) – LLM used for summarization and keyword extraction

🧾 Pydantic – For defining request/response schemas and validation

🧪 Jupyter Notebook – Used for experimenting and understanding LangGraph’s flow

🐍 Python 3.10+

## What I Learned

Building sequential workflows using LangGraph nodes and state dictionaries.

Understanding prompt chaining — connecting multiple LLM steps for complex reasoning.

Designing structured prompts that enforce factual accuracy and avoid hallucinations.

Managing state updates between summarization and keyword extraction nodes.

Integrating LLM workflows with FastAPI endpoints for real-world applications.

## Core Workflow

The implemented workflow follows a simple yet powerful structure:

Input Passage → Provided via the API.

Summarization Node → Generates a summary that’s one-third the length of the passage while keeping tone and meaning intact.

Keyword Extraction Node → Extracts 5-10 meaningful keywords directly from the text, ensuring they appear verbatim in the passage.

Final Output → Clean JSON containing the summary and extracted keywords.

This chaining approach helped me grasp how LangGraph handles multi-step reasoning and data flow, which is essential for building larger AI systems.

## Learning Notebook – BMI Sequential Model

This repo also includes a Jupyter Notebook demonstrating a small BMI calculation workflow, created purely for practice.
It helped me understand how LangGraph nodes interact, pass data sequentially, and maintain state — before applying the same logic to LLM-based workflows.

## Impact on My Technical Growth

### Working on this project has:

Strengthened my understanding of LLM orchestration and workflow design.

Improved my ability to write precise prompts for multi-stage reasoning.

Taught me to integrate LangGraph with API systems for scalable deployment.

Enhanced my overall skill in building modular, interpretable AI pipelines.


## In Summary

This project was my first step into LangGraph’s agentic workflows, where I combined summarization and keyword extraction into a clean, stateful chain of LLM tasks.
It deepened my understanding of AI reasoning pipelines and showed how structured graph-based workflows can make large language models more reliable, interpretable, and reusable.