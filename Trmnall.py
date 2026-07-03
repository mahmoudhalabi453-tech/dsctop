from dstop.GIL import * # أو بقية استدعاءاتك

def run_cmd(CND=None):
    if CND is None:
        CND = []
        
    p2 = Dsktob()
    w = p2.entry(p2.app, x=10, y=10, wid=400, hei=30)
    
    # نضع القيمة الابتدائية هنا على الدالة مباشرة
    run_cmd.if_a = 0 

    def j(event):
        entry_text = p2.get_entry_text(w).strip()
        print(f"[فحص] النص الحالي في الحقل هو: '{entry_text}'")
        
        if entry_text in CND:
            run_cmd.if_a = 1  # تعديل الخاصية التابعة للدالة run_cmd
            print("NANO")
        else:
            run_cmd.if_a = 0  # تعديل الخاصية التابعة للدالة run_cmd
            print("القيمة خاطئة! لن يتم طباعة NANO")

    p2.on_click(w, j, button=1)
    p2.run()

# إعطاء قيمة افتراضية بالخارج منعاً لظهور خطأ الـ AttributeError عند الاستيراد لأول مرة
run_cmd.if_a = 0