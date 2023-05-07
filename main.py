import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class People(BaseModel):  # 继承了BaseModel，定义了People的数据格式
    name: str = None  # 默认了name的值为None
    age: int = 18  # 默认了age为18
    sex: str = "male"  # 默认了sex为renyao
    a: int = 1
    b: int = 1

@app.get("/health")
async def read_item():
    return {"name": "hello world"}


@app.post("/fastapi/")
async def postdate(people: People):  # 传入一个People类型的参数people
    return people


# 计算求和的接口
@app.post("/sum/")
async def calculate(people: People):  # 传入一个People类型的参数people
    return {"sum":f"{people.a+ people.b}"}




if __name__ == "__main__":
    uvicorn.run(app='main:app', host='0.0.0.0', port=8888, reload=True)
