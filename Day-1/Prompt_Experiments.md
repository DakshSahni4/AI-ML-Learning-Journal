# Mini Practical Exercise

**LLM Used:** ChatGPT (GPT-5.5)

## 1. Summarize a Technical Article

### Prompt Used

> Summarize the article and give major points from it
> [https://www.sciencedirect.com/science/article/pii/S2772503025000799](https://www.sciencedirect.com/science/article/pii/S2772503025000799)

### Output

The model summarized the paper *Artificial Intelligence (AI): Foundations, Trends and Future Directions (2025)* by explaining:

* AI foundations and history
* Relationship between AI, Machine Learning, and Deep Learning
* Current AI technologies such as NLP, Computer Vision, Robotics, and Autonomous Vehicles
* Real-world applications in healthcare, education, finance, manufacturing, agriculture, and security
* Future trends including Large Language Models (LLMs), Artificial General Intelligence (AGI), and Quantum AI
* Ethical issues such as bias, privacy, transparency, accountability, and responsible AI development. 


## 2. Generate Python Code

### Prompt Used

> Give a Python code to make a calculator

### Output

The model generated a console-based calculator capable of:

* Addition
* Subtraction
* Multiplication
* Division
* Exit option

The code also handled division by zero and accepted user input from the console. 

## 3. Debug a Small Piece of Code

### Prompt Used

> Debug the following Python code:

```python
tasks = []
while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
```

### Output

The model identified formatting and indentation issues caused by copying the code and provided a corrected version with proper indentation and working logic for the to-do list application. 


## 4. Compare Responses Across Two Different Prompts

### Prompt 1

> Give a Python code to make a calculator.

### Response

The model generated a complete calculator program with helper functions, error handling, an interactive menu, example output, and suggestions for future improvements. 

### Prompt 2

> Just give a Python code for calculator.

### Response

The model generated only the calculator code without explanations, example output, or additional suggestions. 


## What Worked Well

* The article summary was accurate and well organized.
* The generated Python code was correct and executable.
* The debugging response identified and fixed the issues.
* The model adapted its responses based on the prompt.

## What Did Not Work Well

* The first calculator response contained extra explanation that was not requested.
* The debug output assumed the formatting issue was due to copying, which may not always be the actual cause.

## Effect of Changing the Prompt

Changing the prompt significantly affected the response quality.When we prompted it to genrate just a python code then it genrated the python code only and not the explanations which was genrated when we did not used the word "just" when given a simple task LLMs tends to make conversations but when words like "just" or "You are a python code genrator" then the LLMs didnt forced conversations.