from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        from_attributes=True,
        extra="ignore"
    )

    db_url: str
    SECRET_KEY :str
    ALGORITHM :str
    EXP_TIME:int

settings = Settings()
