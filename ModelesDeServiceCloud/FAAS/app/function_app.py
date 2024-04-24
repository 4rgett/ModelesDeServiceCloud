import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.function_name(name="user")
@app.route(route="req", auth_level=func.AuthLevel.ANONYMOUS)
def main(req: func.HttpRequest) -> str:
    user = req.params.get("user")
    return f"Hello, {user}!"