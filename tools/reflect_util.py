from script.entrance.ty import TY

model_module = __import__('script.entrance')
m_py = getattr(model_module, 'ty')
obj = getattr(m_py, TY)
obj('task')
