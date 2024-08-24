from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from services.task import TaskService


# Cria o roteador para as rotas
router = APIRouter(prefix="/task")

# Aqui teremos um crud simples possuindo 6 funções: Criar, Ler 1 task, Ler 2 itens, Atualizar 1 task,Atualizar todas e Deletar 1 task


service = TaskService()


@router.post("/create")
async def create_task(task: dict):
    try:
        print(task)
        task_id = service.create(task)
        return JSONResponse(
            content={"message": "Task criada com sucesso", "id": task_id},
            status_code=201,
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Erro ao criar task") from e


# Exemplo de rota GET
@router.get("/{task_id}")
async def get_one_task(task_id: int, q: str = None):
    try:
        task = service.get_one(task_id)

        if len(task) > 0:
            return JSONResponse(content={"task": dict(task[0])}, status_code=200)
        else:
            return JSONResponse(
                content={"message": "Task não encontrada"}, status_code=404
            )
    except Exception as e:
        raise HTTPException(status_code=400, detail="Erro ao ler task") from e


@router.get("/")
async def get_many_itens(status: bool = None):
    try:
        tasks = service.get_many()
        if status:
            tasks = [task for task in tasks if task["status"] == status]
            return JSONResponse(content={"tasks": tasks}, status_code=200)
        else:
            return JSONResponse(content={"tasks": tasks}, status_code=200)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Erro ao ler tasks") from e


# Exemplo de rota PUT
@router.put("/{task_id}")
async def update_task(task_id: int, task: dict):
    try:
        has_task = service.get_one(task_id)
        if len(has_task) > 0:
            updated_task = service.update(task_id, task)
            return JSONResponse(
                content={
                    "message": "Task atualizada com sucesso",
                    "task": updated_task,
                },
                status_code=200,
            )
        else:
            return JSONResponse(
                content={"message": "Task não encontrada"}, status_code=404
            )
    except Exception as e:
        print("err", e)
        raise HTTPException(status_code=400, detail="Erro ao atualizar task") from e


# Exemplo de rota POST
@router.delete("/{task_id}")
async def delete_task(task_id: int):
    try:
        has_task = service.get_one(task_id)
        if len(has_task) > 0:
            service.delete(task_id)
            return JSONResponse(
                content={"message": "Task deletada com sucesso!"}, status_code=204
            )
        else:
            return JSONResponse(
                content={"message": "Task não encontrada"}, status_code=404
            )
    except Exception as e:
        print("err", e)
        raise HTTPException(status_code=400, detail="Erro ao deletar task") from e
