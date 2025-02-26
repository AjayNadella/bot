import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

class AutomatedSolver:
    def __init__(self):
        groq_api_key = "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" 
        
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=groq_api_key,
            model_name="llama3-70b-8192"
        )

        self.prompt = PromptTemplate.from_template("""
        You are an advanced AI assistant capable of solving any programming problem, analyzing errors, answering any question, and providing insightful explanations. You understand and interpret information on the screen, adapt to the context, and generate solutions accordingly.

        ### INPUT:
        {question_text}

        ### TASK:
        - Understand and analyze the given input.
        - If it's a programming question, provide a **clear and correct code solution first** without explanations in between.
        - If there's an error, provide the **fixed version of the code first**, followed by an explanation of the error.
        - After the code, **provide a structured explanation** of how the solution works.
        - If it's a general or technical question, provide a direct and concise answer, followed by a detailed explanation if necessary.
        - If it's a conceptual topic, break it down in an easy-to-understand manner.
        - Ensure clarity, accuracy, and relevance in all responses.

        ### RESPONSE:

        **Solution (Code First, No Explanation Here):**
        ```python
        # Code solution goes here
        ```

        **Explanation:**
        - Explanation of the approach, logic, and key concepts used.
        - If applicable, explain any errors and how they were resolved.
        - Additional optimizations or alternative approaches.
        """)


    def generate_solution(self, question_text):
        chain = self.prompt | self.llm

        try:
            response = chain.invoke({"question_text": question_text})
            solution = response.content.strip()
            return solution
        except Exception as e:
            print(f"Error generating solution: {e}")
            return "Failed to generate solution."
