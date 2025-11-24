from pydantic import BaseModel, Field, field_validator
import re

class Structure(BaseModel):
    tldr: str = Field(description="finish the following two tasks in order: first, you should answer if the paper is related to (and each of the relating part) DSL or graph processing or MLIR or compiler or HLS. then you should generate a too long; didn't read summary for the paper. you should answer these two continuously and in order.")
    motivation: str = Field(description="describe the motivation in this paper")
    method: str = Field(description="method of this paper")
    result: str = Field(description="result of this paper")
    conclusion: str = Field(description="conclusion of this paper")
