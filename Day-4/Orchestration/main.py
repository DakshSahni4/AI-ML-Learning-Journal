from Orchestrator import AIOrchestrator


def main():

    orchestrator = AIOrchestrator()

    response = orchestrator.execute(
        task= "generateText",
        data=" Write a poem about AI"
    )

    print("\nGenerate Text")
    print(response)


    response = orchestrator.execute(
        task="getModelInfo",
        data= " Artificial Intelligence is transforming industries"
    )

    print("\n Get Model Info")
    print(response)


    response = orchestrator.execute(
        task="generateJSON",
        data= " This movie is amazing"
    )

    print("\nGenerate JSON")
    print(response)

    response = orchestrator.execute(
        task="healthCheck",
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



