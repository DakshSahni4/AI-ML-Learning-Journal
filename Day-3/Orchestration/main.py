from Orchestrator import AIOrchestrator


def main():

    orchestrator = AIOrchestrator()

    # Generate Text
    response = orchestrator.execute(
        provider_name="openai",
        task= "generate_text",
        data=" Write a poem about AI"
    )

    print("\nGenerate Text")
    print(response)

    # Summarize
    response = orchestrator.execute(
        provider_name="claude",
        task="summarize",
        data= " Artificial Intelligence is transforming industries"
    )

    print("\nSummarize")
    print(response)

    # Classify
    response = orchestrator.execute(
        provider_name="gemini",
        task="classify",
        data= " This movie is amazing"
    )

    print("\nClassify")
    print(response)

    # Health Check
    response = orchestrator.execute(
        provider_name="openai",
        task="health_check",
        data=""
    )

    print("\nHealth Check")
    print(response)


if __name__ == "__main__":
    main()



