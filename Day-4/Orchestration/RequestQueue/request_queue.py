from threading import Thread
import uuid 

from collections import deque
from models import AIRequest,RequestStatus

class RequestQueue:
    def __init__(self,orchestrator):
        self.orchestrator = orchestrator
        self.queue = deque()
        self.history = []

    def AddRequest(self,task,data,provider):

        request = AIRequest(
            request_id=str(uuid.uuid4()),
            task = task,
            provider = provider,
            data = data,
            status = RequestStatus.PENDING
        )
        self.queue.append(request)

        print(f"request added: {request.request_id}")
        print(f"request task: {request.task}")

        return request.request_id
    
    def worker(self,request):
        request.status = RequestStatus.RUNNING

        print(f"Running : {request.request_id} | {request.task}")
        try:

            response = self.orchestrator.execute(task=request.task,data = request.data,provider = request.provider)

            request.result = response

            if response.success:
                request.status = RequestStatus.COMPLETED
            else:
                request.status = RequestStatus.FAILED
        
        except Exception as e:

            request.status = RequestStatus.FAILED
            request.result = str(e)
        
        self.history.append(request)
    
    def ProcessQueue(self):
        threads = []

        while self.queue:
            request = self.queue.popleft()

            thread = Thread(
                target = self.worker,
                args=(request,)
            )

            thread.start()

            threads.append(thread)

        for thread in threads:
            thread.join()

    def printSummary(self):

        print("\n" + "=" * 90)
        print("Execution Summary")
        print("=" * 90)

        for request in self.history:

            provider = "-"

            if hasattr(request.result, "provider_name"):
                provider = request.result.provider_name

            print(
                f"Request ID : {request.request_id}"
            )

            print(
                f"Task       : {request.task}"
            )

            print(
                f"Status     : {request.status.value}"
            )

            print(
                f"Provider   : {provider}"
            )

            print("-" * 90)


            