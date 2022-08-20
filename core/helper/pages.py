class PageInfo:
    total_conut:int
    total_page:int
    page_end:bool

    class Config:
        orm_mode = True
