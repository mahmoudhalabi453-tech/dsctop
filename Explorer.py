import json  
from dstop.GIL import * def Explorer():
    p = Dsktob()
    w = p.entry(p.app, x=400, y=10)
    Explorer.current_path = ""

    def on_click_handler(event):
        Explorer.current_path = p.get_entry_text(w).strip()
        print(f"[Explorer] تم حفظ المسار الحالي: {Explorer.current_path}")

    p.on_click(w, on_click_handler, button=1)
    p.run()

Explorer.current_path = ""

def json_open(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  
    return data

def json_save(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
