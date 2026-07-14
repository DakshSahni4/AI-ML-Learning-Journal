import os

from dotenv import load_dotenv


load_dotenv()


class Config:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER")

    MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))

    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 30))

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


    @classmethod
    def validate(cls):

        required = {

            "OPENAI_API_KEY": cls.OPENAI_API_KEY,

            "ANTHROPIC_API_KEY": cls.ANTHROPIC_API_KEY,

            "GEMINI_API_KEY": cls.GEMINI_API_KEY,

            "DEFAULT_PROVIDER": cls.DEFAULT_PROVIDER,

            "LOG_LEVEL": cls.LOG_LEVEL

        }

        missing = []

        for key, value in required.items():

            if value is None or value.strip() == "":

                missing.append(key)

        if missing:

            raise ValueError(

                f"Missing configuration values: {', '.join(missing)}"

            )

        if cls.DEFAULT_PROVIDER.lower() not in [

            "openai",

            "claude",

            "gemini"

        ]:

            raise ValueError(

                "DEFAULT_PROVIDER must be openai, claude, or gemini."

            )

        if cls.MAX_RETRIES < 0:

            raise ValueError(

                "MAX_RETRIES cannot be negative."

            )

        if cls.REQUEST_TIMEOUT <= 0:

            raise ValueError(

                "REQUEST_TIMEOUT must be greater than 0."

            )