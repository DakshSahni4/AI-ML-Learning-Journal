from Orchestrator import AIOrchestrator


def main():

    orchestrator = AIOrchestrator()

    # Generate Text
    response = orchestrator.execute(
        task= "generate_text",
        data=" Write a poem about AI"
    )

    print("\nGenerate Text")
    print(response)

    # Summarize
    response = orchestrator.execute(
        task="summarize",
        data= " Artificial Intelligence is transforming industries"
    )

    print("\nSummarize")
    print(response)

    # Classify
    response = orchestrator.execute(
        task="classify",
        data= " This movie is amazing"
    )

    print("\nClassify")
    print(response)

    # Health Check
    response = orchestrator.execute(
        task="health_check",
        data=""
    )

    print("\nHealth Check")
    print(response)

    response = orchestrator.execute(
        task="Converse",
        data=""
    )

    print("\nInvalid Task")
    print(response)

if __name__ == "__main__":
    main()



