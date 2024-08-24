from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers import task

# Definindo o servidor
app = FastAPI(
    title="Tasks",
    description="API necessária para manutenção de tarefas criadas pelo usuario em um frontend",
    version="1.0.0",
)

# Tasks conterá todas as rotas necessárias para funcionamento da aplicação
app.include_router(task.router)

origins = [
    "http://localhost:8000",  # Allow requests from localhost:3000
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
