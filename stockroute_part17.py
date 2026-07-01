# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: StockRoute
class DryRunMixin:
    def __init__(self, dry_run=False):
        self._dry_run = dry_run

    def _execute(self, action_name, func, *args, **kwargs):
        if self._dry_run:
            print(f"[DRY-RUN] Would {action_name}: {func.__name__}({', '.join(repr(a) for a in args)})")
            return None
        else:
            result = func(*args, **kwargs)
            return result

    def commit(self, *args, **kwargs):
        return self._execute("commit", super().commit if hasattr(super(), 'commit') else lambda x,y,z,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a: None, *args, **kwargs)

    def rollback(self, *args, **kwargs):
        return self._execute("rollback", super().rollback if hasattr(super(), 'rollback') else lambda x,y,z,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a: None, *args, **kwargs)

    def save(self, *args, **kwargs):
        return self._execute("save", super().save if hasattr(super(), 'save') else lambda x,y,z,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a: None, *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._execute("delete", super().delete if hasattr(super(), 'delete') else lambda x,y,z,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a: None, *args, **kwargs)

    def update(self, *args, **kwargs):
        return self._execute("update", super().update if hasattr(super(), 'update') else lambda x,y,z,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a: None, *args, **kwargs)

    def create(self, *args, **kwargs):
        return self._execute("create", super().create if hasattr(super(), 'create') else lambda x,y,z,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a: None, *args, **kwargs)

    def execute(self, command_name, *args, **kwargs):
        return self._execute(command_name, getattr(super(), command_name) if hasattr(super(), command_name) else lambda x,y,z,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a: None, *args, **kwargs)
