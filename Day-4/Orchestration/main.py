from datetime import datetime
import uuid

from Orchestrator import AIOrchestrator
from models import ExecutionLog
from ExecutionLogger.execution_logger import ExecutionLogger



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

def debug():
    logger = ExecutionLogger()

    log = ExecutionLog(

        execution_id=str(uuid.uuid4()),

        timestamp=str(datetime.now()),

        module="generateText",

        provider="gemini",

        model="gemini-2.5-flash",

        execution_time=0.82,

        success=True,

        error=None
    )

    logger.log(log)

    print("Execution logged successfully!")

    print(logger.filterByDate("2026-07-13"))
    print(logger.filterByStatus(False))
    print(logger.filterByStatus(True))
    print(logger.filterByProvider("gemini"))

if __name__ == "__main__":
    main()



